// Webmention receiving for the blyg (Blygger 0.3 §15): accept a claim, verify it structurally, keep a pointer.
// Only blyg-to-blyg mentions are accepted (stub, transclusion, fork); plain web links are not (§15.6).
// Verified mentions are shown as a "Responses" list on the item's page; nothing enters the feed or item files (§15.5).

const LIMITS = { perHost: 60, perDomain: 120, global: 300 };              // claims per hour (§15.3)
const FETCH = { maxFetches: 2, maxRedirects: 3, timeoutMs: 5000, maxBytes: 1_000_000 };   // §15.4

const normOrigin = (u) => {
  try {
    const x = new URL(u);
    return `${x.protocol}//${x.host}${x.pathname.endsWith("/") ? x.pathname : x.pathname + "/"}`;
  } catch { return ""; }
};
const hostOf = (u) => { try { const x = new URL(u); return `${x.protocol}//${x.host}`; } catch { return ""; } };
const domainOf = (host) => host.split(".").slice(-2).join(".");   // a coarse grouping; a heuristic, as the spec allows
const isHttp = (u) => { try { return ["http:", "https:"].includes(new URL(u).protocol); } catch { return false; } };

async function sha(s) {
  const d = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(d)].slice(0, 12).map((b) => b.toString(16).padStart(2, "0")).join("");
}

// The target must be one of our published items: its page (t/{id}/ or f/{id}/) or items/{id}.json.
export function targetId(target, origin) {
  if (!isHttp(target) || hostOf(target) !== hostOf(origin)) return null;
  const base = new URL(origin).pathname;
  const path = new URL(target).pathname;
  if (!path.startsWith(base)) return null;
  const m = path.slice(base.length).match(/^(?:[tf]\/([0-9a-z]{26})\/?|items\/([0-9a-z]{26})\.json)$/);
  return m ? m[1] || m[2] : null;
}

async function bump(kv, key) {
  const n = parseInt((await kv.get(key)) || "0", 10) + 1;
  await kv.put(key, String(n), { expirationTtl: 3600 });
  return n;
}

// §15.3: syntactic checks (400), rate limits (429), then accept (202) and verify asynchronously.
export async function receive(req, env, ctx, origin, itemExists, pinnedOf = async () => []) {
  const form = await req.formData().catch(() => null);
  const source = form && String(form.get("source") || ""), target = form && String(form.get("target") || "");
  if (!source || !target || !isHttp(source) || !isHttp(target) || source === target)
    return new Response("source and target must be different absolute http(s) URLs\n", { status: 400 });
  const id = targetId(target, origin);
  if (!id || !(await itemExists(id))) return new Response("target is not a published item of this blyg\n", { status: 400 });
  const host = new URL(source).host, hour = new Date().toISOString().slice(0, 13);
  const over = (await bump(env.MENTIONS, `rl:h:${host}:${hour}`)) > LIMITS.perHost
    || (await bump(env.MENTIONS, `rl:d:${domainOf(host)}:${hour}`)) > LIMITS.perDomain
    || (await bump(env.MENTIONS, `rl:g:${hour}`)) > LIMITS.global;
  if (over) return new Response("too many mentions; try later\n", { status: 429 });
  const key = `m:${id}:${await sha(source)}`;
  const prev = JSON.parse((await env.MENTIONS.get(key)) || "null");
  await env.MENTIONS.put(key, JSON.stringify({ ...(prev || {}), source, target, target_id: id, status: prev?.status || "pending", received: new Date().toISOString() }));
  ctx.waitUntil(pinnedOf(id).then((pins) => verify(env, key, source, id, origin, (v) => pins.includes(v))));
  return new Response("accepted; verifying\n", { status: 202 });
}

// A bounded fetch: manual redirects, a time limit and a body-size cap. Returns { url, type, text } or null.
async function boundedGet(url, budget) {
  let current = url;
  for (let hop = 0; hop <= FETCH.maxRedirects; hop++) {
    if (budget.fetches++ >= FETCH.maxFetches + FETCH.maxRedirects) return null;
    const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), FETCH.timeoutMs);
    let r;
    try { r = await fetch(current, { redirect: "manual", signal: ctl.signal, headers: { Accept: "application/json, text/html;q=0.9" } }); }
    catch { clearTimeout(t); return null; }
    if ([301, 302, 303, 307, 308].includes(r.status)) {
      clearTimeout(t);
      const loc = r.headers.get("Location"); if (!loc) return null;
      current = new URL(loc, current).toString(); continue;
    }
    if (!r.ok) { clearTimeout(t); return null; }
    const reader = r.body.getReader(); const chunks = []; let size = 0;
    for (;;) {
      const { done, value } = await reader.read(); if (done) break;
      size += value.length; if (size > FETCH.maxBytes) { clearTimeout(t); return null; }
      chunks.push(value);
    }
    clearTimeout(t);
    const buf = new Uint8Array(size); let o = 0; for (const c of chunks) { buf.set(c, o); o += c.length; }
    return { url: current, type: r.headers.get("Content-Type") || "", text: new TextDecoder().decode(buf) };
  }
  return null;
}

