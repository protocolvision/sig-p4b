/**
 * sig-p4b-signup — session sign-ups for npc.here.now/protocolvision
 *
 * Stores name, email, and affiliation in KV so the facilitators can export
 * the list and send reading prep before each session.
 *
 * Routes:
 *   POST /signup       — JSON (fetch) or form-encoded (no-JS fallback, redirects back)
 *   GET  /export.csv   — all sign-ups; requires header X-Export-Secret
 *   GET  /unsubscribe  — ?email=…&t=… (HMAC token included in each export row)
 *   OPTIONS *          — CORS preflight
 *
 * Defenses: honeypot (_hp), 10 requests / hour / IP, length caps, origin allow-list.
 */

interface Env {
  SIGNUPS: KVNamespace;
  EXPORT_SECRET: string;
}

interface Signup {
  name: string;
  email: string;
  affiliation: string;
  ts: string;
  source: string;
}

const SITE = "https://npc.here.now/protocolvision/";
const ALLOWED_ORIGINS = [
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

async function signup(req: Request, env: Env): Promise<Response> {
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

  const row: Signup = {
    name: (body.name || "").trim().slice(0, 100),
    email,
    affiliation: (body.affiliation || "").trim().slice(0, 150),
    ts: new Date().toISOString(),
    source: (body.source || "site").slice(0, 50),
  };
  await env.SIGNUPS.put(`sub:${email}`, JSON.stringify(row));
  return done(true);
}

function csvCell(s: string): string {
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

async function exportCsv(req: Request, env: Env, origin: string): Promise<Response> {
  if (!env.EXPORT_SECRET || req.headers.get("X-Export-Secret") !== env.EXPORT_SECRET) {
    return new Response("Forbidden", { status: 403 });
  }
  const rows: string[] = ["name,email,affiliation,signed_up,source,unsubscribe_url"];
  let cursor: string | undefined;
  do {
    const page = await env.SIGNUPS.list({ prefix: "sub:", cursor });
    for (const k of page.keys) {
      const v = await env.SIGNUPS.get(k.name);
      if (!v) continue;
      const r = JSON.parse(v) as Signup;
      const t = await token(r.email, env.EXPORT_SECRET);
      const unsub = `${origin}/unsubscribe?email=${encodeURIComponent(r.email)}&t=${t}`;
      rows.push([r.name, r.email, r.affiliation, r.ts, r.source, unsub].map(csvCell).join(","));
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
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    if (req.method === "OPTIONS") return new Response(null, { headers: cors(req) });
    if (req.method === "POST" && url.pathname === "/signup") return signup(req, env);
    if (req.method === "GET" && url.pathname === "/export.csv") return exportCsv(req, env, url.origin);
    if (req.method === "GET" && url.pathname === "/unsubscribe") return unsubscribe(url, env);
    return new Response("Not found", { status: 404 });
  },
} satisfies ExportedHandler<Env>;
