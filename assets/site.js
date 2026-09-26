/* Shared behaviour for the SIG site: the next-session card and the register dialog.
   Loaded with <script src="…/assets/site.js" data-root="…/" defer>. No dependencies. */
(function () {
  var script = document.currentScript || document.querySelector('script[data-root]');
  var ROOT = (script && script.getAttribute('data-root')) || './';
  var SIGNUP = 'https://sig-p4b-signup.rafaeldf2.workers.dev/signup';

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
        var a = document.createElement('a'); a.href = n.url; a.textContent = n.title; what.appendChild(a);
        var m = document.createElement('span'); m.className = 'muted small';
        m.textContent = ' ' + n.cite + ' · ' + n.feature_short; what.appendChild(m);
      });
    }).catch(function () {});
  }

  /* Register dialog: built once, opened by any [data-register] control or #register. */
  var triggers = document.querySelectorAll('[data-register]');
  if (!triggers.length) return;
  var d = document.createElement('dialog');
  d.id = 'register'; d.className = 'register'; d.setAttribute('aria-labelledby', 'register-title');
  d.innerHTML =
    '<form method="post" action="' + SIGNUP + '">' +
    '<div class="register-head"><h2 id="register-title">Register for the SIG</h2><button type="button" class="close" data-close aria-label="Close">×</button></div>' +
    '<p class="small muted">We send the reading and prep notes before each session. Only the email is required.</p>' +
    '<label for="r-name">Name</label><input id="r-name" name="name" type="text" autocomplete="name" maxlength="100">' +
    '<label for="r-email">Email <span class="req">required</span></label><input id="r-email" name="email" type="email" autocomplete="email" required maxlength="200">' +
    '<label for="r-website">Website</label><input id="r-website" name="website" type="text" inputmode="url" autocomplete="url" placeholder="yoursite.com" maxlength="200">' +
    '<div class="pair"><div><label for="r-github">GitHub</label><input id="r-github" name="github" type="text" placeholder="username" maxlength="60" autocapitalize="off" spellcheck="false"></div>' +
    '<div><label for="r-discord">Discord</label><input id="r-discord" name="discord" type="text" placeholder="handle" maxlength="60" autocapitalize="off" spellcheck="false"></div></div>' +
    '<label for="r-affiliation">Affiliation</label><input id="r-affiliation" name="affiliation" type="text" autocomplete="organization" placeholder="Organization or project" maxlength="150">' +
    '<input class="hp" name="_hp" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">' +
    '<p class="form-status" aria-live="polite"></p>' +
    '<div class="register-actions"><button type="submit" class="btn">Register</button><button type="button" class="btn-quiet" data-close>Cancel</button></div>' +
    '<p class="small muted">Sessions are recorded. Each email includes a link to unsubscribe.</p>' +
    '</form>';
  document.body.appendChild(d);
  var f = d.querySelector('form'), st = f.querySelector('.form-status');
  var banners = document.querySelectorAll('.register-status');
  function say(msg) { banners.forEach(function (b) { b.textContent = msg; }); }
  function open(e) { if (e) e.preventDefault(); st.textContent = ''; if (d.showModal) d.showModal(); else d.setAttribute('open', ''); f.querySelector('#r-name').focus(); }
  function close() { if (d.close) d.close(); else d.removeAttribute('open'); }
  triggers.forEach(function (b) { b.addEventListener('click', open); });
  d.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', close); });
  d.addEventListener('click', function (e) { if (e.target === d) close(); });
  if (/[?&]signup=ok/.test(location.search)) say('Thanks, you’re registered.');
  if (/[?&]signup=error/.test(location.search)) say('That didn’t work. Please try again.');
  if (location.hash === '#register') open();
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var b = f.querySelector('button[type=submit]'); b.disabled = true; st.textContent = 'Sending…';
    var data = {}; new FormData(f).forEach(function (v, k) { data[k] = v; }); data.source = location.pathname;
    fetch(f.action, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); })
      .then(function (r) {
        if (r.ok) { f.reset(); close(); say('Thanks, you’re registered.'); }
        else { st.textContent = r.error || 'That didn’t work.'; }
      })
      .catch(function () { st.textContent = 'That didn’t work. Try again, or join us on Discord.'; })
      .finally(function () { b.disabled = false; });
  });
})();
