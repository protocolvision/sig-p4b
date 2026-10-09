// The kickoff deck's live layer (/kickoffslides08102026/): reactions, taps, polls, a question feed with upvotes,
// and intros sent from the deck, recorded in D1 (binding KICKOFF, schema in migrations/). Every browser has a
// random client id (kept in its localStorage) so a tap can be undone and counts once; no names, IPs or cookies.
// Intros and emails are never served back out, except through /export with the hosts' token.

const ID = /^[A-Za-z0-9_-]{16,40}$/, KEY = /^[a-z0-9:-]{1,40}$/;
// Which polls exist, and which allow only one choice per person.
const POLLS = { react: "many", there: "many", lesson: "one", theme: "many", paid: "many" };
const json = (body, status = 200) => new Response(JSON.stringify(body), {
  status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });
const clip = (s, n) => String(s ?? "").replace(/\s+$/g, "").slice(0, n);

async function body(request) {
  if (Number(request.headers.get("content-length") || 0) > 8000) return null;
  try { return await request.json(); } catch { return null; }
}

async function state(env, client) {
  const db = env.KICKOFF;
  const [votes, mine, questions, ups] = await db.batch([
    db.prepare("SELECT poll, option, COUNT(*) AS n FROM votes GROUP BY poll, option"),
    db.prepare("SELECT poll, option FROM votes WHERE client = ?").bind(client),
    db.prepare(`SELECT q.id, q.text, q.created, COUNT(u.client) AS n FROM questions q
                LEFT JOIN upvotes u ON u.qid = q.id WHERE q.hidden = 0 GROUP BY q.id ORDER BY n DESC, q.created ASC LIMIT 100`),
    db.prepare("SELECT qid FROM upvotes WHERE client = ?").bind(client),
  ]);
  const counts = {}, own = {};
  for (const r of votes.results) (counts[r.poll] ??= {})[r.option] = r.n;
  for (const r of mine.results) (own[r.poll] ??= []).push(r.option);
  const upped = new Set(ups.results.map((r) => r.qid));
  const sent = await db.prepare("SELECT kind FROM entries WHERE client = ? GROUP BY kind").bind(client).all();
  return { counts, mine: own, questions: questions.results.map((q) => ({ ...q, mine: upped.has(q.id) })),
           sent: sent.results.map((r) => r.kind) };
}

export async function kickoff(request, env, url) {
  if (!env.KICKOFF) return json({ error: "not configured" }, 503);
  const db = env.KICKOFF, path = url.pathname.replace(/^\/api\/kickoff\/?/, ""), now = Date.now();

  if (request.method === "GET" && path === "state") {
    const client = url.searchParams.get("client") || "";
    return json(await state(env, ID.test(client) ? client : "-"));
  }
  if (request.method === "GET" && path === "export") {   // for the hosts: everything, including intros and emails
    const token = (request.headers.get("Authorization") || "").replace(/^Bearer /, "");
    if (!env.KICKOFF_EXPORT_TOKEN || token !== env.KICKOFF_EXPORT_TOKEN) return json({ error: "unauthorized" }, 401);
    const [entries, questions, votes] = await db.batch([
      db.prepare("SELECT * FROM entries ORDER BY created"),
      db.prepare("SELECT q.*, (SELECT COUNT(*) FROM upvotes u WHERE u.qid = q.id) AS upvotes FROM questions q ORDER BY created"),
      db.prepare("SELECT poll, option, COUNT(*) AS n FROM votes GROUP BY poll, option ORDER BY poll, n DESC"),
    ]);
    return json({ entries: entries.results, questions: questions.results, votes: votes.results });
  }
  if (request.method !== "POST") return json({ error: "not found" }, 404);
  const b = await body(request);
  if (!b || !ID.test(b.client || "")) return json({ error: "bad request" }, 400);

  if (path === "vote") {   // {client, poll, option, on}
    const mode = POLLS[String(b.poll).split(":")[0]];
    if (!mode || !KEY.test(b.poll) || !KEY.test(b.option || "")) return json({ error: "bad vote" }, 400);
    const ops = [];
    if (b.on && mode === "one") ops.push(db.prepare("DELETE FROM votes WHERE poll = ? AND client = ?").bind(b.poll, b.client));
    ops.push(b.on
      ? db.prepare("INSERT OR IGNORE INTO votes (poll, option, client, created) VALUES (?, ?, ?, ?)").bind(b.poll, b.option, b.client, now)
      : db.prepare("DELETE FROM votes WHERE poll = ? AND option = ? AND client = ?").bind(b.poll, b.option, b.client));
    await db.batch(ops);
    return json(await state(env, b.client));
  }
  if (path === "question") {   // {client, text}
    const text = clip(b.text, 280).trim();
    if (text.length < 3) return json({ error: "too short" }, 400);
    const { n } = await db.prepare("SELECT COUNT(*) AS n FROM questions WHERE client = ?").bind(b.client).first();
    if (n >= 10) return json({ error: "That's ten questions from you already." }, 429);
    await db.prepare("INSERT INTO questions (text, client, created) VALUES (?, ?, ?)").bind(text, b.client, now).run();
    return json(await state(env, b.client));
  }
  if (path === "upvote") {   // {client, qid, on}
    const qid = Number(b.qid);
    if (!Number.isInteger(qid)) return json({ error: "bad question" }, 400);
    await (b.on
      ? db.prepare("INSERT OR IGNORE INTO upvotes (qid, client, created) SELECT id, ?, ? FROM questions WHERE id = ?").bind(b.client, now, qid)
      : db.prepare("DELETE FROM upvotes WHERE qid = ? AND client = ?").bind(qid, b.client)).run();
    return json(await state(env, b.client));
  }
  if (path === "entry") {   // {client, kind: intro|paid, name, website, case_text, email, raw}
    const kind = b.kind === "paid" ? "paid" : "intro";
    const email = clip(b.email, 200).trim();
    if (kind === "paid" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: "Please add an email address." }, 400);
    const { n } = await db.prepare("SELECT COUNT(*) AS n FROM entries WHERE client = ?").bind(b.client).first();
    if (n >= 20) return json({ error: "Thanks, we have plenty from you already." }, 429);
    await db.prepare(`INSERT INTO entries (kind, name, website, case_text, email, raw, client, created)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)`)
      .bind(kind, clip(b.name, 120), clip(b.website, 300), clip(b.case_text, 2000), email, clip(b.raw, 4000), b.client, now).run();
    return json(await state(env, b.client));
  }
  return json({ error: "not found" }, 404);
}
