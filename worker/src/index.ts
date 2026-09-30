/**
 * sig-p4b-signup — session sign-ups for npc.here.now/protocolvision
 *
 * Stores name, email, affiliation, website, GitHub and Discord handles in KV so the facilitators can export
 * the list and send reading prep before each session.
 *
 * Routes:
 *   POST /signup       — JSON (fetch) or form-encoded (no-JS fallback, redirects back)
 *   POST /talk         — an offer to speak at a session; posted to the SIG's Discord channel (nothing stored)
 *   POST /advisory     — a request for advisory services; posted to the SIG's Discord channel (nothing stored)
 *   GET  /export.csv   — all sign-ups; requires header X-Export-Secret
 *   GET  /unsubscribe  — ?email=…&t=… (HMAC token included in each export row)
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
let SITE = "https://npc.here.now/protocolvision/";
let ALLOWED_ORIGINS = [
  "https://npc.here.now",
  "https://scarlet-rapids-8mbp.here.now",
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

// A short note to the SIG's Discord channel when someone new registers. It carries no personal
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
        username: "SIG sign-ups",
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

// Talk offers go straight to the SIG's Discord channel so the facilitators can reply. The form tells
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
      username: "SIG talk offers",
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
      username: "SIG advisory requests",
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
      `<!doctype html><meta charset="utf-8"><title>Protocols for Business SIG</title>` +
        `<body style="font:17px/1.6 Georgia,serif;max-width:36rem;margin:4rem auto;padding:0 1rem">` +
        `<p>${msg}</p><p><a href="${SITE}">Back to the site</a></p>`,
      { headers: { "Content-Type": "text/html; charset=utf-8" } },
    );
  if (!email || t !== (await token(email, env.EXPORT_SECRET))) return page("That link is not valid.");
  await env.SIGNUPS.delete(`sub:${email}`);
  return page("You're unsubscribed from session emails.");
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
    return new Response("Not found", { status: 404 });
  },
} satisfies ExportedHandler<Env>;
