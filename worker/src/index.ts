/**
 * sig-p4b-signup — session sign-ups for protocolsforbusiness.com
 *
 * Stores name, email, affiliation, website, GitHub and Discord handles in KV so the facilitators can export
 * the list and send reading prep before each session.
 *
 * Routes:
 *   POST /signup       — JSON (fetch) or form-encoded (no-JS fallback, redirects back)
 *   POST /talk         — an offer to speak at a session; posted to the group's Discord channel (nothing stored)
 *   POST /advisory     — a request for advisory services; posted to the group's Discord channel (nothing stored)
 *   GET  /export.csv   — all sign-ups; requires header X-Export-Secret
 *   GET  /unsubscribe  — ?email=…&t=… (HMAC token included in each export row)
 *   POST /unsubscribe  — email only, from the site's unsubscribe page; same answer whether or not it was listed
 *   GET  /digest       — preview this week's blyg digest (requires X-Export-Secret); nothing is posted
 *   POST /digest       — send the digest now (requires X-Export-Secret)
 *   cron (Fridays)     — post the week's blyg digest to the group's Discord channel, if anything changed
 *   OPTIONS *          — CORS preflight
 *
 * Defenses: honeypot (_hp), 10 requests / hour / IP, length caps, origin allow-list.
 */

interface Env {
  SIGNUPS: KVNamespace;
  EXPORT_SECRET: string;
  SITE?: string;             // public site, used for redirects back after a no-JS form post
  ALLOWED_ORIGINS?: string;  // comma-separated origins allowed to call /signup from a browser
  DISCORD_WEBHOOK?: string;  // secret: a Discord channel webhook; new sign-ups post a short note there
  MENTIONS?: KVNamespace;    // the blyg's Webmentions, written by site/worker.js; read here for the weekly digest
}

interface Signup {
  name: string;
  email: string;
  affiliation: string;
  website: string;
  github: string;
  discord: string;
  role?: string;
  ts: string;        // first signed up (kept on re-registration)
  source: string;    // where they first signed up (kept on re-registration)
  updated?: string;  // latest registration that changed or confirmed the record
}

// Defaults; a deployment overrides them with SITE and ALLOWED_ORIGINS in wrangler.jsonc "vars".
let SITE = "https://protocolsforbusiness.com/";
let ALLOWED_ORIGINS = [
  "https://protocolsforbusiness.com",
  "https://www.protocolsforbusiness.com",
  "http://localhost:8000",
  "http://127.0.0.1:8000",
];
const RATE_LIMIT_PER_HOUR = 10;
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function cors(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") || "";
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };
}

function json(req: Request, body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...cors(req) },
  });
}

async function token(email: string, secret: string): Promise<string> {
  const key = await crypto.subtle.importKey(
    "raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(email));
  return [...new Uint8Array(sig)].slice(0, 16).map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function rateLimited(env: Env, ip: string): Promise<boolean> {
  const key = `rl:${ip}:${new Date().toISOString().slice(0, 13)}`;
  const n = parseInt((await env.SIGNUPS.get(key)) || "0", 10);
  if (n >= RATE_LIMIT_PER_HOUR) return true;
  await env.SIGNUPS.put(key, String(n + 1), { expirationTtl: 3600 });
  return false;
}

async function readBody(req: Request): Promise<Record<string, string>> {
  const type = req.headers.get("Content-Type") || "";
  if (type.includes("application/json")) return (await req.json()) as Record<string, string>;
  const form = await req.formData();
  const out: Record<string, string> = {};
  for (const [k, v] of form.entries()) out[k] = String(v);
  return out;
}

function clean(v: unknown, max: number): string {
  // Plain text only: trim, cap length, strip control characters.
  return String(v ?? "").replace(/[\u0000-\u001f\u007f]/g, "").trim().slice(0, max);
}

// A short note to the group's Discord channel when someone new registers. It carries no personal
// details (registrants haven't agreed to be announced), only that someone joined and the new total.
// Test addresses on example.com are skipped. Failures never affect the sign-up.
async function notifyDiscord(env: Env): Promise<void> {
  if (!env.DISCORD_WEBHOOK) return;
  let count = 0, cursor: string | undefined;
  do {
    const page = await env.SIGNUPS.list({ prefix: "sub:", cursor });
    count += page.keys.length;
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor);
  try {
    await fetch(env.DISCORD_WEBHOOK, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: "Protocols for Business sign-ups",
        content: `New sign-up for Protocols for Business session emails. ${count} people are now registered.`,
        allowed_mentions: { parse: [] },
      }),
    });
  } catch { /* ignore: the note is a courtesy */ }
}