const refIs = (ref, origin, id) => ref && normOrigin(ref.origin || "") === normOrigin(origin) && ref.id === id;

// §15.4: fetch the source; it must be (or point to) a blyg item document from its own origin that names the target.
export async function verifyDoc(source, id, origin, pinned = () => false) {
  const budget = { fetches: 0 };
  const parse = (s) => { try { return JSON.parse(s); } catch { return null; } };
  let got = await boundedGet(source, budget);
  if (!got) return { status: "failed", reason: "source unreachable" };
  let doc = parse(got.text);
  if (!(doc && typeof doc === "object" && doc.blyg)) {
    const m = got.text.match(/<link[^>]+rel=["']alternate["'][^>]*type=["']application\/json["'][^>]*>|<link[^>]+type=["']application\/json["'][^>]*rel=["']alternate["'][^>]*>/i);
    const href = m && (m[0].match(/href=["']([^"']+)["']/i) || [])[1];
    if (!href) return { status: "failed", reason: "no blyg item document" };
    got = await boundedGet(new URL(href, got.url).toString(), budget);
    doc = got && parse(got.text);
    if (!(doc && typeof doc === "object" && doc.blyg)) return { status: "failed", reason: "not a blyg item document" };
  }
  if (hostOf(doc.origin || "") !== hostOf(got.url)) return { status: "failed", reason: "document origin does not match where it was fetched" };
  if (doc.kind === "withdrawn") return { status: "gone", reason: "source withdrawn" };
  let relation = null;
  if (refIs(doc.stub_of, origin, id)) relation = "stub";
  else if ((doc.transclusions || []).some((t) => t.origin && refIs(t, origin, id))) relation = "transclusion";
  else if (refIs(doc.forked_from, origin, id) && pinned(doc.forked_from.version)) relation = "fork";
  if (!relation) return { status: "failed", reason: "document does not reference this item" };
  return {
    status: "verified", relation, source_id: doc.id, source_origin: doc.origin, source_version: doc.version,
    source_kind: doc.kind, source_updated: doc.updated || null, author: doc.author?.name || null,
    page: doc.page ? new URL(doc.page, doc.origin).toString() : source,
  };
}

async function verify(env, key, source, id, origin, pinned) {
  const result = await verifyDoc(source, id, origin, pinned);
  const prev = JSON.parse((await env.MENTIONS.get(key)) || "{}");
  // A mention that verified before and fails now becomes "gone" and is kept (§15.4).
  const status = result.status === "failed" && prev.status === "verified" ? "gone" : result.status;
  await env.MENTIONS.put(key, JSON.stringify({ ...prev, ...result, status, checked: new Date().toISOString() }));
}

async function verified(env, prefix) {
  const out = [];
  let cursor;
  do {
    const page = await env.MENTIONS.list({ prefix, cursor });
    for (const k of page.keys) {
      const m = JSON.parse((await env.MENTIONS.get(k.name)) || "null");
      if (m && m.status === "verified") out.push(m);
    }
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor);
  return out;
}

// Verified mentions of one item, for its page.
export async function listFor(env, id) {
  return (await verified(env, `m:${id}:`))
    .map((m) => ({ author: m.author, page: m.page, relation: m.relation, origin: m.source_origin, checked: m.checked }));
}

// Verified mentions of every item, newest first: pointers for the blyg page, built hourly (tools/build_blyg.py).
export async function listRecent(env, limit = 50) {
  return (await verified(env, "m:"))
    .map((m) => ({ target_id: m.target_id, author: m.author, page: m.page, relation: m.relation, origin: m.source_origin,
      source_id: m.source_id, source_version: m.source_version, source_kind: m.source_kind,
      at: m.source_updated || m.checked }))
    .sort((a, b) => String(b.at).localeCompare(String(a.at)))
    .slice(0, limit);
}
