/* Shared behaviour for the site: the next-session card and the register dialog.
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
      for (var i = 0; i < S.length; i++) { if (Date.parse(S[i].end_utc) > now) { n = S[i]; break; } }
      cards.forEach(function (box) {
        var when = box.querySelector('.when'), what = box.querySelector('.what');
        if (!n) { when.textContent = 'The year is complete.'; what.textContent = ''; return; }
        // the reader's own time, with UTC beside it; both come from the schedule
        var d = new Date(n.start_utc), utc = n.start_utc.slice(11, 16) + ' UTC';
        var day = d.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
        var local = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', timeZoneName: 'short' });
        when.textContent = day + ' · ' + (d.getTimezoneOffset() === 0 ? utc : local + ' · ' + utc);
        what.textContent = '';
        var a = document.createElement('a'); a.href = n.url; a.target = '_blank'; a.rel = 'noopener noreferrer'; a.textContent = n.title; what.appendChild(a);
        var m = document.createElement('span'); m.className = 'muted small';
        m.textContent = ' ' + n.cite + ' · ' + n.feature_short; what.appendChild(m);
      });
    }).catch(function () {});
  }

  /* Blyg responses: verified Webmentions (stubs, quotes, forks from other blygs) listed under a post. */
  var resp = document.querySelector('[data-responses]');
  if (resp && window.fetch) {
    var VERB = { stub: 'responded to this', transclusion: 'quoted this', fork: 'forked this' };
    fetch(ROOT + 'blyg/webmention/responses?id=' + resp.getAttribute('data-responses'))
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (list) {
        if (!list.length) return;
        var ul = resp.querySelector('ul');
        list.forEach(function (m) {
          var li = document.createElement('li'), a = document.createElement('a');
          var host = ''; try { host = new URL(m.origin || m.page).host; } catch (e) {}
          a.href = m.page; a.textContent = (m.author || host) + ' ' + (VERB[m.relation] || 'mentioned this');
          li.appendChild(a);
          if (host) { var s = document.createElement('span'); s.className = 'muted small'; s.textContent = ' · ' + host; li.appendChild(s); }
          ul.appendChild(li);
        });
        resp.hidden = false;
      }).catch(function () {});
  }

  /* Short forms that go to the group's Discord channel: offer a talk ([data-talk]) and request advisory
     services ([data-advisory]). Both reuse the register dialog's look; the worker posts them and stores nothing. */
  var BASE = SIGNUP.replace(/\/signup$/, '');
  function field(id, label, input, optional) {
    return '<label for="' + id + '">' + label + (optional ? ' <span class="req">optional</span>' : '') + '</label>' + input;
  }
  function inquiry(cfg) {
    var btns = document.querySelectorAll('[' + cfg.trigger + ']');
    if (!btns.length) return;
    var dlg = document.createElement('dialog');
    dlg.id = cfg.id; dlg.className = 'register'; dlg.setAttribute('aria-labelledby', cfg.id + '-title');
    dlg.innerHTML =
      '<div class="register-head"><h2 id="' + cfg.id + '-title">' + cfg.title + '</h2><button type="button" class="close" data-x aria-label="Close">×</button></div>' +
      '<form method="post" action="' + BASE + cfg.route + '"><p class="small muted">' + cfg.intro + '</p>' + cfg.fields +
      '<input class="hp" name="_hp" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      '<p class="form-status" aria-live="polite"></p>' +
      '<div class="register-actions"><button type="submit" class="btn">' + cfg.submit + '</button><button type="button" class="btn-quiet" data-x>Cancel</button></div></form>';
    document.body.appendChild(dlg);
    var form = dlg.querySelector('form'), status = dlg.querySelector('.form-status');
    var open = function (e) { if (e) e.preventDefault(); status.textContent = ''; if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', ''); dlg.querySelector('input, textarea').focus(); };
    var close = function () { if (dlg.close) dlg.close(); else dlg.removeAttribute('open'); };
    btns.forEach(function (b) { b.addEventListener('click', open); });
    dlg.querySelectorAll('[data-x]').forEach(function (b) { b.addEventListener('click', close); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) close(); });
    form.addEventListener('submit', function (e) {
      if (!window.fetch) return;   // no-JS fallback: the form posts and the worker redirects back
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = {}; new FormData(form).forEach(function (v, k) { data[k] = v; });
      var btn = form.querySelector('[type=submit]'); btn.disabled = true; status.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (x) {
          btn.disabled = false;
          if (!x.ok) { status.textContent = x.j.error || 'Something went wrong. Message @rafa_0x on Discord.'; return; }
          form.reset(); status.textContent = cfg.thanks;
        })
        .catch(function () { btn.disabled = false; status.textContent = 'Could not send. Message @rafa_0x on Discord.'; });
    });
    if (new RegExp('[?&]' + cfg.id + '=ok').test(location.search)) { open(); status.textContent = cfg.thanks; }
  }
  inquiry({
    trigger: 'data-talk', id: 'talk', route: '/talk', title: 'Offer a talk', submit: 'Send offer',
    intro: 'Guests speak first, at the start of a session. What you send here, including how to reach you, is posted to the group’s Discord channel so we can reply. Sessions are recorded.',
    fields: field('t-name', 'Name', '<input id="t-name" name="name" type="text" autocomplete="name" required maxlength="100">') +
      field('t-contact', 'Discord handle or email', '<input id="t-contact" name="contact" type="text" required maxlength="150" autocapitalize="off" spellcheck="false">') +
      field('t-title', 'Talk title', '<input id="t-title" name="title" type="text" required maxlength="200">') +
      field('t-theme', 'Closest theme', '<select id="t-theme" name="theme"><option>Agents</option><option>Nature</option><option>Emissions</option><option>Incidents</option><option>Hardness</option><option>Liveness</option><option selected>Not sure</option></select>') +
      field('t-about', 'A few lines about it', '<textarea id="t-about" name="about" rows="3" maxlength="1200"></textarea>', true) +
      field('t-link', 'Link to your work', '<input id="t-link" name="link" type="text" inputmode="url" placeholder="paper, site or repo" maxlength="300">', true) +
      field('t-when', 'Preferred month', '<input id="t-when" name="when" type="text" placeholder="e.g. March 2027" maxlength="80">', true),
    thanks: 'Thanks! Your offer is in the group’s Discord channel. We’ll reply there or by email.'
  });
  inquiry({
    trigger: 'data-advisory', id: 'advisory', route: '/advisory', title: 'Request advisory services', submit: 'Send request',
    intro: 'Tell us what you’re working on and where you’d like help. Your request, including how to reach you, is posted to the group’s Discord channel so the facilitators can reply.',
    fields: field('a-name', 'Name', '<input id="a-name" name="name" type="text" autocomplete="name" required maxlength="100">') +
      field('a-contact', 'Email or Discord handle', '<input id="a-contact" name="contact" type="text" autocomplete="email" required maxlength="150" autocapitalize="off" spellcheck="false">') +
      field('a-org', 'Organization', '<input id="a-org" name="org" type="text" autocomplete="organization" maxlength="150">', true) +
      field('a-need', 'What would you like help with?', '<textarea id="a-need" name="need" rows="4" required maxlength="1500" placeholder="For example: where agents should sit in a process, which protocols to harden, or how to log what they do"></textarea>') +
      field('a-when', 'Timing', '<input id="a-when" name="when" type="text" placeholder="e.g. this quarter" maxlength="80">', true),
    thanks: 'Thanks! Your request is in the group’s Discord channel. We’ll get back to you.'
  });
  inquiry({
    trigger: 'data-listing', id: 'listing', route: '/listing', title: 'Add your blyg', submit: 'Send request',
    intro: 'Members who write a blyg can be listed in the community here and in our blogroll. We check that the address serves a blyg, then post your request, including how to reach you, to the group’s Discord channel.',
    fields: field('l-name', 'Name', '<input id="l-name" name="name" type="text" autocomplete="name" required maxlength="100">') +
      field('l-contact', 'Discord handle or email', '<input id="l-contact" name="contact" type="text" required maxlength="150" autocapitalize="off" spellcheck="false">') +
      field('l-link', 'Your blyg’s address', '<input id="l-link" name="link" type="text" inputmode="url" required placeholder="https://example.com/blyg/" maxlength="300" autocapitalize="off" spellcheck="false">') +
      field('l-note', 'Anything we should know', '<textarea id="l-note" name="note" rows="2" maxlength="600"></textarea>', true),
    thanks: 'Thanks! Your request is in the group’s Discord channel. Your blyg will appear here once it’s added.'
  });

  /* Unsubscribe page: removes the address, and says the same thing whether or not it was on the list. */
  var unsub = document.querySelector('form[data-unsub]');
  if (unsub) {
    unsub.action = BASE + '/unsubscribe';
    var us = unsub.querySelector('.form-status'), DONE = 'Done. If that address was on the list, it’s off now, and you won’t get session emails.';
    if (/[?&]done=1/.test(location.search)) us.textContent = DONE;
    unsub.addEventListener('submit', function (e) {
      if (!window.fetch) return;
      e.preventDefault();
      if (!unsub.reportValidity()) return;
      var data = {}; new FormData(unsub).forEach(function (v, k) { data[k] = v; });
      var btn = unsub.querySelector('[type=submit]'); btn.disabled = true; us.textContent = 'One moment…';
      fetch(unsub.action, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (x) { btn.disabled = false; us.textContent = x.ok ? DONE : (x.j.error || 'Something went wrong. Message @rafa_0x on Discord.'); if (x.ok) unsub.reset(); })
        .catch(function () { btn.disabled = false; us.textContent = 'Could not reach the server. Try again, or message @rafa_0x on Discord.'; });
    });
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

/* Image viewer: any image in the page content opens larger on click (or Enter/Space when focused).
   The viewer can show it at full size, download it, or copy it to the clipboard as a PNG. Esc closes. */
(function () {
  var imgs = Array.prototype.filter.call(document.querySelectorAll('main img'), function (img) {
    /* skip links, the logo, and decorative art that sits behind controls (the next-session card) */
    return !img.closest('a') && !img.classList.contains('logo') && !img.classList.contains('mark') && !img.classList.contains('fig-next');
  });
  if (!imgs.length || typeof HTMLDialogElement === 'undefined') return;

  var dlg = document.createElement('dialog');
  dlg.className = 'lightbox';
  dlg.setAttribute('aria-label', 'Image, enlarged');
  dlg.innerHTML =
    '<div class="lb-bar">' +
      '<a class="lb-open" target="_blank" rel="noopener">Open full size</a>' +
      '<a class="lb-download" download>Download</a>' +
      '<button type="button" class="lb-copy">Copy image</button>' +
      '<span class="lb-status" role="status"></span>' +
      '<button type="button" class="lb-close" aria-label="Close">Close ✕</button>' +
    '</div>' +
    '<div class="lb-stage"><img alt=""></div>' +
    '<p class="lb-caption"></p>';
  document.body.appendChild(dlg);
  var big = dlg.querySelector('.lb-stage img'), cap = dlg.querySelector('.lb-caption'), status = dlg.querySelector('.lb-status');
  var current = null;

  function open(img) {
    current = img;
    var src = img.currentSrc || img.src;
    big.src = src; big.alt = img.alt || '';
    big.classList.remove('lb-zoomed');
    cap.textContent = img.alt || '';
    cap.hidden = !img.alt;
    dlg.querySelector('.lb-open').href = src;
    var dl = dlg.querySelector('.lb-download');
    dl.href = src; dl.setAttribute('download', src.split('/').pop().split('?')[0]);
    status.textContent = '';
    dlg.showModal();
  }

  imgs.forEach(function (img) {
    img.classList.add('zoomable');
    img.tabIndex = 0;
    img.setAttribute('role', 'button');
    img.setAttribute('aria-label', 'Enlarge image' + (img.alt ? ': ' + img.alt : ''));
    img.addEventListener('click', function () { open(img); });
    img.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(img); }
    });
  });

  /* Click the image to switch between fitting the screen and its full drawn size. */
  big.addEventListener('click', function () { big.classList.toggle('lb-zoomed'); });
  dlg.querySelector('.lb-close').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg || e.target.classList.contains('lb-stage')) dlg.close(); });
  dlg.addEventListener('close', function () { if (current) current.focus(); });

  /* Copy as PNG: draw the image on a canvas at twice its size (SVGs stay sharp), then write it to the clipboard. */
  function png() {
    return new Promise(function (resolve, reject) {
      var im = new Image();
      im.onload = function () {
        var w = (im.naturalWidth || 1200) * 2, h = (im.naturalHeight || 600) * 2;
        var c = document.createElement('canvas'); c.width = w; c.height = h;
        var ctx = c.getContext('2d');
        ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, w, h);
        ctx.drawImage(im, 0, 0, w, h);
        c.toBlob(function (b) { b ? resolve(b) : reject(new Error('no image')); }, 'image/png');
      };
      im.onerror = reject;
      im.src = big.src;
    });
  }
  dlg.querySelector('.lb-copy').addEventListener('click', function () {
    if (!navigator.clipboard || typeof ClipboardItem === 'undefined') {
      status.textContent = 'Copying isn’t supported in this browser. Use Download.'; return;
    }
    status.textContent = 'Copying…';
    navigator.clipboard.write([new ClipboardItem({ 'image/png': png() })])
      .then(function () { status.textContent = 'Copied.'; },
            function () { status.textContent = 'Couldn’t copy. Use Download instead.'; });
  });
})();