async function signup(req: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
  const isForm = !(req.headers.get("Content-Type") || "").includes("application/json");
  const done = (ok: boolean, error?: string) =>
    isForm
      ? Response.redirect(`${SITE}?signup=${ok ? "ok" : "error"}#join`, 303)
      : json(req, ok ? { ok: true } : { error }, ok ? 200 : 400);

  let body: Record<string, string>;
  try {
    body = await readBody(req);
  } catch {
    return done(false, "Could not read the form.");
  }
  if (body._hp) return done(true); // honeypot: pretend success

  const email = (body.email || "").trim().toLowerCase().slice(0, 200);
  if (!EMAIL_RE.test(email)) return done(false, "Please enter a valid email.");

  const ip = req.headers.get("CF-Connecting-IP") || "unknown";
  if (await rateLimited(env, ip)) return done(false, "Too many attempts. Try again later.");

  let website = clean(body.website, 200);
  if (website && !/^https?:\/\//i.test(website)) website = "https://" + website;
  if (website && !/^https?:\/\/[^\s]+\.[^\s]+$/i.test(website)) return done(false, "Please check the website address.");
  const now = new Date().toISOString();
  const incoming: Signup = {
    name: clean(body.name, 100),
    email,
    affiliation: clean(body.affiliation, 150),
    website,
    github: clean(body.github, 60).replace(/^@/, "").replace(/^https?:\/\/github\.com\//i, "").replace(/\/$/, ""),
    discord: clean(body.discord, 60).replace(/^@/, ""),
    ts: now,
    source: (body.source || "site").slice(0, 50),
  };
  // Re-registration merges: non-empty new fields update the record, empty ones keep what's there,
  // and the original signup date, source, and role are preserved. The response is the same either
  // way, so the form never reveals whether an address was already on the list.
  let row = incoming;
  const prevRaw = await env.SIGNUPS.get(`sub:${email}`);
  if (prevRaw) {
    try {
      const prev = JSON.parse(prevRaw) as Signup;
      const pick = (a: string, b: string | undefined) => (a ? a : b ?? "");
      row = {
        name: pick(incoming.name, prev.name),
        email,
        affiliation: pick(incoming.affiliation, prev.affiliation),
        website: pick(incoming.website, prev.website),
        github: pick(incoming.github, prev.github),
        discord: pick(incoming.discord, prev.discord),
        role: prev.role,
        ts: prev.ts || now,
        source: prev.source || incoming.source,
        updated: now,
      };
    } catch { /* unreadable old record: store the new one */ }
  }
  await env.SIGNUPS.put(`sub:${email}`, JSON.stringify(row));
  if (!prevRaw && !email.endsWith("@example.com")) ctx.waitUntil(notifyDiscord(env));
  return done(true);
}

// Talk offers go straight to the group's Discord channel so the facilitators can reply. The form tells
// the speaker that what they send, including their contact, is posted there. Nothing is stored.
const THEMES = ["Agents", "Nature", "Emissions", "Incidents", "Hardness", "Liveness", "Not sure"];
async function talk(req: Request, env: Env): Promise<Response> {
  const isForm = !(req.headers.get("Content-Type") || "").includes("application/json");
  const done = (ok: boolean, error?: string) =>
    isForm
      ? Response.redirect(`${SITE}research/?talk=${ok ? "ok" : "error"}#speak`, 303)
      : json(req, ok ? { ok: true } : { error }, ok ? 200 : 400);
  let body: Record<string, string>;
  try {
    body = await readBody(req);
  } catch {
    return done(false, "Could not read the form.");
  }
  if (body._hp) return done(true);
  const name = clean(body.name, 100), contact = clean(body.contact, 150), title = clean(body.title, 200);
  const theme = THEMES.includes(body.theme) ? body.theme : "Not sure";
  const about = clean(String(body.about ?? "").replace(/\r?\n/g, " "), 1200), when = clean(body.when, 80);
  let link = clean(body.link, 300);
  if (link && !/^https?:\/\//i.test(link)) link = "https://" + link;
  if (link && !/^https?:\/\/[^\s]+\.[^\s]+$/i.test(link)) return done(false, "Please check the link.");
  if (!name || !contact || !title) return done(false, "Please add your name, a way to reach you, and a title.");
  const ip = req.headers.get("CF-Connecting-IP") || "unknown";
  if (await rateLimited(env, ip)) return done(false, "Too many attempts. Try again later.");
  if (!env.DISCORD_WEBHOOK) return done(false, "Talk offers are not set up yet. Message @rafa_0x on Discord.");
  const fields = [
    { name: "From", value: name, inline: true },
    { name: "Contact", value: contact, inline: true },
    { name: "Theme", value: theme, inline: true },
    ...(when ? [{ name: "Preferred timing", value: when, inline: true }] : []),
    ...(link ? [{ name: "Link", value: link }] : []),
  ];
  const r = await fetch(env.DISCORD_WEBHOOK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "Protocols for Business talk offers",
      content: "New offer to speak at a Protocols for Business session:",
      embeds: [{ title: title.slice(0, 250), description: about || undefined, fields, color: 0x004fcc }],
      allowed_mentions: { parse: [] },   // nobody gets pinged, whatever the text says
    }),
  });
  return r.ok ? done(true) : done(false, "Could not send right now. Message @rafa_0x on Discord.");
}

