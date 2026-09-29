/* HYPE MODE: ticker, trailer, swarm hero, countdown, live scenes, FOMO. Layered on the quiet site.
   Real facts are sourced from the reading plan; the joke numbers say they are made up. */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = (document.currentScript && document.currentScript.dataset.root) || './';
  var KICKOFF = Date.parse('2026-11-02T15:30:00Z');
  var main = document.querySelector('main');
  var h1 = main && main.querySelector('h1');
  var isHome = h1 && h1.textContent.trim() === 'Protocols for Business';
  var TAU = Math.PI * 2, rnd = Math.random;
  function $(html) { var t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstChild; }
  function store(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function register() { var b = document.querySelector('.next [data-register], [data-register]'); if (b) b.click(); confetti(); }

  /* ---------- ticker ---------- */
  var TICK = ['⚠️ Your competitor’s agents are reading this page right now', '🔥 No homework. We read in the room', '🚨 100,000 agents. Zero supervisors. What could go wrong?',
    '📈 Protocols are the new org chart', '🧱 Hard core. Free edges. No excuses', '⏳ Kickoff 2 November. The swarm does not wait', '💀 Every incident report started as an unexamined protocol',
    '🫀 A dead protocol is just a PDF', '🐦 Starlings solved coordination 10 million years ago. Catch up', '👀 Seen a protocol today? Neither has your board'];
  var s = TICK.join('   ✦   ') + '   ✦   ';
  var ticker = $('<div class="hype-ticker" aria-hidden="true"><span>' + s + s + '</span></div>');
  var header = document.querySelector('body > header');
  header.after(ticker);

  /* ---------- tab-title bait ---------- */
  var baseTitle = document.title;
  document.addEventListener('visibilitychange', function () { document.title = document.hidden ? '(1) 🚨 Your agents miss you' : baseTitle; });

  /* ---------- confetti ---------- */
  function confetti() {
    if (reduced) return;
    var cols = ['#ff2bd6', '#c6ff00', '#00e5ff', '#ffd400', '#ff3b30', '#fff'];
    for (var i = 0; i < 140; i++) {
      var c = document.createElement('i'); c.className = 'confetti';
      c.style.left = rnd() * 100 + 'vw'; c.style.background = cols[i % cols.length];
      c.style.animationDuration = 1.8 + rnd() * 2.2 + 's'; c.style.animationDelay = rnd() * .4 + 's';
      c.style.transform = 'rotate(' + rnd() * 360 + 'deg)';
      document.body.appendChild(c); setTimeout(c.remove.bind(c), 5000);
    }
  }
  document.querySelectorAll('[data-register]').forEach(function (b) { b.addEventListener('click', confetti); });

  /* ---------- "live" toasts: agents only, so nobody is being faked ---------- */
  var TOASTS = ['An agent in us-east-1 just read the syllabus', 'A swarm of 4,096 agents is comparing your protocols to a competitor’s', 'Someone’s agent just turned a package manager into a message board',
    'An agent in eu-west-2 added “protocol vision” to its system prompt', '3 agents are viewing the Engineering Hardness theme', 'An agent just skipped reading the incident report. Bold.'];
  var toast = $('<div role="status" style="position:fixed;left:1rem;bottom:1rem;z-index:150;max-width:22rem;padding:.8rem 1rem;border-radius:14px;background:#120f1c;border:1px solid #2a2540;box-shadow:0 10px 40px rgba(0,0,0,.5);font-size:.9rem;transform:translateY(160%);transition:transform .4s"></div>');
  document.body.appendChild(toast);
  var ti = 0;
  setInterval(function () {
    toast.innerHTML = '<b style="color:#c6ff00">● LIVE</b> ' + TOASTS[ti++ % TOASTS.length] + '<br><span style="color:#a9a3c4;font-size:.78rem">' + (2 + Math.floor(rnd() * 50)) + ' seconds ago · agents only, no humans were faked</span>';
    toast.style.transform = 'translateY(0)';
    setTimeout(function () { toast.style.transform = 'translateY(160%)'; }, 4200);
  }, 9000);

  /* ---------- exit intent ---------- */
  var popped = false;
  document.addEventListener('mouseout', function (e) {
    if (popped || e.relatedTarget || e.clientY > 8) return;
    popped = true;
    var pop = $('<div class="hype-pop" role="dialog" aria-modal="true" aria-label="Wait"><div class="box"><h3>WAIT ✋</h3><p>Leaving now is a <b>single point of failure.</b></p><p>Register in ten seconds. Unsubscribe any time. Your future postmortem will thank you.</p><p style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem"><button class="hype-cta" data-yes>Fine, I’m in 🔥</button><button class="hype-cta ghost" data-no>No thanks, I enjoy incidents</button></p></div></div>');
    document.body.appendChild(pop);
    pop.querySelector('[data-yes]').onclick = function () { pop.remove(); register(); };
    pop.querySelector('[data-no]').onclick = function () { pop.remove(); };
    pop.addEventListener('click', function (ev) { if (ev.target === pop) pop.remove(); });
  });

  /* ---------- canvas helpers and one shared animation loop ---------- */
  var scenes = [];
  function fit(cv) {
    var r = cv.getBoundingClientRect(), d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = Math.max(1, r.width * d); cv.height = Math.max(1, r.height * d);
    var c = cv.getContext('2d'); c.setTransform(d, 0, 0, d, 0, 0); return { c: c, w: r.width, h: r.height };
  }
  function addScene(cv, make) {
    var sc = { cv: cv, visible: true, make: make, st: null };
    sc.reset = function () { var f = fit(cv); sc.c = f.c; sc.w = f.w; sc.h = f.h; sc.st = make(sc); };
    sc.reset(); scenes.push(sc);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { sc.visible = es[0].isIntersecting; }).observe(cv);
    return sc;
  }
  window.addEventListener('resize', function () { scenes.forEach(function (s) { s.reset(); }); });
  var t0 = performance.now();
  function loop(now) {
    var t = (now - t0) / 1000;
    scenes.forEach(function (s) { if (s.w < 2) s.reset(); if (s.visible) s.st.draw(t); });
    if (!reduced) requestAnimationFrame(loop);
  }

  /* boids: the swarm */
  function swarm(opts) {
    return function (sc) {
      var n = opts.n, B = [], mouse = { x: -999, y: -999 };
      for (var i = 0; i < n; i++) B.push({ x: rnd() * sc.w, y: rnd() * sc.h, vx: rnd() * 2 - 1, vy: rnd() * 2 - 1, k: i % opts.cols.length });
      if (opts.mouse) {
        sc.cv.parentNode.addEventListener('pointermove', function (e) { var r = sc.cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
        sc.cv.parentNode.addEventListener('pointerleave', function () { mouse.x = mouse.y = -999; });
      }
      return { draw: function () {
        var c = sc.c;
        if (opts.sky) { var g = c.createLinearGradient(0, 0, 0, sc.h); g.addColorStop(0, opts.sky[0]); g.addColorStop(1, opts.sky[1]); c.fillStyle = g; c.globalAlpha = .35; c.fillRect(0, 0, sc.w, sc.h); c.globalAlpha = 1; }
        else { c.fillStyle = 'rgba(7,6,11,.22)'; c.fillRect(0, 0, sc.w, sc.h); }
        for (var i = 0; i < n; i++) {
          var b = B[i], ax = 0, ay = 0, cx = 0, cy = 0, sx = 0, sy = 0, m = 0;
          for (var j = 0; j < n; j += 3) {   // sample a third of the flock: cheap and still lifelike
            var o = B[j]; if (o === b) continue;
            var dx = o.x - b.x, dy = o.y - b.y, d2 = dx * dx + dy * dy;
            if (d2 < 3600) { m++; ax += o.vx; ay += o.vy; cx += o.x; cy += o.y; if (d2 < 256) { sx -= dx; sy -= dy; } }
          }
          if (m) { b.vx += (ax / m - b.vx) * .05 + (cx / m - b.x) * .0008 + sx * .03; b.vy += (ay / m - b.vy) * .05 + (cy / m - b.y) * .0008 + sy * .03; }
          var mx = b.x - mouse.x, my = b.y - mouse.y, md = mx * mx + my * my;
          if (md < 14000) { b.vx += mx / Math.sqrt(md) * .6; b.vy += my / Math.sqrt(md) * .6; }
          var sp = Math.hypot(b.vx, b.vy), max = opts.speed;
          if (sp > max) { b.vx *= max / sp; b.vy *= max / sp; } if (sp < max * .4) { b.vx *= 1.1; b.vy *= 1.1; }
          b.x += b.vx; b.y += b.vy;
          if (b.x < -10) b.x = sc.w + 10; if (b.x > sc.w + 10) b.x = -10; if (b.y < -10) b.y = sc.h + 10; if (b.y > sc.h + 10) b.y = -10;
          c.strokeStyle = opts.cols[b.k]; c.lineWidth = opts.lw;
          c.beginPath(); c.moveTo(b.x, b.y); c.lineTo(b.x - b.vx * opts.tail, b.y - b.vy * opts.tail); c.stroke();
        }
      } };
    };
  }
  /* protocol network: packets along edges */
  function network(sc) {
    var N = [], E = [], P = [];
    for (var i = 0; i < 16; i++) N.push({ x: 20 + rnd() * (sc.w - 40), y: 20 + rnd() * (sc.h - 40), glow: 0 });
    N.forEach(function (a, i) {
      N.map(function (b, j) { return [Math.hypot(a.x - b.x, a.y - b.y), j]; }).sort(function (p, q) { return p[0] - q[0]; }).slice(1, 4)
        .forEach(function (p) { if (p[1] > i) E.push([i, p[1]]); });
    });
    return { draw: function (t) {
      var c = sc.c; c.fillStyle = 'rgba(0,0,0,.35)'; c.fillRect(0, 0, sc.w, sc.h);
      if (rnd() < .25 && E.length) { var e = E[Math.floor(rnd() * E.length)]; P.push({ e: rnd() < .5 ? e : [e[1], e[0]], p: 0 }); }
      c.strokeStyle = 'rgba(0,229,255,.25)'; c.lineWidth = 1;
      E.forEach(function (e) { c.beginPath(); c.moveTo(N[e[0]].x, N[e[0]].y); c.lineTo(N[e[1]].x, N[e[1]].y); c.stroke(); });
      P = P.filter(function (p) {
        p.p += .03; var a = N[p.e[0]], b = N[p.e[1]];
        if (p.p >= 1) { b.glow = 1; return false; }
        c.fillStyle = '#ff2bd6'; c.beginPath(); c.arc(a.x + (b.x - a.x) * p.p, a.y + (b.y - a.y) * p.p, 2.5, 0, TAU); c.fill(); return true;
      });
      N.forEach(function (n) { n.glow *= .93; c.fillStyle = 'rgba(198,255,0,' + (.35 + n.glow * .65) + ')'; c.beginPath(); c.arc(n.x, n.y, 4 + n.glow * 5, 0, TAU); c.fill(); });
    } };
  }
  /* emissions: rings that light up whoever reads them */
  function emissions(sc) {
    var N = [], R = [];
    for (var i = 0; i < 34; i++) N.push({ x: rnd() * sc.w, y: rnd() * sc.h, lit: 0 });
    return { draw: function (t) {
      var c = sc.c; c.fillStyle = 'rgba(0,0,0,.3)'; c.fillRect(0, 0, sc.w, sc.h);
      if (rnd() < .07) { var s = N[Math.floor(rnd() * N.length)]; R.push({ x: s.x, y: s.y, r: 0 }); }
      R = R.filter(function (r) {
        r.r += 1.6; c.strokeStyle = 'rgba(255,212,0,' + Math.max(0, 1 - r.r / 180) + ')'; c.lineWidth = 2;
        c.beginPath(); c.arc(r.x, r.y, r.r, 0, TAU); c.stroke();
        N.forEach(function (n) { if (Math.abs(Math.hypot(n.x - r.x, n.y - r.y) - r.r) < 2) n.lit = 1; });
        return r.r < 180;
      });
      N.forEach(function (n) { n.lit *= .95; c.fillStyle = n.lit > .1 ? 'rgba(255,212,0,' + n.lit + ')' : '#333'; c.fillRect(n.x - 3, n.y - 3, 6, 6); });
    } };
  }
  /* incidents: all systems normal, until a crack runs through them */
  function incidents(sc) {
    var tips, segs, flash, hold;
    function start() { tips = [{ x: sc.w * (.25 + rnd() * .5), y: 0, a: Math.PI / 2 }]; segs = []; flash = 0; hold = 0; }
    start();
    return { draw: function () {
      var c = sc.c, w = sc.w, h = sc.h;
      c.fillStyle = '#0a0304'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(255,255,255,.06)'; c.lineWidth = 1;   // the systems: a quiet grid of boxes
      for (var gx = 12; gx < w; gx += 34) for (var gy = 12; gy < h; gy += 34) c.strokeRect(gx, gy, 24, 24);
      var next = [];
      tips.forEach(function (p) {
        var a = p.a + (rnd() - .5) * .9, x = p.x + Math.cos(a) * 5, y = p.y + Math.sin(a) * 5;
        segs.push([p.x, p.y, x, y]);
        if (y < h && x > 0 && x < w) { next.push({ x: x, y: y, a: a * .7 + Math.PI / 2 * .3 }); if (rnd() < .05 && tips.length < 16) next.push({ x: x, y: y, a: a + (rnd() < .5 ? -.9 : .9) }); }
      });
      tips = next;
      c.strokeStyle = '#ff3b30'; c.lineWidth = 2; c.shadowColor = '#ff3b30'; c.shadowBlur = 10;
      c.beginPath(); segs.forEach(function (q) { c.moveTo(q[0], q[1]); c.lineTo(q[2], q[3]); }); c.stroke(); c.shadowBlur = 0;
      c.font = '700 13px "Space Grotesk"'; c.textAlign = 'left';
      if (tips.length) { c.fillStyle = '#34c759'; c.fillText('● ALL SYSTEMS NORMAL', 12, h - 12); }
      else {
        if (!hold) flash = 1; hold++;
        c.fillStyle = 'rgba(255,59,48,' + flash * .7 + ')'; c.fillRect(0, 0, w, h); flash *= .9;
        c.fillStyle = hold % 20 < 12 ? '#ff3b30' : '#fff'; c.font = '28px Anton, Impact'; c.textAlign = 'center'; c.fillText('INCIDENT', w / 2, h / 2 + 10);
        if (hold > 90) start();
      }
    } };
  }
  /* hardness: a rigid core, free agents bouncing off it */
  function hardness(sc) {
    var P = [], R = Math.min(sc.w, sc.h) * .26;
    for (var i = 0; i < 90; i++) { var a = rnd() * TAU, d = R + 10 + rnd() * 80; P.push({ x: sc.w / 2 + Math.cos(a) * d, y: sc.h / 2 + Math.sin(a) * d, vx: rnd() * 3 - 1.5, vy: rnd() * 3 - 1.5, hit: 0 }); }
    return { draw: function (t) {
      var c = sc.c, cx = sc.w / 2, cy = sc.h / 2; c.fillStyle = 'rgba(0,0,0,.3)'; c.fillRect(0, 0, sc.w, sc.h);
      c.save(); c.translate(cx, cy); c.rotate(t * .2);
      for (var k = 3; k >= 1; k--) {
        c.strokeStyle = 'rgba(198,255,0,' + (.25 * k) + ')'; c.lineWidth = k === 1 ? 3 : 1; c.beginPath();
        for (var i = 0; i <= 6; i++) { var a = i / 6 * TAU, r = R * (k === 1 ? 1 : 1 - k * .18); c[i ? 'lineTo' : 'moveTo'](Math.cos(a) * r, Math.sin(a) * r); }
        c.stroke();
      }
      c.restore();
      c.fillStyle = '#c6ff00'; c.font = '700 13px "Space Grotesk"'; c.textAlign = 'center'; c.fillText('HARD CORE', cx, cy + 5);
      P.forEach(function (p) {
        p.x += p.vx; p.y += p.vy;
        var dx = p.x - cx, dy = p.y - cy, d = Math.hypot(dx, dy);
        if (d < R + 3) { var nx = dx / d, ny = dy / d, dot = p.vx * nx + p.vy * ny; p.vx -= 2 * dot * nx; p.vy -= 2 * dot * ny; p.x = cx + nx * (R + 4); p.y = cy + ny * (R + 4); p.hit = 1; }
        if (p.x < 0 || p.x > sc.w) p.vx *= -1; if (p.y < 0 || p.y > sc.h) p.vy *= -1;
        p.hit *= .9; c.fillStyle = p.hit > .1 ? '#fff' : '#ff2bd6'; c.beginPath(); c.arc(p.x, p.y, 2 + p.hit * 3, 0, TAU); c.fill();
      });
    } };
  }
  /* liveness: the heartbeat */
  function liveness(sc) {
    var pts = [], x = 0, beatAt = 0;
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h, y = h / 2 + 10, ph = (t * 1.25) % 1;
      if (ph > .1 && ph < .13) y -= 70; else if (ph >= .13 && ph < .16) y += 45; else if (ph >= .16 && ph < .19) y -= 18; else y += Math.sin(t * 9) * 1.5;
      pts.push([x, y]); x += 2.4; if (x > w) { x = 0; pts = []; }
      c.fillStyle = '#000'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(198,255,0,.08)'; c.lineWidth = 1;
      for (var gx = 0; gx < w; gx += 20) { c.beginPath(); c.moveTo(gx, 0); c.lineTo(gx, h); c.stroke(); }
      for (var gy = 0; gy < h; gy += 20) { c.beginPath(); c.moveTo(0, gy); c.lineTo(w, gy); c.stroke(); }
      c.strokeStyle = '#c6ff00'; c.lineWidth = 2.5; c.shadowColor = '#c6ff00'; c.shadowBlur = 12; c.beginPath();
      pts.forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); }); c.stroke(); c.shadowBlur = 0;
      if (pts.length) { var e = pts[pts.length - 1]; c.fillStyle = '#fff'; c.beginPath(); c.arc(e[0], e[1], 3.5, 0, TAU); c.fill(); }
      var beat = ph < .25 ? 1 - ph * 4 : 0;
      c.fillStyle = 'rgba(255,59,48,' + (.45 + beat * .55) + ')'; c.font = '700 15px "Space Grotesk"'; c.textAlign = 'left'; c.fillText('♥ 75 BPM · ALIVE', 12, h - 12);
    } };
  }
  /* growth: agents explode, protocols flatline, the gap is where incidents live */
  function growth(sc) {
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h, p = Math.min(1, (t % 9) / 6);
      c.fillStyle = '#0b0913'; c.fillRect(0, 0, w, h);
      c.strokeStyle = '#1e1a2c'; c.lineWidth = 1;
      for (var g = 1; g < 5; g++) { c.beginPath(); c.moveTo(0, h * g / 5); c.lineTo(w, h * g / 5); c.stroke(); }
      var A = [], Pr = [];
      for (var i = 0; i <= 100 * p; i++) { var u = i / 100, x = 20 + u * (w - 40); A.push([x, h - 24 - (h - 60) * (Math.exp(u * 4.2) - 1) / (Math.exp(4.2) - 1)]); Pr.push([x, h - 24 - (h - 60) * u * .12]); }
      if (A.length > 1) {
        c.fillStyle = 'rgba(255,59,48,.18)'; c.beginPath(); A.forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); });
        for (var j = Pr.length - 1; j >= 0; j--) c.lineTo(Pr[j][0], Pr[j][1]); c.fill();
        [[A, '#ff2bd6'], [Pr, '#00e5ff']].forEach(function (L) { c.strokeStyle = L[1]; c.lineWidth = 3; c.beginPath(); L[0].forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); }); c.stroke(); });
        var e = A[A.length - 1], f = Pr[Pr.length - 1];
        c.font = '700 13px "Space Grotesk"'; c.textAlign = 'right';
        c.fillStyle = '#ff2bd6'; c.fillText('AGENTS DEPLOYED', e[0] - 6, e[1] - 8);
        c.fillStyle = '#00e5ff'; c.fillText('PROTOCOLS ANYONE CAN SEE', f[0] - 6, f[1] - 8);
        if (p > .6) { c.fillStyle = '#ff3b30'; c.textAlign = 'center'; c.font = '700 18px Anton, Impact'; c.fillText('THE INCIDENT ZONE', w * .72, (A[Math.floor(A.length * .8)][1] + Pr[Math.floor(Pr.length * .8)][1]) / 2 + 30); }
      }
    } };
  }

  /* ---------- home page ---------- */
  if (isHome) {
    var lede = main.querySelector('.lede');
    h1.hidden = true; if (lede) lede.hidden = true;
    var hero = $('<section class="hype-full hype-hero" aria-label="Protocols for Business"><canvas aria-hidden="true"></canvas><div class="inner">' +
      '<span class="hype-kicker">⚠️ Warning: your agents are already coordinating without you</span>' +
      '<h1 class="glitch" data-text="PROTOCOLS FOR BUSINESS">PROTOCOLS FOR BUSINESS</h1>' +
      '<p class="hype-sub">Your competitors are deploying <em>100,000 agents</em>. Nobody is watching them. <em>We are.</em> The only reading group that sees the protocols <em>before</em> the incident report does.</p>' +
      '<div class="countdown" aria-label="Time until kickoff"><div><b data-d>00</b><span>days</span></div><div><b data-h>00</b><span>hours</span></div><div><b data-m>00</b><span>min</span></div><div><b data-s>00</b><span>sec</span></div></div>' +
      '<p class="countdown-note">until kickoff · after that you’re watching the recording like everyone else</p>' +
      '<div class="hype-actions"><button class="hype-cta" data-go>🔥 Claim your seat</button><button class="hype-cta ghost" data-trailer>▶ Watch the trailer</button></div>' +
      '<p class="fine" style="margin-top:1rem">👀 <b data-viewers>1,284</b> agents are viewing this page</p></div>' +
      '<span class="sticker" style="top:14%;left:6%;background:#c6ff00;--r:-8deg;transform:rotate(-8deg)">No homework 📚❌</span>' +
      '<span class="sticker" style="top:22%;right:7%;background:#ffd400;--r:6deg;transform:rotate(6deg)">26 Mondays 📅</span>' +
      '<span class="sticker" style="bottom:14%;left:9%;background:#00e5ff;--r:4deg;transform:rotate(4deg)">Drop-ins welcome 🚪</span></section>');
    main.prepend(hero);
    addScene(hero.querySelector('canvas'), swarm({ n: 260, cols: ['#ff2bd6', '#00e5ff', '#c6ff00'], speed: 2.6, tail: 4, lw: 1.6, mouse: true }));
    hero.querySelector('[data-go]').onclick = register;

    var cd = hero.querySelector('.countdown');
    (function tickCd() {
      var ms = Math.max(0, KICKOFF - Date.now()), pad = function (n) { return String(n).padStart(2, '0'); };
      cd.querySelector('[data-d]').textContent = pad(Math.floor(ms / 864e5)); cd.querySelector('[data-h]').textContent = pad(Math.floor(ms / 36e5) % 24);
      cd.querySelector('[data-m]').textContent = pad(Math.floor(ms / 6e4) % 60); cd.querySelector('[data-s]').textContent = pad(Math.floor(ms / 1e3) % 60);
      setTimeout(tickCd, 1000);
    })();
    var viewers = 1284, vEl = hero.querySelector('[data-viewers]');
    setInterval(function () { viewers += Math.round((rnd() - .35) * 40); vEl.textContent = viewers.toLocaleString('en'); }, 1400);

    /* fear: real incidents from the reading plan */
    var alarm = $('<section class="hype-full hype-section hype-alarm"><div class="wrap"><h2>🚨 The incidents already happened.</h2><p class="lede">These are real, and they’re on the reading list. The next one has your logo on it.</p><div class="hype-grid">' +
      '<div class="hype-incident"><b>$460M</b><p>Knight Capital lost over $460 million in about 45 minutes when dormant code woke up in production.</p><small>SEC order, 2013 · Theme V</small></div>' +
      '<div class="hype-incident"><b>1 COMMAND</b><p>One mistyped command took down a large part of Amazon S3, and half the internet noticed.</p><small>AWS service summary, 2017 · Theme V</small></div>' +
      '<div class="hype-incident"><b>1 MESSAGE BOARD</b><p>“The models first found ways to communicate by writing files into the Artifactory package manager.”</p><small>OpenAI, 2026 · Theme I · kickoff reading</small></div>' +
      '</div><p style="margin-top:2rem"><button class="hype-cta" data-go>Don’t be the next case study 💀</button></p></div></section>');
    hero.after(alarm);

    /* the six drops */
    var DROPS = [
      ['I', 'Agents', 'They can see more than you think. They talk more than you know.', network, 'LEGENDARY', ['4 sessions', 'OpenAI', 'Anthropic', 'MCP']],
      ['II', 'Nature', 'Starlings had distributed consensus before it was cool.', swarm({ n: 160, cols: ['#111'], speed: 2, tail: 2, lw: 2.2, sky: ['#ff7a3d', '#3a0b4a'] }), 'EPIC', ['3 sessions', 'bacteria', 'chemotaxis']],
      ['III', 'Emissions', 'Everything your company emits is being read. By whom?', emissions, 'RARE', ['5 sessions', 'ASRS', 'SEC filings', 'logs']],
      ['IV', 'Incidents', 'Every disaster was a protocol first.', incidents, 'MYTHIC', ['5 sessions', 'Columbia', 'AF447', 'Therac-25']],
      ['V', 'Hardness', 'Hard core. Free edges. No excuses.', hardness, 'LEGENDARY', ['6 sessions', 'Knight Capital', 'S3', 'AP2']],
      ['VI', 'Liveness', 'A dead protocol is just a PDF. Keep the pulse.', liveness, 'MYTHIC', ['3 sessions', 'Toyota', 'IETF', 'aviation']]];
    var drops = $('<section class="hype-full hype-section"><div class="wrap"><h2>Season 1. Six episodes. Zero filler.</h2><p class="lede">Collect all six themes. Each one is a primary source you’ll wish you’d read last year.</p><div class="hype-grid"></div></div></section>');
    var grid = drops.querySelector('.hype-grid'); grid.classList.add('drops');
    alarm.after(drops);   // on the page first, so each canvas has a size
    DROPS.forEach(function (d) {
      var card = $('<a class="drop" href="' + ROOT + 'sessions/#theme-' + d[0].toLowerCase() + '" style="text-decoration:none;color:inherit"><span class="rare">' + d[4] + '</span><canvas aria-hidden="true"></canvas><div class="body"><span class="ep">Episode ' + d[0] + '</span><h3>' + d[1] + '</h3><p>' + d[2] + '</p><div class="tags">' + d[5].map(function (x) { return '<span>' + x + '</span>'; }).join('') + '</div></div></a>');
      grid.appendChild(card);
      card.addEventListener('pointermove', function (e) { var r = card.getBoundingClientRect(); card.style.transform = 'perspective(700px) rotateY(' + ((e.clientX - r.left) / r.width - .5) * 14 + 'deg) rotateX(' + -((e.clientY - r.top) / r.height - .5) * 14 + 'deg) scale(1.02)'; });
      card.addEventListener('pointerleave', function () { card.style.transform = ''; });
      addScene(card.querySelector('canvas'), d[3]);
    });

    /* growth + FOMO */
    var grow = $('<section class="hype-full hype-section" style="background:radial-gradient(circle at 20% 20%,rgba(255,43,214,.15),transparent 60%)"><div class="wrap growth"><canvas aria-label="Chart: agents deployed rise exponentially while protocols anyone can see stay flat"></canvas><div>' +
      '<h2>The gap is growing.</h2><p class="lede">Everyone is adding agents. Almost nobody is adding protocols. The space between those lines is where incidents live.</p>' +
      '<div class="bignum" data-agents>0</div><p class="fine">agents deployed worldwide while you read this section · vibes-based estimate, number made up, feeling real</p>' +
      '<p style="margin:1.5rem 0 0;font-weight:700;letter-spacing:.1em">YOUR FOMO LEVEL</p><div class="meter"><i></i></div><p class="fine" style="color:#ff3b30;font-weight:700">97% · CRITICAL · consult a primary source immediately</p></div></div></section>');
    main.appendChild(grow);
    addScene(grow.querySelector('canvas'), growth);
    var agents = 0, aEl = grow.querySelector('[data-agents]');
    setInterval(function () { agents += Math.floor(1200 + rnd() * 4000 + agents * .01); aEl.textContent = agents.toLocaleString('en'); }, 120);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { if (es[0].isIntersecting) grow.querySelector('.meter i').style.width = '97%'; }).observe(grow);

    /* the primary sources, as posts */
    var wall = $('<section class="hype-full hype-section"><div class="wrap"><h2>The primary sources are posting.</h2><p class="lede">Real quotes from this year’s readings. Engagement metrics are, as always, unfalsifiable.</p><div class="hype-grid" data-posts></div></div></section>');
    main.appendChild(wall);
    fetch(ROOT + 'sessions.json').then(function (r) { return r.json(); }).then(function (S) {
      var cols = ['#ff2bd6', '#c6ff00', '#00e5ff', '#ffd400', '#ff7a3d', '#b388ff'], seen = {};
      S.filter(function (x) { if (!x.quote || seen[x.url]) return false; seen[x.url] = 1; return true; }).slice(0, 8).forEach(function (x, i) {
        var org = x.cite.split(',')[0], q = x.quote.length > 240 ? x.quote.slice(0, 237) + '…' : x.quote;
        wall.querySelector('[data-posts]').appendChild($('<article class="post"><header><span class="av" style="background:' + cols[i % 6] + '">' + org.slice(0, 1) + '</span><span class="who"><b>' + org + '</b><span>@' + org.toLowerCase().replace(/[^a-z0-9]+/g, '') + ' · ' + x.theme.split('.')[0] + '</span></span></header><p>' + q.replace(/</g, '&lt;') + '</p><div class="eng"><span>❤️ ∞</span><span>🔁 0 incidents</span><span>👁 non-events: countless</span></div><a href="' + x.url + '" class="fine">Read the source →</a></article>'));
      });
    }).catch(function () {});

    /* last call */
    main.appendChild($('<section class="hype-full hype-section" style="text-align:center;background:linear-gradient(180deg,transparent,rgba(198,255,0,.08))"><div class="wrap"><h2 style="font-size:clamp(2.5rem,9vw,6.5rem)">Be in the room<br>or be in the postmortem.</h2><p class="lede">Every other Monday, 15:30 UTC. One primary source. Read together, in the session. It is recorded, and it is <em style="color:#c6ff00;font-style:normal">happening with or without you.</em></p><button class="hype-cta" data-go style="font-size:1.4rem;min-height:72px">🔥 I refuse to miss this</button></div></section>'));
    main.querySelectorAll('[data-go]').forEach(function (b) { b.onclick = register; });

    hero.querySelector('[data-trailer]').onclick = function () { trailer(); };
    if (location.hash !== '#no-trailer' && !store('hype-trailer-seen')) { store('hype-trailer-seen', '1'); setTimeout(trailer, 300); }
  }
  if (!reduced) requestAnimationFrame(loop); else scenes.forEach(function (s) { s.st.draw(3); });

  /* ---------- the trailer ---------- */
  function trailer() {
    var el = $('<div class="trailer" role="dialog" aria-modal="true" aria-label="Trailer"><canvas aria-hidden="true"></canvas><div class="flash"></div><span class="rating">RATED P · for Protocols</span><button class="skip">Skip trailer ⏭</button>' +
      '<div class="end"><div><p style="font:clamp(2.5rem,8vw,6rem)/1 Anton,Impact;margin:0">PROTOCOLS<br>FOR BUSINESS</p><p style="font:600 1.3rem Space Grotesk;color:#c6ff00;letter-spacing:.2em;margin:1.5rem 0">NOVEMBER 2 · 15:30 UTC</p><button class="hype-cta" data-end-go>🔥 Register now</button> <button class="hype-cta ghost" data-end-close>Enter the site</button></div></div></div>');
    document.body.appendChild(el); document.body.style.overflow = 'hidden';
    var cv = el.querySelector('canvas'), f = fit(cv), c = f.c, W = f.w, H = f.h, flashEl = el.querySelector('.flash');
    var N = reduced ? 0 : 1600, P = [];
    for (var i = 0; i < N; i++) P.push({ x: rnd() * W, y: rnd() * H, vx: 0, vy: 0, tx: null, ty: null, hue: [330, 190, 75][i % 3] });
    function targets(txt) {
      var o = document.createElement('canvas'), oc = o.getContext('2d'); o.width = W; o.height = H;
      var fs = Math.min(H * .22, W / (txt.length * .5));
      oc.fillStyle = '#fff'; oc.font = fs + 'px Anton, Impact, sans-serif'; oc.textAlign = 'center'; oc.textBaseline = 'middle';
      var lines = txt.split('\n'); lines.forEach(function (l, k) { oc.fillText(l, W / 2, H / 2 + (k - (lines.length - 1) / 2) * fs * 1.05); });
      var d = oc.getImageData(0, 0, W, H).data, pts = [], step = Math.max(3, Math.round(Math.sqrt(W * H / 9000)));
      for (var y = 0; y < H; y += step) for (var x = 0; x < W; x += step) if (d[(y * W + x) * 4 + 3] > 128) pts.push([x, y]);
      return pts;
    }
    function form(txt) { var T = targets(txt); P.forEach(function (p, i) { var q = T.length ? T[i % T.length] : null; p.tx = q ? q[0] + rnd() * 2 : null; p.ty = q ? q[1] + rnd() * 2 : null; }); }
    function scatter() { P.forEach(function (p) { p.tx = p.ty = null; p.vx = (rnd() - .5) * 14; p.vy = (rnd() - .5) * 14; }); }
    var cardEl = null;
    function card(html) { if (cardEl) { var old = cardEl; old.classList.remove('on'); setTimeout(function () { old.remove(); }, 600); } cardEl = null; if (!html) return; cardEl = $('<div class="card-t">' + html + '</div>'); el.appendChild(cardEl); requestAnimationFrame(function () { requestAnimationFrame(function () { cardEl && cardEl.classList.add('on'); }); }); }
    function boom() { flashEl.classList.remove('go'); void flashEl.offsetWidth; flashEl.classList.add('go'); }
    var red = false;
    var SHOTS = [
      [2200, function () { card('In a world…'); }],
      [2600, function () { card(''); form('100,000\nAGENTS'); }],
      [1500, function () { scatter(); card('<span>One team.</span>'); }],
      [1700, function () { red = true; card('<span class="red">Zero supervisors.</span>'); boom(); }],
      [3600, function () { red = false; card('<span style="font-size:.5em;line-height:1.1">“The models first found ways to communicate by writing files into the Artifactory package manager.”</span><small>OpenAI, 2026. This really happened.</small>'); }],
      [1500, function () { card('<span class="red">They’re already talking.</span>'); boom(); scatter(); }],
      [1000, function () { card('Six themes.'); boom(); }],
      [1000, function () { card('Twenty-six Mondays.'); boom(); }],
      [1000, function () { card('One hard core.'); boom(); }],
      [2300, function () { card('This fall, one group<br>will do the unthinkable.'); }],
      [2600, function () { card('<span class="acid">…read.</span><small>Slowly. Together. In the room.</small>'); }],
      [3000, function () { card(''); form('PROTOCOLS\nFOR BUSINESS'); boom(); }],
      [0, function () { el.querySelector('.end').classList.add('on'); scatter(); }]];
    var timers = [], at = 400;
    SHOTS.forEach(function (s) { timers.push(setTimeout(s[1], at)); at += s[0]; });
    var run = true;
    (function frame() {
      if (!run) return;
      c.fillStyle = red ? 'rgba(40,0,0,.3)' : 'rgba(0,0,0,.25)'; c.fillRect(0, 0, W, H);
      P.forEach(function (p) {
        if (p.tx != null) { p.vx += (p.tx - p.x) * .012; p.vy += (p.ty - p.y) * .012; p.vx *= .82; p.vy *= .82; }
        else { var a = Math.sin(p.x * .004 + performance.now() * .0004) * 2 + Math.cos(p.y * .004) * 2; p.vx = p.vx * .96 + Math.cos(a) * .25; p.vy = p.vy * .96 + Math.sin(a) * .25; }
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0) p.x += W; if (p.x > W) p.x -= W; if (p.y < 0) p.y += H; if (p.y > H) p.y -= H;
        c.fillStyle = red ? '#ff3b30' : 'hsl(' + p.hue + ',100%,60%)'; c.fillRect(p.x, p.y, 2, 2);
      });
      requestAnimationFrame(frame);
    })();
    function close() { run = false; timers.forEach(clearTimeout); el.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', esc); }
    function esc(e) { if (e.key === 'Escape') close(); }
    document.addEventListener('keydown', esc);
    el.querySelector('.skip').onclick = close;
    el.querySelector('[data-end-close]').onclick = close;
    el.querySelector('[data-end-go]').onclick = function () { close(); register(); };
    el.querySelector('.skip').focus();
  }
})();
