/* Shared behaviour for the SIG site: the next-session card and the register dialog.
   Loaded with <script src="…/assets/site.js" data-root="…/" defer>. No dependencies. */
(function () {
  var script = document.currentScript || document.querySelector('script[data-root]');
  /* Deep links into a collapsed syllabus movement: open it, then scroll to the session. */
  function revealHash() {
    var id = decodeURIComponent((location.hash || '').slice(1));
    var el = id && document.getElementById(id);
    if (!el) return;
    var d = el.closest && el.closest('details');
    if (d && !d.open) { d.open = true; el.scrollIntoView({ block: 'start' }); }
  }
  revealHash();
  window.addEventListener('hashchange', revealHash);

  var ROOT = (script && script.getAttribute('data-root')) || './';
  var SIGNUP = ((script && script.getAttribute('data-signup')) || 'https://sig-p4b-signup.rafaeldf2.workers.dev') + '/signup';

  /* Copy buttons: [data-copy="id"] copies that element's text. */
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var src = document.getElementById(b.getAttribute('data-copy'));
      var status = b.parentNode.querySelector('[data-copy-status]');
      var done = function (msg) { if (status) status.textContent = msg; };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(src.textContent).then(function () { done('Copied.'); }, function () { select(); });
      } else { select(); }
      function select() {
        var r = document.createRange(); r.selectNodeContents(src);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
        done('Selected. Press Cmd+C or Ctrl+C to copy.');
      }
    });
  });

  /* Next session: fill every [data-next] card from sessions.json. The static HTML
     already shows the first session, so the card reads correctly without script. */
  var cards = document.querySelectorAll('[data-next]');
  if (cards.length && window.fetch) {
    fetch(ROOT + 'sessions.json').then(function (r) { return r.json(); }).then(function (S) {
      var now = Date.now(), n = null;
      for (var i = 0; i < S.length; i++) { if (Date.parse(S[i].date + 'T16:30:00Z') > now) { n = S[i]; break; } }
      cards.forEach(function (box) {
        var when = box.querySelector('.when'), what = box.querySelector('.what');
        if (!n) { when.textContent = 'The year is complete.'; what.textContent = ''; return; }
        var d = new Date(n.date + 'T15:30:00Z');
        var day = d.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
        var local = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', timeZoneName: 'short' });
        when.textContent = day + ' · 15:30 UTC (' + local + ' your time)';
        what.textContent = '';
        var a = document.createElement('a'); a.href = n.url; a.target = '_blank'; a.rel = 'noopener noreferrer'; a.textContent = n.title; what.appendChild(a);
        var m = document.createElement('span'); m.className = 'muted small';
        m.textContent = ' ' + n.cite + ' · ' + n.feature_short; what.appendChild(m);
      });
    }).catch(function () {});
  }

  /* Register dialog, in two steps: email first (enough to get session emails), then optional
     details for people who plan to come regularly. The worker merges the second submission into
     the first, so skipping step two loses nothing. Opened by any [data-register] control or #register. */
  var triggers = document.querySelectorAll('[data-register]');
  if (!triggers.length) return;
  var HP = '<input class="hp" name="_hp" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">';
  var d = document.createElement('dialog');
  d.id = 'register'; d.className = 'register'; d.setAttribute('aria-labelledby', 'register-title');
  d.innerHTML =
    '<div class="register-head"><h2 id="register-title">Get session emails</h2><button type="button" class="close" data-close aria-label="Close">×</button></div>' +
    '<form class="step step-1" method="post" action="' + SIGNUP + '" novalidate>' +
      '<p class="small muted">The reading and prep notes before each session, and nothing else. Every email has an unsubscribe link.</p>' +
      '<label for="r-email">Email</label><input id="r-email" name="email" type="email" autocomplete="email" required maxlength="200" placeholder="you@example.com">' + HP +
      '<p class="form-status" aria-live="polite"></p>' +
      '<div class="register-actions"><button type="submit" class="btn">Get session emails</button></div>' +
    '</form>' +
    '<form class="step step-2" method="post" action="' + SIGNUP + '" hidden>' +
      '<p class="done">You’re on the list.</p>' +
      '<p class="small muted">Planning to come regularly? Add a few details so other members can find you. All optional.</p>' +
      '<label for="r-name">Name</label><input id="r-name" name="name" type="text" autocomplete="name" maxlength="100">' +
      '<label for="r-website">Website</label><input id="r-website" name="website" type="text" inputmode="url" autocomplete="url" placeholder="yoursite.com" maxlength="200">' +
      '<div class="pair"><div><label for="r-github">GitHub</label><input id="r-github" name="github" type="text" placeholder="username" maxlength="60" autocapitalize="off" spellcheck="false"></div>' +
      '<div><label for="r-discord">Discord</label><input id="r-discord" name="discord" type="text" placeholder="handle" maxlength="60" autocapitalize="off" spellcheck="false"></div></div>' +
      '<label for="r-affiliation">Affiliation</label><input id="r-affiliation" name="affiliation" type="text" autocomplete="organization" placeholder="Organization or project" maxlength="150">' + HP +
      '<p class="form-status" aria-live="polite"></p>' +
      '<div class="register-actions"><button type="submit" class="btn">Save details</button><button type="button" class="btn-quiet" data-close>Not now</button></div>' +
      '<p class="small muted">Sessions are recorded.</p>' +
    '</form>';
  document.body.appendChild(d);
  var f1 = d.querySelector('.step-1'), f2 = d.querySelector('.step-2'), title = d.querySelector('#register-title');
  var email = '';
  var banners = document.querySelectorAll('.register-status');
  function say(msg) { banners.forEach(function (b) { b.textContent = msg; }); }
  function step(n) {
    f1.hidden = n !== 1; f2.hidden = n !== 2;
    title.textContent = n === 1 ? 'Get session emails' : 'A little more, if you like';
    (n === 1 ? f1.querySelector('#r-email') : f2.querySelector('#r-name')).focus();
  }
  function open(e) {
    if (e) e.preventDefault();
    d.querySelectorAll('.form-status').forEach(function (s) { s.textContent = ''; });
    if (d.showModal) d.showModal(); else d.setAttribute('open', '');
    step(email ? 2 : 1);
  }
  function close() { if (d.close) d.close(); else d.removeAttribute('open'); }
  triggers.forEach(function (b) { b.addEventListener('click', open); });
  d.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', close); });
  // Close on a backdrop click only when the press and the release both land outside the dialog's box.
  // (Dragging to select text inside a field and releasing past its edge reports a click on the
  // dialog itself, which must not close it.)
  var downOnBackdrop = false;
  function outside(e) {
    var r = d.getBoundingClientRect();
    return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
  }
  d.addEventListener('pointerdown', function (e) { downOnBackdrop = e.target === d && outside(e); });
  d.addEventListener('click', function (e) {
    if (downOnBackdrop && e.target === d && outside(e)) close();
    downOnBackdrop = false;
  });
  d.addEventListener('close', function () { if (email) say('Thanks, you’re registered.'); });
  if (/[?&]signup=ok/.test(location.search)) say('Thanks, you’re registered.');
  if (/[?&]signup=error/.test(location.search)) say('That didn’t work. Please try again.');
  if (location.hash === '#register') open();

  function send(form, extra) {
    var st = form.querySelector('.form-status'), b = form.querySelector('button[type=submit]');
    var data = {}; new FormData(form).forEach(function (v, k) { data[k] = v; });
    for (var k in extra) data[k] = extra[k];
    data.source = location.pathname;
    b.disabled = true; st.textContent = 'Sending…';
    return fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); })
      .then(function (r) { if (!r.ok) throw new Error(r.error || 'That didn’t work.'); st.textContent = ''; return r; })
      .catch(function (err) { st.textContent = err.message || 'That didn’t work. Try again, or join us on Discord.'; throw err; })
      .finally(function () { b.disabled = false; });
  }
  f1.addEventListener('submit', function (e) {
    e.preventDefault();
    var input = f1.querySelector('#r-email'), st = f1.querySelector('.form-status');
    if (!input.value || !input.checkValidity()) { st.textContent = 'Please enter a valid email.'; input.focus(); return; }
    send(f1, {}).then(function () { email = input.value.trim(); say('Thanks, you\u2019re registered.'); step(2); }, function () {});
  });
  f2.addEventListener('submit', function (e) {
    e.preventDefault();
    send(f2, { email: email }).then(function () { close(); }, function () {});
  });
})();