// Advisory requests go to the same channel, the same way: nothing stored, mentions never ping.
async function advisory(req: Request, env: Env): Promise<Response> {
  const isForm = !(req.headers.get("Content-Type") || "").includes("application/json");
  const done = (ok: boolean, error?: string) =>
    isForm
      ? Response.redirect(`${SITE}?advisory=${ok ? "ok" : "error"}`, 303)
      : json(req, ok ? { ok: true } : { error }, ok ? 200 : 400);
  let body: Record<string, string>;
  try {
    body = await readBody(req);
  } catch {
    return done(false, "Could not read the form.");
  }
  if (body._hp) return done(true);
  const name = clean(body.name, 100), contact = clean(body.contact, 150), org = clean(body.org, 150);
  const need = clean(String(body.need ?? "").replace(/\r?\n/g, " "), 1500), when = clean(body.when, 80);
  if (!name || !contact || !need) return done(false, "Please add your name, a way to reach you, and what you need.");
  const ip = req.headers.get("CF-Connecting-IP") || "unknown";
  if (await rateLimited(env, ip)) return done(false, "Too many attempts. Try again later.");
  if (!env.DISCORD_WEBHOOK) return done(false, "Requests are not set up yet. Message @rafa_0x on Discord.");
  const fields = [
    { name: "From", value: name, inline: true },
    { name: "Contact", value: contact, inline: true },
    ...(org ? [{ name: "Organization", value: org, inline: true }] : []),
    ...(when ? [{ name: "Timing", value: when, inline: true }] : []),
  ];
  const r = await fetch(env.DISCORD_WEBHOOK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "Protocols for Business advisory requests",
      content: "New request for advisory services:",
      embeds: [{ title: org ? `Advisory request from ${org}`.slice(0, 250) : "Advisory request", description: need, fields, color: 0x0f6e56 }],
      allowed_mentions: { parse: [] },
    }),
  });
  return r.ok ? done(true) : done(false, "Could not send right now. Message @rafa_0x on Discord.");
}

