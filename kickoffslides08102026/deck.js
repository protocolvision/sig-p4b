// The kickoff deck's live layer: reactions on every slide, taps and polls, a question feed with upvotes, and
// intros sent from the deck. Everything goes to /api/kickoff/ (site/kickoff.js) and is recorded in D1.
// Counts refresh every few seconds while the page is visible. Without the API, the deck still reads fine.
(() => {
  const API = "/api/kickoff/";
  const REDUCE = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, el = document) => el.querySelector(s), $$ = (s, el = document) => [...el.querySelectorAll(s)];

  // One random id per browser, so a tap counts once and can be undone. Nothing else identifies anyone.
  const client = (() => {
    const fresh = () => btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(16)))).replace(/[+/=]/g, (c) => ({ "+": "-", "/": "_", "=": "" })[c]);
    try { let id = localStorage.getItem("kickoff-client"); if (!id) { id = fresh(); localStorage.setItem("kickoff-client", id); } return id; }
    catch { return fresh(); }
  })();

  let S = { counts: {}, mine: {}, questions: [], sent: [] }, online = false;
  const post = async (path, data) => {
    const r = await fetch(API + path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ client, ...data }) });
    const out = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(out.error || "Couldn't send that. Try again?");
    S = out; online = true; render(); return out;
  };
  const refresh = async () => {
    try { const r = await fetch(`${API}state?client=${client}`); if (r.ok) { S = await r.json(); online = true; render(); } }
    catch { online = false; }
  };

  // ---- reactions: three on every slide, in its footer ----
  const REACT = [["question", "❓", "I have a question"], ["heart", "❤️", "Love this"], ["idea", "💡", "This gave me an idea"]];
  $$(".slide").forEach((s) => {
    const foot = $(".foot", s); if (!foot) return;
    const bar = document.createElement("div"); bar.className = "react";
    bar.innerHTML = REACT.map(([k, e, l]) => `<button type="button" data-poll="react:${s.id}" data-option="${k}" aria-label="${l}" title="${l}"><span aria-hidden="true">${e}</span><b data-count></b></button>`).join("");
    foot.prepend(bar);
  });

  // ---- anything with data-poll + data-option is a tap: toggle it, show its count ----
  const tap = async (el) => {
    const poll = el.dataset.poll, option = el.dataset.option, on = !(S.mine[poll] || []).includes(option);
    // Show it at once; the server's answer replaces this guess.
    const mine = new Set(S.mine[poll] || []), c = (S.counts[poll] ||= {});
    if (el.closest("[data-single]") && on) { for (const o of mine) c[o] = Math.max(0, (c[o] || 1) - 1); mine.clear(); }
    on ? mine.add(option) : mine.delete(option); c[option] = Math.max(0, (c[option] || 0) + (on ? 1 : -1));
    S.mine[poll] = [...mine]; render();
    try { await post("vote", { poll, option, on }); } catch { refresh(); }
  };
  document.addEventListener("click", (e) => {
    const el = e.target.closest("[data-poll][data-option]"); if (!el || e.target.closest("a")) return;
    const asking = el.dataset.option === "question" && el.dataset.poll.startsWith("react:") && !(S.mine[el.dataset.poll] || []).includes("question");
    tap(el);
    if (asking) { setQa(true); setTimeout(() => $("#qa-form textarea")?.focus(), 280); }   // ❓ opens the question panel, ready to type (after it slides in)
  });
  document.addEventListener("keydown", (e) => {
    const el = e.target.closest?.("[data-poll][data-option]");
    if (el && el.tagName !== "BUTTON" && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); tap(el); }
  });

  // ---- the question feed, in a side panel ----
  const qa = $("#qa"), qList = $("#qa-list"), qForm = $("#qa-form"), qBtn = $("#qa-open");
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  // Open beside the slides on wide screens; on phones it's a sheet you open from the top bar.
  function setQa(open) { document.body.classList.toggle("qa-open", open); qBtn?.setAttribute("aria-expanded", open); }
  setQa(matchMedia("(min-width: 1500px)").matches);
  qBtn?.addEventListener("click", () => { const open = !document.body.classList.contains("qa-open"); setQa(open); if (open) setTimeout(() => $("textarea", qForm).focus(), 280); });
  $("#qa-close")?.addEventListener("click", () => setQa(false));
  qForm?.addEventListener("submit", async (e) => {
    e.preventDefault(); const t = $("textarea", qForm), note = $(".note", qForm);
    if (t.value.trim().length < 3) return;
    try { await post("question", { text: t.value }); t.value = ""; note.textContent = "Added. Upvote the ones you want answered."; }
    catch (err) { note.textContent = err.message; }
  });
  qList?.addEventListener("click", async (e) => {
    const b = e.target.closest("button[data-q]"); if (!b) return;
    const q = S.questions.find((x) => x.id === +b.dataset.q); if (!q) return;
    q.mine = !q.mine; q.n += q.mine ? 1 : -1; render();
    try { await post("upvote", { qid: q.id, on: q.mine }); } catch { refresh(); }
  });

  // ---- intros (slides 8 and 9): copy a prompt, paste what the assistant wrote, check it, send ----
  const field = (raw, label) => (raw.match(new RegExp(`^\\s*\\**${label}\\**\\s*:\\s*(.*)$`, "im")) || [])[1]?.trim() || "";
  const parse = (raw) => {
    const name = field(raw, "Name"), website = field(raw, "Website");
    const m = raw.match(/^\s*\**Case study idea\**\s*:\s*([\s\S]*)$/im);
    return { name, website, case_text: m ? m[1].trim() : "" };
  };
  $$("[data-copy-prompt]").forEach((b) => b.addEventListener("click", async () => {
    const text = $("#intro-prompt").textContent.trim(), note = b.parentElement.querySelector(".note");
    try { await navigator.clipboard.writeText(text); note.textContent = "Copied. Paste it into your AI assistant."; }
    catch { note.textContent = "Couldn't copy. Open “Read the prompt” and copy it by hand."; }
  }));
  $$("form[data-intro]").forEach((f) => {
    const t = $("textarea", f), preview = $(".preview", f), note = $(".note", f);
    const show = () => {
      const p = parse(t.value);
      preview.innerHTML = t.value.trim() ? (p.name || p.website || p.case_text
        ? `<b>${esc(p.name || "No name yet")}</b>${p.website ? ` · ${esc(p.website)}` : ""}${p.case_text ? `<br>${esc(p.case_text.slice(0, 220))}${p.case_text.length > 220 ? "…" : ""}` : ""}`
        : "Couldn't find “Name:”, “Website:” or “Case study idea:” lines. We'll send it as you wrote it.") : "";
    };
    t.addEventListener("input", show);
    f.addEventListener("submit", async (e) => {
      e.preventDefault(); if (!t.value.trim()) { note.textContent = "Paste what your assistant wrote first."; return; }
      try { await post("entry", { kind: "intro", raw: t.value, ...parse(t.value) }); note.textContent = "Thanks! The hosts have it."; t.value = ""; show(); }
      catch (err) { note.textContent = err.message; }
    });
  });

  // ---- paid work (slide 9): tap to say you're interested, then leave an email ----
  $("#paid-form")?.addEventListener("submit", async (e) => {
    e.preventDefault(); const f = e.target, note = $(".note", f), email = $("input[type=email]", f).value;
    try { await post("entry", { kind: "paid", email, name: $("input[name=name]", f).value }); note.textContent = "Thanks! Rafael will be in touch."; f.reset(); }
    catch (err) { note.textContent = err.message; }
  });

  // ---- draw the current state into the page ----
  function render() {
    $$("[data-poll][data-option]").forEach((el) => {
      const n = S.counts[el.dataset.poll]?.[el.dataset.option] || 0, on = (S.mine[el.dataset.poll] || []).includes(el.dataset.option);
      el.classList.toggle("on", on); el.setAttribute("aria-pressed", on);
      const c = $("[data-count]", el); if (c) c.textContent = n ? n : "";
    });
    $$("[data-single]").forEach((group) => {   // a poll: each option's share, as a bar behind it
      const opts = $$("[data-option]", group), total = opts.reduce((t, o) => t + (S.counts[o.dataset.poll]?.[o.dataset.option] || 0), 0);
      opts.forEach((o) => o.style.setProperty("--pct", total ? `${Math.round(100 * (S.counts[o.dataset.poll]?.[o.dataset.option] || 0) / total)}%` : "0%"));
    });
    const qs = S.questions || [];
    if (qBtn) $("b", qBtn).textContent = qs.length ? qs.length : "";
    if (qList) qList.innerHTML = qs.length ? qs.map((q) => `<li><button type="button" data-q="${q.id}" class="${q.mine ? "on" : ""}" aria-pressed="${q.mine}" aria-label="Upvote"><span aria-hidden="true">▲</span><b>${q.n || ""}</b></button><p>${esc(q.text)}</p></li>`).join("")
      : `<li class="empty">No questions yet. Ask the first one.</li>`;
    $$("[data-sent]").forEach((el) => { el.hidden = !(S.sent || []).includes(el.dataset.sent); });
    document.body.classList.toggle("offline", !online);
  }

  // ---- gentle entrances: each slide settles in the first time it's seen ----
  if (REDUCE || !("IntersectionObserver" in window)) $$(".slide").forEach((s) => s.classList.add("in"));
  else {
    document.documentElement.classList.add("anim");
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .35 });
    $$(".slide").forEach((s) => io.observe(s));
  }

  // ---- drawers: the intro and paid-work forms open beside the slides (a sheet on phones) ----
  document.addEventListener("click", (e) => {
    const open = e.target.closest("[data-open]");
    if (open) { const d = document.getElementById(open.dataset.open); d?.showModal(); d?.querySelector("textarea, input")?.focus(); return; }
    if (e.target.closest("[data-close]")) e.target.closest("dialog")?.close();
    else if (e.target.tagName === "DIALOG") e.target.close();   // a click on the backdrop
  });

  // ---- slide 10: add your blyg, blog or Substack (the sign-up Worker checks the feed and tells the hosts on Discord) ----
  $("#feed-form")?.addEventListener("submit", async (e) => {
    e.preventDefault(); const f = e.target, note = $(".note", f), btn = $("[type=submit]", f);
    if (!f.reportValidity()) return;
    btn.disabled = true; note.textContent = "Checking the address…";
    try {
      const r = await fetch(f.dataset.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(Object.fromEntries(new FormData(f))) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.error || "Something went wrong. Message @rafa_0x on Discord.");
      f.reset(); note.textContent = "Thanks! The hosts will add it."; $$("[data-feed-sent]").forEach((x) => (x.hidden = false));
    } catch (err) { note.textContent = err.message === "Failed to fetch" ? "Couldn't reach the server. Message @rafa_0x on Discord." : err.message; }
    btn.disabled = false;
  });

  // ---- the film slide: play while it's on screen, pause when it isn't ----
  const film = $("iframe.film");
  if (film && "IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => film.contentWindow?.postMessage({ film: e.isIntersecting ? "play" : "pause" }, "*"), { threshold: .6 }).observe(film);
  }

  // ---- the QR code: tap to make it big enough to scan from across the room ----
  $("#qr")?.addEventListener("click", () => $("#qr").classList.toggle("big"));

  render(); refresh();
  let timer = setInterval(() => document.visibilityState === "visible" && refresh(), 4000);
  document.addEventListener("visibilitychange", () => document.visibilityState === "visible" && refresh());
})();