function csvCell(s: string): string {
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

async function exportCsv(req: Request, env: Env, origin: string): Promise<Response> {
  if (!env.EXPORT_SECRET || req.headers.get("X-Export-Secret") !== env.EXPORT_SECRET) {
    return new Response("Forbidden", { status: 403 });
  }
  const rows: string[] = ["name,email,affiliation,website,github,discord,role,signed_up,source,updated,unsubscribe_url"];
  let cursor: string | undefined;
  do {
    const page = await env.SIGNUPS.list({ prefix: "sub:", cursor });
    for (const k of page.keys) {
      const v = await env.SIGNUPS.get(k.name);
      if (!v) continue;
      const r = JSON.parse(v) as Signup;
      const t = await token(r.email, env.EXPORT_SECRET);
      const unsub = `${origin}/unsubscribe?email=${encodeURIComponent(r.email)}&t=${t}`;
      rows.push([r.name, r.email, r.affiliation, r.website ?? "", r.github ?? "", r.discord ?? "", r.role ?? "member", r.ts, r.source, r.updated ?? "", unsub]
        .map(csvCell).join(","));
    }
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor);
  return new Response(rows.join("\n") + "\n", {
    headers: { "Content-Type": "text/csv; charset=utf-8", "Cache-Control": "no-store" },
  });
}

async function unsubscribe(url: URL, env: Env): Promise<Response> {
  const email = (url.searchParams.get("email") || "").toLowerCase();
  const t = url.searchParams.get("t") || "";
  const page = (msg: string) =>
    new Response(
      `<!doctype html><meta charset="utf-8"><title>Protocols for Business</title>` +
        `<body style="font:17px/1.6 Georgia,serif;max-width:36rem;margin:4rem auto;padding:0 1rem">` +
        `<p>${msg}</p><p><a href="${SITE}">Back to the site</a></p>`,
      { headers: { "Content-Type": "text/html; charset=utf-8" } },
    );
  if (!email || t !== (await token(email, env.EXPORT_SECRET))) return page("That link is not valid.");
  await env.SIGNUPS.delete(`sub:${email}`);
  return page("You're unsubscribed from session emails.");
}

// The site's general unsubscribe page: enter an email, it's removed. The answer is the same whether or
// not the address was on the list, so the form can't be used to check who signed up.
async function unsubscribeForm(req: Request, env: Env): Promise<Response> {
  const isForm = !(req.headers.get("Content-Type") || "").includes("application/json");
  const done = (ok: boolean, error?: string) =>
    isForm
      ? Response.redirect(`${SITE}unsubscribe/?${ok ? "done=1" : "error=1"}`, 303)
      : json(req, ok ? { ok: true } : { error }, ok ? 200 : 400);
  let body: Record<string, string>;
  try {
    body = await readBody(req);
  } catch {
    return done(false, "Could not read the form.");
  }
  if (body._hp) return done(true);
  const email = (body.email || "").trim().toLowerCase().slice(0, 200);
  if (!EMAIL_RE.test(email)) return done(false, "Please enter a valid email.");
  const ip = req.headers.get("CF-Connecting-IP") || "unknown";
  if (await rateLimited(env, ip)) return done(false, "Too many attempts. Try again later.");
  await env.SIGNUPS.delete(`sub:${email}`);
  return done(true);
}

// Weekly blyg digest: one Discord message listing what was published or updated on the blyg in the
// past seven days, read from the site's public blyg index. Nothing is sent in a quiet week.
interface BlygIndexItem { id: string; kind: string; created: string; updated: string; version: number }

function titleOf(md: string): string {
  const lines = md.split("\n").map((l) => l.trim()).filter(Boolean);
  const h = lines.find((l) => l.startsWith("# "));
  const t = (h ? h.slice(2) : (lines[0] || "Untitled")).replace(/[*_`]/g, "").replace(/\[([^\]]*)\]\([^)]*\)/g, "$1");
  return t.length > 90 ? t.slice(0, 87).trimEnd() + "…" : t;
}

async function buildDigest(env: Env, now = Date.now()): Promise<string | null> {
  const base = SITE + "blyg/";
  const res = await fetch(base + "items/index.json", { cf: { cacheTtl: 0 } } as RequestInit);
  if (!res.ok) return null;
  const index = (await res.json()) as { items: BlygIndexItem[] };
  const since = now - 7 * 24 * 3600 * 1000;
  const recent = index.items.filter((i) => Date.parse(i.updated) >= since);
  const upcoming = await nextSession(now);
  const responses = await recentResponses(env, since);
  if (!recent.length && !upcoming && !responses.length) return null;
  const fresh: string[] = [], changed: string[] = [];
  for (const i of recent.sort((a, b) => Date.parse(b.updated) - Date.parse(a.updated))) {
    const r = await fetch(base + `items/${i.id}.json`);
    if (!r.ok) continue;
    const item = (await r.json()) as { page: string; content_md: string };
    const line = `• [${titleOf(item.content_md)}](${base}${item.page})`;
    (Date.parse(i.created) >= since ? fresh : changed).push(line);
  }
  const fmt = (t: number) => new Date(t).toLocaleDateString("en-GB", { day: "numeric", month: "short", timeZone: "UTC" });
  const parts = [`**This week on the Protocols for Business blyg** (${fmt(since)} – ${fmt(now)})`];
  if (fresh.length) parts.push(`**New**\n` + fresh.join("\n"));
  if (changed.length) parts.push(`**Updated**\n` + changed.slice(0, 8).join("\n") + (changed.length > 8 ? `\n…and ${changed.length - 8} more` : ""));
  if (responses.length) parts.push(`**Responses from other blygs**\n` + responses.join("\n"));
  if (upcoming) parts.push(upcoming);
  parts.push(`All posts: ${base} · feed: ${base}feed.xml`);
  let msg = parts.join("\n\n");
  if (msg.length > 1900) msg = msg.slice(0, 1890) + "…";
  return msg;
}

// Webmentions verified in the past week: who responded to which of our posts.
async function recentResponses(env: Env, since: number): Promise<string[]> {
  if (!env.MENTIONS) return [];
  const out: string[] = [];
  let cursor: string | undefined;
  do {
    const page = await env.MENTIONS.list({ prefix: "m:", cursor });
    for (const k of page.keys) {
      const m = JSON.parse((await env.MENTIONS.get(k.name)) || "null");
      if (!m || m.status !== "verified" || Date.parse(m.checked || "") < since) continue;
      const verb = ({ stub: "responded to", transclusion: "quoted", fork: "forked" } as Record<string, string>)[m.relation] || "mentioned";
      out.push(`• [${m.author || new URL(m.page).host} ${verb} our post](${m.page})`);
    }
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor);
  return out.slice(0, 8);
}

// The next session, from the site's public schedule: date, time in UTC, the reading, what else happens.
async function nextSession(now: number): Promise<string | null> {
  const r = await fetch(SITE + "sessions.json");
  if (!r.ok) return null;
  const S = (await r.json()) as { start_utc: string; end_utc: string; title: string; url: string; cite: string; feature_short: string }[];
  const n = S.find((x) => Date.parse(x.end_utc) > now);
  if (!n) return null;
  const d = new Date(n.start_utc);
  const day = d.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", timeZone: "UTC" });
  return `**Next session** · ${day}, ${n.start_utc.slice(11, 16)}–${n.end_utc.slice(11, 16)} UTC · ${n.feature_short}\n` +
    `Reading: [${n.title}](${n.url}) (${n.cite}) · nothing to prepare, we read together\nGet session emails: ${SITE}`;
}

async function postDigest(env: Env): Promise<void> {
  if (!env.DISCORD_WEBHOOK) return;
  const content = await buildDigest(env);
  if (!content) return;
  await fetch(env.DISCORD_WEBHOOK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: "Protocols for Business blyg", content, allowed_mentions: { parse: [] }, flags: 4 }),   // 4: no link previews
  });
}

export default {
  async fetch(req: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    if (env.SITE) SITE = env.SITE;
    if (env.ALLOWED_ORIGINS) ALLOWED_ORIGINS = env.ALLOWED_ORIGINS.split(",").map((o) => o.trim()).filter(Boolean);
    const url = new URL(req.url);
    if (req.method === "OPTIONS") return new Response(null, { headers: cors(req) });
    if (req.method === "POST" && url.pathname === "/signup") return signup(req, env, ctx);
    if (req.method === "POST" && url.pathname === "/talk") return talk(req, env);
    if (req.method === "POST" && url.pathname === "/advisory") return advisory(req, env);
    if (req.method === "GET" && url.pathname === "/export.csv") return exportCsv(req, env, url.origin);
    if (req.method === "GET" && url.pathname === "/unsubscribe") return unsubscribe(url, env);
    if (req.method === "GET" && url.pathname === "/digest") {
      if (!env.EXPORT_SECRET || req.headers.get("X-Export-Secret") !== env.EXPORT_SECRET) return new Response("Forbidden", { status: 403 });
      return new Response((await buildDigest(env)) ?? "(nothing new this week; no message would be sent)", { headers: { "Content-Type": "text/plain; charset=utf-8" } });
    }
    if (req.method === "POST" && url.pathname === "/digest") {   // send it now (same secret), e.g. the first one
      if (!env.EXPORT_SECRET || req.headers.get("X-Export-Secret") !== env.EXPORT_SECRET) return new Response("Forbidden", { status: 403 });
      await postDigest(env);
      return new Response("sent (if there was anything to say)\n", { headers: { "Content-Type": "text/plain; charset=utf-8" } });
    }
    if (req.method === "POST" && url.pathname === "/unsubscribe") return unsubscribeForm(req, env);
    return new Response("Not found", { status: 404 });
  },
  async scheduled(_event: ScheduledController, env: Env, ctx: ExecutionContext): Promise<void> {
    if (env.SITE) SITE = env.SITE;
    ctx.waitUntil(postDigest(env));
  },
} satisfies ExportedHandler<Env>;
