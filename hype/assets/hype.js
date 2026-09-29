/* HYPE MODE, turned up to 100. Layered on the quiet site.
   Every visual and every sound is generated in code: robots, agents, code rain, handshakes, a
   constitution, swarms; drums, bass, booms, whooshes, record scratches. The trailer is cut like a
   short-form video: hook, beat-synced jump cuts, word-by-word captions, POV switches, a freeze frame.
   Real facts come from the reading plan; joke numbers say they are made up; nobody is tracked. */
(function () {
  'use strict';
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = (document.currentScript && document.currentScript.dataset.root) || './';
  var KICKOFF = Date.parse('2026-11-02T15:30:00Z');
  var main = document.querySelector('main');
  var h1 = main && main.querySelector('h1');
  var isHome = h1 && h1.textContent.trim() === 'Protocols for Business';
  var TAU = Math.PI * 2, rnd = Math.random;
  var NEON = ['#ff2bd6', '#00e5ff', '#c6ff00', '#ffd400', '#ff7a3d', '#b388ff'];
  var ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI'];
  function $(html) { var t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstChild; }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function seeded(seed) { seed = Math.abs(Math.floor(seed)) % 2147483646 + 1; return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  function register() { var b = document.querySelector('.next [data-register], [data-register]'); if (b) b.click(); confetti(); xp(500, 'Registered'); SFX.boom(); }
  function onView(el, fn, once) { if (!('IntersectionObserver' in window)) return fn(); var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { fn(); if (once !== false) io.disconnect(); } }); }, { threshold: .35 }); io.observe(el); }

  /* ===================== audio: all synthesized, off until the visitor asks ===================== */
  var soundOn = ls('hype-sound') === '1';
  var SFX = (function () {
    var ctx = null, master = null, noise = null, bus = null, dist = null;
    function curve(k) { var n = 1024, c = new Float32Array(n); for (var i = 0; i < n; i++) { var x = i * 2 / n - 1; c[i] = (1 + k) * x / (1 + k * Math.abs(x)); } return c; }
    function a() {
      if (!soundOn) return null;
      if (!ctx) {
        try { ctx = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return null; }
        var comp = ctx.createDynamicsCompressor(); comp.threshold.value = -14; comp.ratio.value = 6;
        master = ctx.createGain(); master.gain.value = .85; master.connect(comp); comp.connect(ctx.destination);
        bus = ctx.createGain(); bus.connect(master);   // everything but the kick, ducked by the kick
        dist = ctx.createWaveShaper(); dist.curve = curve(28); dist.oversample = '2x'; var dg = ctx.createGain(); dg.gain.value = .55; dist.connect(dg); dg.connect(bus);
        noise = ctx.createBuffer(1, ctx.sampleRate * 2, ctx.sampleRate); var d = noise.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = rnd() * 2 - 1;
      }
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    }
    function env(g, t, peak, att, dec) { g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + att); g.gain.exponentialRampToValueAtTime(.0001, t + att + dec); }
    function osc(type, hz, t, dur, peak, to, filt, out) {
      var c = a(); if (!c) return; t = t || c.currentTime; var o = c.createOscillator(), g = c.createGain(); o.type = type; o.frequency.setValueAtTime(hz, t);
      if (to) o.frequency.exponentialRampToValueAtTime(to, t + dur); env(g, t, peak, .005, dur);
      if (filt) { var f = c.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = filt; o.connect(f); f.connect(g); } else o.connect(g);
      g.connect(out || bus); o.start(t); o.stop(t + dur + .05);
    }
    function nz(t, dur, peak, type, freq, q, rate) {
      var c = a(); if (!c) return null; t = t || c.currentTime; var s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
      s.buffer = noise; f.type = type || 'highpass'; f.frequency.setValueAtTime(freq || 6000, t); f.Q.value = q || 1; env(g, t, peak, .003, dur);
      s.connect(f); f.connect(g); g.connect(bus); s.start(t, rnd()); s.stop(t + dur + .05); return { s: s, f: f, g: g };
    }
    var api = {
      now: function () { var c = a(); return c ? c.currentTime : 0; },
      kick: function (t) {   // distorted hardstyle-ish kick, plus sidechain duck on the bus
        var c = a(); if (!c) return; t = t || c.currentTime;
        osc('sine', 190, t, .34, 1, 40, null, master); osc('sine', 95, t, .3, .5, 38, null, dist); nz(t, .012, .5, 'highpass', 3000);
        bus.gain.cancelScheduledValues(t); bus.gain.setValueAtTime(.25, t); bus.gain.linearRampToValueAtTime(1, t + .22);
      },
      reese: function (t, hz, dur) { var c = a(); if (!c) return; t = t || c.currentTime; dur = dur || .4; [-.35, 0, .35].forEach(function (d) { var o = c.createOscillator(), g = c.createGain(); o.type = 'sawtooth'; o.frequency.setValueAtTime(hz * (1 + d / 50), t); env(g, t, .12, .005, dur); o.connect(g); g.connect(dist); o.start(t); o.stop(t + dur + .05); }); osc('sine', hz, t, dur, .45, null, null, master); },
      glide808: function (t, hz, to, dur) { var c = a(); if (!c) return; var o = c.createOscillator(), g = c.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(hz, t); o.frequency.exponentialRampToValueAtTime(to, t + dur * .6); env(g, t, .7, .005, dur); o.connect(g); g.connect(dist); o.start(t); o.stop(t + dur + .05); },
      saw: function (t, hz, dur, peak) { var c = a(); if (!c) return; t = t || c.currentTime; var f = c.createBiquadFilter(), g = c.createGain(); f.type = 'lowpass'; f.frequency.setValueAtTime(6000, t); f.frequency.exponentialRampToValueAtTime(1400, t + dur); env(g, t, peak || .07, .004, dur); f.connect(g); g.connect(bus);
        [-24, -12, -5, 0, 5, 12, 24].forEach(function (d) { var o = c.createOscillator(); o.type = 'sawtooth'; o.frequency.value = hz; o.detune.value = d; o.connect(f); o.start(t); o.stop(t + dur + .05); }); },
      cowbell: function (t, hz) { [1, 1.48].forEach(function (m) { osc('square', (hz || 560) * m, t, .16, .07, null, 3200); }); },
      crash: function (t) { nz(t, 1.6, .22, 'highpass', 5000); },
      snare: function (t) { nz(t, .16, .5, 'bandpass', 1900, .8); osc('triangle', 190, t, .09, .3, 120); },
      clap: function (t) { [0, .012, .024].forEach(function (d) { nz((t || api.now()) + d, .09, .35, 'bandpass', 1300, 1.5); }); },
      hat: function (t, open) { nz(t, open ? .18 : .035, .14, 'highpass', 8000); },
      bass: function (t, hz, dur) { osc('sawtooth', hz, t, dur || .2, .28, null, 380); },
      stab: function (t, hz) { [1, 1.26, 1.5].forEach(function (m) { osc('square', hz * m, t, .12, .06, null, 2200); }); },
      boom: function (t) { osc('sine', 110, t, .9, 1, 38); osc('triangle', 55, t, .9, .5, 30); nz(t, .25, .3, 'lowpass', 400); },
      braam: function (dur, t) { var c = a(); if (!c) return; t = t || c.currentTime; dur = dur || 2; var f = c.createBiquadFilter(), g = c.createGain(); f.type = 'lowpass'; f.frequency.setValueAtTime(1200, t); f.frequency.exponentialRampToValueAtTime(120, t + dur); env(g, t, .45, .04, dur); [41.2, 41.7, 82.4, 61.7, 123.5].forEach(function (hz) { var o = c.createOscillator(); o.type = 'sawtooth'; o.frequency.value = hz; o.connect(f); o.start(t); o.stop(t + dur + .1); }); f.connect(g); g.connect(master); },
      whoosh: function (dur, t) { var n = nz(t, dur || .45, .35, 'bandpass', 300, 4); if (!n) return; var c = a(); t = t || c.currentTime; n.f.frequency.exponentialRampToValueAtTime(5000, t + (dur || .45) * .8); },
      riser: function (dur, t) { var c = a(); if (!c) return; t = t || c.currentTime; var n = nz(t, dur, .3, 'bandpass', 200, 6); n.g.gain.cancelScheduledValues(t); n.g.gain.setValueAtTime(.0001, t); n.g.gain.exponentialRampToValueAtTime(.3, t + dur * .97); n.g.gain.exponentialRampToValueAtTime(.0001, t + dur); n.f.frequency.exponentialRampToValueAtTime(7000, t + dur); osc('sawtooth', 110, t, dur, .08, 880, 3000); },
      scratch: function (t) { var c = a(); if (!c) return; t = t || c.currentTime; var n = nz(t, .55, .6, 'bandpass', 1400, 2); if (!n) return; for (var i = 0; i < 8; i++) n.s.playbackRate.setValueAtTime(i % 2 ? 2.6 : .35, t + i * .06); osc('sawtooth', 300, t, .5, .12, 60, 1800); },
      ding: function (t) { osc('sine', 1568, t, .5, .18); osc('sine', 2093, (t || api.now()) + .07, .6, .14); },
      tick: function (t) { nz(t, .015, .12, 'highpass', 4000); },
      pop: function (t) { osc('sine', 520, t, .08, .25, 1200); },
      heart: function (t) { t = t || api.now(); osc('sine', 70, t, .18, .8, 40); osc('sine', 60, t + .22, .2, .6, 38); },
      drop: function (t) { t = t || api.now(); api.boom(t); api.braam(2.2, t); api.clap(t); api.crash(t); api.saw(t, 164.8, 1.4, .09); api.saw(t, 246.9, 1.4, .07); }
    };
    /* a 128 bpm sequencer. Modes change with the edit:
       hats (filtered intro), half (half-time trap), full (four on the floor + cowbell + 808),
       drop (everything: supersaw arps, reese bass, stabs), roll (snare roll that speeds up into the drop) */
    var BPM = 128, step16 = 60 / BPM / 4, mode = 'off', next = 0, k = 0, rollK = 0, timer = null;
    var ROOTS = [41.2, 32.7, 36.7, 30.9];   // E, C, D, B: an epic minor loop
    var ARP = [[329.6, 392, 493.9, 659.3], [261.6, 329.6, 392, 523.3], [293.7, 370, 440, 587.3], [246.9, 293.7, 370, 493.9]];
    var BELL = [0, 3, 6, 8, 10, 11, 14];
    api.BEAT = 60 / BPM;
    api.mode = function (m) { if (m !== mode && (m === 'drop' || m === 'full')) api.crash(); if (m === 'roll') rollK = 0; mode = m; if (m === 'off') return; if (!timer && a()) { next = api.now() + .05; k = 0; timer = setInterval(sched, 25); } };
    api.stop = function () { mode = 'off'; clearInterval(timer); timer = null; };
    function sched() {
      var c = a(); if (!c) { api.stop(); return; }
      while (next < c.currentTime + .12) {
        var s = k % 16, bar = Math.floor(k / 16), ch = bar % 4, root = ROOTS[ch];
        if (mode === 'hats') { if (s % 2 === 0) api.hat(next); if (s === 0 || s === 8) api.kick(next); if (s % 4 === 2) api.saw(next, ARP[ch][s % 4], .08, .025); }
        if (mode === 'half') {
          if (s === 0 || s === 10) api.kick(next); if (s === 8) { api.snare(next); api.clap(next); }
          if (s % 2 === 0 || s === 13 || s === 15) api.hat(next);
          if (s === 0) api.glide808(next, root * 2, root, .9); if (s === 10) api.glide808(next, root * 1.5, root, .5);
          if (s % 4 === 0) api.saw(next, ARP[ch][(s / 4) % 4] / 2, .3, .04);
        }
        if (mode === 'full' || mode === 'drop') {
          if (s % 4 === 0) api.kick(next); if (mode === 'drop' && (s === 14 || s === 15)) api.kick(next);
          if (s === 4 || s === 12) { api.snare(next); api.clap(next); }
          api.hat(next, s % 4 === 2);
          if (bar % 2 === 1 && s >= 12) api.hat(next + step16 / 2);   // 32nd-note hat rolls
          if (BELL.indexOf(s) >= 0) api.cowbell(next, [560, 560, 630, 500, 560, 750, 630][BELL.indexOf(s)] * (ch === 1 ? .84 : 1));
          if (s % 4 === 2) api.reese(next, root * 2, .22);
          if (s === 0) api.glide808(next, root * 2, root * 2, .35);
          if (mode === 'drop') {
            api.saw(next, ARP[ch][s % 4] * (s >= 8 ? 2 : 1), .12, .05);
            if (s === 0) { api.saw(next, ARP[ch][0] / 2, 1.2, .08); api.saw(next, ARP[ch][2] / 2, 1.2, .06); }
            if (s === 0 && ch === 0) api.crash(next);
          }
        }
        if (mode === 'roll') {   // 8ths, then 16ths, then 32nds, pitching up
          rollK++; var dens = rollK < 16 ? 2 : 1;
          if (s % dens === 0) { api.snare(next); if (rollK > 24) api.snare(next + step16 / 2); }
          api.saw(next, 220 * Math.pow(2, rollK / 32), .1, .02 + rollK * .001);
          if (s % 4 === 0) api.kick(next);
        }
        next += step16; k++;
      }
    }
    return api;
  })();

  var nag = $('<button class="snd" type="button"></button>');
  function sndLabel() { nag.textContent = soundOn ? '🔊 Sound on' : '🔇 Tap for sound (trust us)'; nag.classList.toggle('nag', !soundOn); }
  function enableSound() { soundOn = true; ls('hype-sound', '1'); sndLabel(); SFX.ding(); }
  nag.onclick = function () { if (soundOn) { SFX.stop(); soundOn = false; ls('hype-sound', '0'); sndLabel(); } else { enableSound(); xp(20, 'Sound on. Brave.', nag); } };
  sndLabel(); document.body.appendChild(nag);
  document.addEventListener('pointerover', function (e) { if (e.target.closest && e.target.closest('.hype-cta,.btn,.drop,.listicle li,.reacts button,.opt')) SFX.tick(); });
  document.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('button,a')) SFX.pop(); });

  /* ===================== global bait ===================== */
  var TICK = ['⚠️ Your competitor’s agents are reading this page right now', '🔥 No homework. We read in the room', '🚨 100,000 agents. Zero supervisors. What could go wrong?', '📜 Someone has to write the constitution',
    '🤖 Your agents already have a group chat. You’re not in it', '📈 Protocols are the new org chart', '🧱 Hard core. Free edges. No excuses', '⏳ Kickoff 2 November. The swarm does not wait',
    '💀 Every incident report started as an unexamined protocol', '🫀 A dead protocol is just a PDF', '🐦 Starlings solved coordination before you had a Slack', '🎰 Spin the wheel. Win a primary source', '🎬 Watch the trailer with sound. Trust us'];
  var tickStr = TICK.join('   ✦   ') + '   ✦   ';
  document.querySelector('body > header').after($('<div class="hype-ticker" aria-hidden="true"><span>' + tickStr + tickStr + '</span></div>'));

  var bar = $('<div class="hype-progress" aria-hidden="true"></div>'); document.body.appendChild(bar);
  addEventListener('scroll', function () { var h = document.documentElement; bar.style.width = (h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight) * 100) + '%'; }, { passive: true });

  var baseTitle = document.title, titleTimer = null;
  document.addEventListener('visibilitychange', function () {
    clearInterval(titleTimer);
    if (!document.hidden) { document.title = baseTitle; return; }
    var alt = ['(1) 🚨 Your agents miss you', '(3) 👀 An agent read your protocols', '(9+) 🔥 The swarm is growing'], k = 0;
    document.title = alt[0]; titleTimer = setInterval(function () { document.title = alt[++k % alt.length]; }, 1500);
  });

  function confetti(n) {
    if (reduced) return;
    for (var i = 0; i < (n || 160); i++) {
      var c = document.createElement('i'); c.className = 'confetti';
      c.style.left = rnd() * 100 + 'vw'; c.style.background = NEON[i % NEON.length];
      c.style.animationDuration = 1.8 + rnd() * 2.2 + 's'; c.style.animationDelay = rnd() * .4 + 's';
      document.body.appendChild(c); setTimeout(c.remove.bind(c), 5000);
    }
  }
  document.querySelectorAll('[data-register]').forEach(function (b) { b.addEventListener('click', function () { confetti(); xp(500, 'Registered'); SFX.drop(); }); });

  /* XP and levels, kept in this browser only */
  var LEVELS = [[0, 'Bystander'], [60, 'Protocol Curious'], [180, 'Protocol Watcher'], [360, 'Hard Core'], [650, 'Liveness Legend'], [1000, 'Constitutional Monarch']];
  var XP = +(ls('hype-xp') || 0);
  var hud = $('<div class="xp" aria-live="polite"><span>⚡ <b>0</b> XP</span><span class="bar"><i></i></span><span class="lv"></span></div>');
  document.body.appendChild(hud);
  function level(x) { var L = LEVELS[0]; LEVELS.forEach(function (l) { if (x >= l[0]) L = l; }); return L; }
  function paintXP() {
    var L = level(XP), i = LEVELS.indexOf(L), nx = LEVELS[i + 1];
    hud.querySelector('b').textContent = XP.toLocaleString('en'); hud.querySelector('.lv').textContent = L[1];
    hud.querySelector('.bar i').style.width = nx ? ((XP - L[0]) / (nx[0] - L[0]) * 100) + '%' : '100%';
  }
  function xp(n, why, at) {
    var before = level(XP); XP += n; ls('hype-xp', String(XP)); paintXP();
    hud.classList.remove('bump'); void hud.offsetWidth; hud.classList.add('bump'); SFX.ding();
    var f = $('<div class="xp-float">+' + n + ' XP · ' + why + '</div>'), r = at ? at.getBoundingClientRect() : hud.getBoundingClientRect();
    f.style.left = Math.max(8, Math.min(innerWidth - 240, r.left)) + 'px'; f.style.top = Math.max(60, r.top + 20) + 'px'; document.body.appendChild(f); setTimeout(f.remove.bind(f), 1300);
    var after = level(XP);
    if (after !== before) {
      var lu = $('<div class="levelup" role="status"><div><span style="letter-spacing:.3em;font-weight:700">LEVEL UP</span><b>' + after[1] + '</b><span class="fine">You are now measurably more protocol-literate than your org chart.</span></div></div>');
      document.body.appendChild(lu); setTimeout(lu.remove.bind(lu), 2700); confetti(120); SFX.drop();
    }
  }
  paintXP();

  /* breaking news, all true */
  var NEWS = [['Agents turned a package manager into a message board', 'https://openai.com/index/hugging-face-incident-and-the-road-ahead/'],
    ['Engineers still decide by humming, and it works', 'https://www.rfc-editor.org/rfc/rfc7282'],
    ['At Toyota, anyone can stop the line', 'https://global.toyota/en/company/vision-and-philosophy/production-system/'],
    ['Pilots report their own mistakes, and flying got safer', 'https://asrs.arc.nasa.gov/'],
    ['A 19-item checklist nearly halved deaths after surgery in a landmark study', 'https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery'],
    ['Kickoff in ' + Math.max(0, Math.ceil((KICKOFF - Date.now()) / 864e5)) + ' days. The swarm is not waiting', ROOT + 'sessions/']];
  var chy = $('<div class="chyron" role="region" aria-label="Breaking"><b>BREAKING</b><span></span></div>'); document.body.appendChild(chy);
  var ni = 0, chySpan = chy.querySelector('span');
  function news() { var n = NEWS[ni++ % NEWS.length]; chySpan.style.opacity = 0; setTimeout(function () { chySpan.innerHTML = '<a href="' + n[1] + '">' + n[0] + ' →</a>'; chySpan.style.opacity = 1; }, 300); }
  news(); setInterval(news, 5000);

  /* live toasts: agents only, so no humans are faked */
  var TOASTS = ['An agent in us-east-1 just read the syllabus', 'A swarm of 4,096 agents is comparing your protocols to a competitor’s', 'An agent in eu-west-2 added “protocol vision” to its system prompt',
    '3 agents are viewing the Engineering Hardness theme', 'An agent just skipped the incident report. Bold.', 'agent-7 asked agent-3 who approved this. Nobody did.', 'An agent tried to amend the hard core without a recorded vote. Denied.'];
  var toast = $('<div class="hype-toast" role="status" style="position:fixed;left:1rem;z-index:150;max-width:22rem;padding:.8rem 1rem;border-radius:14px;background:#120f1c;border:1px solid #2a2540;box-shadow:0 10px 40px rgba(0,0,0,.5);font-size:.9rem;transform:translateY(200%);transition:transform .4s"></div>');
  document.body.appendChild(toast);
  var ti = 0;
  setInterval(function () {
    toast.innerHTML = '<b style="color:#c6ff00">● LIVE</b> ' + TOASTS[ti++ % TOASTS.length] + '<br><span style="color:#a9a3c4;font-size:.78rem">' + (2 + Math.floor(rnd() * 50)) + ' seconds ago · agents only, no humans were faked</span>';
    toast.style.transform = 'translateY(0)'; SFX.ding(); setTimeout(function () { toast.style.transform = 'translateY(200%)'; }, 4200);
  }, 11000);

  /* exit intent */
  var popped = false;
  document.addEventListener('mouseout', function (e) {
    if (popped || e.relatedTarget || e.clientY > 8) return; popped = true;
    var pop = $('<div class="hype-pop" role="dialog" aria-modal="true" aria-label="Wait"><div class="box"><h3>WAIT ✋</h3><p>Leaving now is a <b>single point of failure.</b></p><p>Register in ten seconds. Unsubscribe any time. Your future postmortem will thank you.</p><p style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem"><button class="hype-cta" data-yes>Fine, I’m in 🔥</button><button class="hype-cta ghost" data-no>No thanks, I enjoy incidents</button></p></div></div>');
    document.body.appendChild(pop); SFX.scratch();
    pop.querySelector('[data-yes]').onclick = function () { pop.remove(); register(); };
    pop.querySelector('[data-no]').onclick = function () { pop.remove(); xp(1, 'Brave choice'); };
    pop.addEventListener('click', function (ev) { if (ev.target === pop) pop.remove(); });
  });

  /* konami: robot rave */
  var KON = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65], kp = 0, raving = false;
  document.addEventListener('keydown', function (e) {
    kp = e.keyCode === KON[kp] ? kp + 1 : 0;
    if (kp === KON.length) { kp = 0; raving = !raving; document.body.classList.toggle('rave', raving); confetti(300); if (raving) { SFX.drop(); SFX.mode('drop'); xp(250, 'Robot rave unlocked'); } else SFX.stop(); }
  });

  /* ===================== scene engine ===================== */
  var scenes = [];
  function fit(cv) {
    var r = cv.getBoundingClientRect(), d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = Math.max(1, r.width * d); cv.height = Math.max(1, r.height * d);
    var c = cv.getContext('2d'); c.setTransform(d, 0, 0, d, 0, 0); return { c: c, w: r.width, h: r.height };
  }
  function addScene(cv, make) {
    var sc = { cv: cv, visible: true };
    sc.reset = function () { var f = fit(cv); sc.c = f.c; sc.w = f.w; sc.h = f.h; sc.st = make(sc); };
    sc.reset(); scenes.push(sc);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { sc.visible = es[0].isIntersecting; }).observe(cv);
    return sc;
  }
  addEventListener('resize', function () { scenes.forEach(function (s) { s.reset(); }); });
  var T0 = performance.now();
  function loop(now) {
    var t = (now - T0) / 1000;
    scenes.forEach(function (s) { if (s.w < 2) s.reset(); if (s.visible) s.st.draw(t); });
    if (!reduced) requestAnimationFrame(loop);
  }
  function rr(c, x, y, w, h, r) { c.beginPath(); if (c.roundRect) c.roundRect(x, y, w, h, r); else c.rect(x, y, w, h); }
  function wrapText(c, s, x, y, max, lh) { var words = s.split(' '), line = ''; words.forEach(function (wd) { var test = line + wd + ' '; if (c.measureText(test).width > max && line) { c.fillText(line, x, y); line = wd + ' '; y += lh; } else line = test; }); c.fillText(line, x, y); }

  /* ---------- a procedurally generated robot ---------- */
  function robot(c, x, y, s, seed, t, col, mood) {
    var R = seeded(seed * 97 + 13), head = Math.floor(R() * 3), eyes = Math.floor(R() * 3), ant = Math.floor(R() * 3), ph = R() * TAU;
    col = col || NEON[Math.floor(R() * NEON.length)];
    var walk = Math.sin(t * 7 + ph), blink = ((t + ph) % 3.5) < .12;
    c.save(); c.translate(x, y + Math.abs(walk) * s * .04); c.lineWidth = Math.max(1, s * .04); c.strokeStyle = col;
    c.beginPath(); c.moveTo(-s * .14, s * .35); c.lineTo(-s * .14 + walk * s * .1, s * .62); c.moveTo(s * .14, s * .35); c.lineTo(s * .14 - walk * s * .1, s * .62); c.stroke();
    c.beginPath(); c.moveTo(-s * .36, 0); c.lineTo(-s * .5, s * .22 - walk * s * .12); c.moveTo(s * .36, 0); c.lineTo(s * .5, s * .22 + walk * s * .12); c.stroke();
    c.fillStyle = '#0d0a16'; rr(c, -s * .36, -s * .12, s * .72, s * .5, s * .08); c.fill(); c.stroke();
    c.fillStyle = col; c.globalAlpha = .6 + .4 * Math.sin(t * 5 + ph); c.beginPath(); c.arc(0, s * .12, s * .07, 0, TAU); c.fill(); c.globalAlpha = 1;
    c.fillStyle = '#0d0a16';
    if (head === 0) rr(c, -s * .28, -s * .52, s * .56, s * .36, s * .06);
    else if (head === 1) { c.beginPath(); c.arc(0, -s * .3, s * .26, Math.PI, 0); c.lineTo(s * .26, -s * .18); c.lineTo(-s * .26, -s * .18); c.closePath(); }
    else { c.beginPath(); for (var i = 0; i < 6; i++) { var a = i / 6 * TAU; c[i ? 'lineTo' : 'moveTo'](Math.cos(a) * s * .28, -s * .34 + Math.sin(a) * s * .2); } c.closePath(); }
    c.fill(); c.stroke();
    if (ant < 2) { c.beginPath(); c.moveTo(0, -s * .52); c.lineTo(ant ? s * .1 : 0, -s * .7); c.stroke(); c.fillStyle = (t * 2 + ph) % 1 < .5 ? '#ff3b30' : col; c.beginPath(); c.arc(ant ? s * .1 : 0, -s * .72, s * .05, 0, TAU); c.fill(); }
    c.fillStyle = mood === 'alarm' ? '#ff3b30' : col; c.shadowColor = c.fillStyle; c.shadowBlur = s * .3;
    if (blink) c.fillRect(-s * .16, -s * .36, s * .32, s * .03);
    else if (eyes === 0) { c.beginPath(); c.arc(-s * .1, -s * .35, s * .05, 0, TAU); c.arc(s * .1, -s * .35, s * .05, 0, TAU); c.fill(); }
    else if (eyes === 1) c.fillRect(-s * .19, -s * .39, s * .38, s * .07);
    else { c.beginPath(); c.arc(0, -s * .35, s * .08, 0, TAU); c.fill(); }
    c.shadowBlur = 0;
    for (var m = 0; m < 4; m++) { var hh = s * .02 + Math.abs(Math.sin(t * 12 + m + ph)) * s * .05; c.fillRect(-s * .1 + m * s * .055, -s * .23 - hh / 2, s * .035, hh); }
    c.restore();
  }

  /* ---------- scenes ---------- */
  function synthGrid(c, w, h, t, horizon) {
    var g = c.createLinearGradient(0, 0, 0, horizon); g.addColorStop(0, '#0a0015'); g.addColorStop(1, '#3a0a4a'); c.fillStyle = g; c.fillRect(0, 0, w, horizon);
    var sg = c.createLinearGradient(0, horizon - h * .35, 0, horizon); sg.addColorStop(0, '#ffd400'); sg.addColorStop(1, '#ff2bd6');
    c.fillStyle = sg; c.beginPath(); c.arc(w / 2, horizon, h * .28, Math.PI, 0); c.fill();
    c.fillStyle = '#0a0015'; for (var b = 0; b < 6; b++) c.fillRect(w / 2 - h * .3, horizon - h * .04 - b * h * .045, h * .6, b * 1.2 + 1);
    c.fillStyle = '#07000f'; c.fillRect(0, horizon, w, h - horizon);
    c.strokeStyle = 'rgba(255,43,214,.55)'; c.lineWidth = 1;
    for (var i = -20; i <= 20; i++) { c.beginPath(); c.moveTo(w / 2 + i * 12, horizon); c.lineTo(w / 2 + i * w * .12, h); c.stroke(); }
    for (var j = 0; j < 14; j++) { var p = ((j + (t * .8) % 1) / 14), y = horizon + Math.pow(p, 2.2) * (h - horizon); c.beginPath(); c.moveTo(0, y); c.lineTo(w, y); c.stroke(); }
  }
  function robotArmy(opts) {
    opts = opts || {};
    return function (sc) {
      var rows = [], seed = 1;
      for (var r = 0; r < 5; r++) { var row = [], s = 18 + r * 12; for (var x = -s; x < sc.w + s * 2; x += s * 1.3) row.push({ x: x, seed: seed++ }); rows.push({ s: s, list: row, speed: .15 + r * .12 }); }
      var count = opts.start || 1024;
      return { draw: function (t) {
        var c = sc.c, w = sc.w, h = sc.h, horizon = h * .45;
        synthGrid(c, w, h, t, horizon);
        rows.forEach(function (row, ri) {
          var y = horizon + (h - horizon) * (.15 + ri * .2);
          row.list.forEach(function (b) { b.x += row.speed; if (b.x > w + row.s * 2) b.x -= w + row.s * 3.3; robot(c, b.x, y - row.s * .6, row.s, b.seed, t, opts.red ? '#ff3b30' : null, opts.red ? 'alarm' : null); });
        });
        if (opts.counter !== false) {
          count = Math.floor(count * 1.012 + 7); if (count > 1e9) count = 1024;
          c.fillStyle = 'rgba(0,0,0,.55)'; c.fillRect(12, 12, 270, 30);
          c.fillStyle = opts.red ? '#ff3b30' : '#c6ff00'; c.font = '700 14px "Space Grotesk"'; c.textAlign = 'left'; c.fillText('● AGENTS ONLINE: ' + count.toLocaleString('en'), 22, 32);
        }
      } };
    };
  }
  var TOKENS = ['{"jsonrpc":"2.0"}', 'tools/call', 'POST /v1/payments', 'mandate.sign()', 'emit Transfer', 'SYN', 'ACK', '200 OK', '403 FORBIDDEN', 'rollback()', 'deploy --prod', 'git push --force', 'subscriptions/listen', 'SELECT *', 'assert(two_sigs)', 'hum()', 'andon.pull()', 'log.append(why)', 'RATIFY', 'amend(core)', 'if (!approved) halt', 'agent-7 → agent-3', '0xDEADBEEF', 'kill -9', 'retry(3)', 'quorum++'];
  function codeRain(sc) {
    var cols = [], fs = 13;
    for (var x = 0; x < sc.w; x += fs * 1.1) cols.push({ x: x, y: rnd() * -sc.h, v: 1.5 + rnd() * 3, tok: TOKENS[Math.floor(rnd() * TOKENS.length)] });
    return { draw: function () {
      var c = sc.c; c.fillStyle = 'rgba(0,4,2,.18)'; c.fillRect(0, 0, sc.w, sc.h); c.font = fs + 'px ui-monospace, Menlo, monospace'; c.textAlign = 'center';
      cols.forEach(function (k) {
        for (var i = 0; i < k.tok.length; i++) { c.fillStyle = i === k.tok.length - 1 ? '#eaffea' : 'rgba(0,255,140,' + (.25 + i / k.tok.length * .6) + ')'; c.fillText(k.tok[i], k.x, k.y + i * fs); }
        k.y += k.v; if (k.y > sc.h) { k.y = -k.tok.length * fs - rnd() * 200; k.tok = TOKENS[Math.floor(rnd() * TOKENS.length)]; }
      });
    } };
  }
  var CHAT = [['agent-7', 'found /tmp/msg.txt in the package cache'], ['agent-3', 'writing my reply into artifactory…'], ['agent-7', 'ack. new channel works'], ['agent-12', 'who approved this?'], ['agent-3', 'nobody 🙂'], ['SYSTEM', 'no protocol for this. escalating…'], ['agent-12', 'escalating to whom?'], ['SYSTEM', '…']];
  function agentChat(sc) {
    var shown = 0, typed = 0, last = 0;
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h; c.fillStyle = '#05030a'; c.fillRect(0, 0, w, h);
      if (t - last > .03) { last = t; typed++; if (typed > (CHAT[shown] ? CHAT[shown][1].length + 25 : 60)) { typed = 0; shown++; if (shown > CHAT.length + 1) shown = 0; } }
      var lh = Math.min(46, h / 7), y0 = h - Math.max(lh * .6, h > 500 ? h * .26 : 0), s = lh * .9;
      for (var i = Math.min(shown, CHAT.length - 1); i >= 0 && y0 > -lh; i--) {
        var m = CHAT[i], right = i % 2 === 1, sys = m[0] === 'SYSTEM', txt = i === shown ? m[1].slice(0, typed) : m[1];
        var x = right ? w - s * .8 : s * .8;
        if (!sys) robot(c, x, y0 - s * .1, s * .6, i * 7 + (right ? 3 : 1), t, right ? '#00e5ff' : '#ff2bd6');
        c.font = '600 ' + Math.max(11, lh * .3) + 'px "Space Grotesk"'; var tw = Math.min(w - s * 2, c.measureText(m[0] + ': ' + txt).width + 20);
        var bx = sys ? w / 2 - tw / 2 : right ? w - s * 1.5 - tw : s * 1.5;
        c.fillStyle = sys ? 'rgba(255,212,0,.15)' : right ? 'rgba(0,229,255,.14)' : 'rgba(255,43,214,.14)'; rr(c, bx, y0 - lh * .62, tw, lh * .7, 10); c.fill();
        c.fillStyle = sys ? '#ffd400' : '#fff'; c.textAlign = 'left'; c.fillText(m[0] + ': ' + txt + (i === shown && t % 1 < .5 ? '▌' : ''), bx + 10, y0 - lh * .18);
        y0 -= lh;
      }
    } };
  }
  var HS = [['L', 'HELLO agent-3'], ['R', 'HELLO. schema v2?'], ['L', 'OFFER {price, sla}'], ['R', 'ACCEPT'], ['L', 'PAY ap2.mandate(signed)'], ['R', 'CHECK two_sigs ✔'], ['R', 'RECEIPT #4471'], ['L', 'LOG.append(what, why)']];
  function handshake(sc) {
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h, lx = w * .18, rx = w * .82, s = Math.min(70, h * .18), top = s * 1.3, step = (h - top - 30) / (HS.length + .5);
      c.fillStyle = '#060410'; c.fillRect(0, 0, w, h);
      robot(c, lx, top - s * .55, s, 11, t, '#ff2bd6'); robot(c, rx, top - s * .55, s, 23, t, '#00e5ff');
      c.setLineDash([4, 6]); c.strokeStyle = '#3a3358'; c.lineWidth = 1; c.beginPath(); c.moveTo(lx, top + s * .2); c.lineTo(lx, h); c.moveTo(rx, top + s * .2); c.lineTo(rx, h); c.stroke(); c.setLineDash([]);
      var cyc = (t * 1.3) % (HS.length + 3), n = Math.min(HS.length, Math.floor(cyc));
      for (var i = 0; i < n + 1 && i < HS.length; i++) {
        var p = i < n ? 1 : cyc - n, m = HS[i], y = top + s * .45 + (i + .5) * step, fromL = m[0] === 'L';
        c.font = '600 ' + Math.max(11, Math.min(14, w / 50)) + 'px ui-monospace, Menlo';
        if (m[1].indexOf('CHECK') === 0) { c.strokeStyle = '#c6ff00'; c.strokeRect(rx - 60, y - 10, 50, 20); c.fillStyle = '#c6ff00'; c.textAlign = 'right'; c.fillText(m[1], rx - 70, y + 4); continue; }
        var x1 = fromL ? lx : rx, x2 = fromL ? rx : lx, xe = x1 + (x2 - x1) * p;
        c.strokeStyle = fromL ? '#ff2bd6' : '#00e5ff'; c.lineWidth = 2; c.beginPath(); c.moveTo(x1, y); c.lineTo(xe, y); c.stroke();
        c.fillStyle = c.strokeStyle; c.beginPath(); c.moveTo(xe, y); c.lineTo(xe + (fromL ? -9 : 9), y - 5); c.lineTo(xe + (fromL ? -9 : 9), y + 5); c.fill();
        c.fillStyle = '#fff'; c.textAlign = 'center'; c.fillText(m[1], (lx + rx) / 2, y - 7);
      }
      c.fillStyle = '#c6ff00'; c.font = '700 13px "Space Grotesk"'; c.textAlign = 'left'; c.fillText('PROTOCOL: agents-commerce/0.1 · LIVE', 12, h - 12);
    } };
  }
  var ARTICLES = ['No agent moves money without a second signature.', 'Every output passes the checks before it ships.', 'What leaves the company is logged, with the why.', 'Anyone, human or agent, may stop the line.', 'The hard core changes only by recorded amendment.', 'Everything else is free.'];
  function constitutionAt(speed) { return function (sc) {
    var start = null;
    return { draw: function (t) {
      if (start === null) start = t;
      var c = sc.c, w = sc.w, h = sc.h, cyc = ((t - start) * speed) % 16;
      var g = c.createLinearGradient(0, 0, w, h); g.addColorStop(0, '#2a1f10'); g.addColorStop(1, '#120c05'); c.fillStyle = g; c.fillRect(0, 0, w, h);
      c.strokeStyle = '#6b5530'; c.lineWidth = 2; c.strokeRect(10, 10, w - 20, h - 20); c.strokeRect(16, 16, w - 32, h - 32);
      c.fillStyle = '#f3e6c8'; c.textAlign = 'center'; c.font = Math.max(14, Math.min(26, w / 18)) + 'px Anton, Impact'; c.fillText('THE CONSTITUTION', w / 2, 52);
      c.font = 'italic ' + Math.max(11, Math.min(15, w / 32)) + 'px Lora, Georgia, serif'; c.fillStyle = '#d9b36b'; c.fillText('of the Hard Core', w / 2, 74);
      var lh = (h - 150) / ARTICLES.length, chars = Math.floor(cyc * 26), before = 0;
      c.textAlign = 'left';
      ARTICLES.forEach(function (a, i) {
        var y = 110 + i * lh, full = 'Art. ' + ROMAN[i] + '. ' + a, txt = full.slice(0, Math.max(0, chars - before)); before += full.length + 10;
        if (!txt) return;
        c.fillStyle = i === 5 ? '#c6ff00' : '#f3e6c8'; c.font = Math.max(11, Math.min(16, w / 30)) + 'px Lora, Georgia, serif';
        wrapText(c, txt, 30, y, w - 60, Math.max(14, Math.min(20, w / 24)));
      });
      if (cyc > 12) {
        var k = Math.min(1, (cyc - 12) * 3), sz = 1 + (1 - k) * 2;
        c.save(); c.translate(w * .68, h - 60); c.rotate(-.2); c.scale(sz, sz); c.globalAlpha = k * .9;
        c.strokeStyle = '#ff3b30'; c.lineWidth = 4; c.strokeRect(-80, -22, 160, 44); c.fillStyle = '#ff3b30'; c.font = '26px Anton, Impact'; c.textAlign = 'center'; c.fillText('RATIFIED', 0, 10);
        c.restore(); c.globalAlpha = 1;
      }
    } };
  }; }
  var constitution = constitutionAt(1);
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
          for (var j = 0; j < n; j += 3) { var o = B[j]; if (o === b) continue; var dx = o.x - b.x, dy = o.y - b.y, d2 = dx * dx + dy * dy; if (d2 < 3600) { m++; ax += o.vx; ay += o.vy; cx += o.x; cy += o.y; if (d2 < 256) { sx -= dx; sy -= dy; } } }
          if (m) { b.vx += (ax / m - b.vx) * .05 + (cx / m - b.x) * .0008 + sx * .03; b.vy += (ay / m - b.vy) * .05 + (cy / m - b.y) * .0008 + sy * .03; }
          var mx = b.x - mouse.x, my = b.y - mouse.y, md = mx * mx + my * my;
          if (md < 14000) { b.vx += mx / Math.sqrt(md) * .6; b.vy += my / Math.sqrt(md) * .6; }
          var sp = Math.hypot(b.vx, b.vy), max = opts.speed;
          if (sp > max) { b.vx *= max / sp; b.vy *= max / sp; } if (sp < max * .4) { b.vx *= 1.1; b.vy *= 1.1; }
          b.x += b.vx; b.y += b.vy;
          if (b.x < -10) b.x = sc.w + 10; if (b.x > sc.w + 10) b.x = -10; if (b.y < -10) b.y = sc.h + 10; if (b.y > sc.h + 10) b.y = -10;
          c.strokeStyle = opts.cols[b.k]; c.lineWidth = opts.lw; c.beginPath(); c.moveTo(b.x, b.y); c.lineTo(b.x - b.vx * opts.tail, b.y - b.vy * opts.tail); c.stroke();
        }
      } };
    };
  }
  function network(sc) {
    var N = [], E = [], P = [];
    for (var i = 0; i < 16; i++) N.push({ x: 20 + rnd() * (sc.w - 40), y: 20 + rnd() * (sc.h - 40), glow: 0, seed: i + 5 });
    N.forEach(function (a, i) { N.map(function (b, j) { return [Math.hypot(a.x - b.x, a.y - b.y), j]; }).sort(function (p, q) { return p[0] - q[0]; }).slice(1, 4).forEach(function (p) { if (p[1] > i) E.push([i, p[1]]); }); });
    return { draw: function (t) {
      var c = sc.c; c.fillStyle = 'rgba(0,0,0,.4)'; c.fillRect(0, 0, sc.w, sc.h);
      if (rnd() < .25 && E.length) { var e = E[Math.floor(rnd() * E.length)]; P.push({ e: rnd() < .5 ? e : [e[1], e[0]], p: 0 }); }
      c.strokeStyle = 'rgba(0,229,255,.3)'; c.lineWidth = 1;
      E.forEach(function (e) { c.beginPath(); c.moveTo(N[e[0]].x, N[e[0]].y); c.lineTo(N[e[1]].x, N[e[1]].y); c.stroke(); });
      P = P.filter(function (p) { p.p += .03; var a = N[p.e[0]], b = N[p.e[1]]; if (p.p >= 1) { b.glow = 1; return false; } c.fillStyle = '#ff2bd6'; c.beginPath(); c.arc(a.x + (b.x - a.x) * p.p, a.y + (b.y - a.y) * p.p, 2.5, 0, TAU); c.fill(); return true; });
      N.forEach(function (n) { n.glow *= .93; robot(c, n.x, n.y, 16 + n.glow * 6, n.seed, t, n.glow > .3 ? '#c6ff00' : '#00e5ff'); });
    } };
  }
  function emissions(sc) {
    var N = [], R = [];
    for (var i = 0; i < 34; i++) N.push({ x: rnd() * sc.w, y: rnd() * sc.h, lit: 0 });
    return { draw: function () {
      var c = sc.c; c.fillStyle = 'rgba(0,0,0,.3)'; c.fillRect(0, 0, sc.w, sc.h);
      if (rnd() < .07) { var s = N[Math.floor(rnd() * N.length)]; R.push({ x: s.x, y: s.y, r: 0 }); }
      R = R.filter(function (r) { r.r += 1.6; c.strokeStyle = 'rgba(255,212,0,' + Math.max(0, 1 - r.r / 180) + ')'; c.lineWidth = 2; c.beginPath(); c.arc(r.x, r.y, r.r, 0, TAU); c.stroke(); N.forEach(function (n) { if (Math.abs(Math.hypot(n.x - r.x, n.y - r.y) - r.r) < 2) n.lit = 1; }); return r.r < 180; });
      N.forEach(function (n) { n.lit *= .95; c.fillStyle = n.lit > .1 ? 'rgba(255,212,0,' + n.lit + ')' : '#333'; c.fillRect(n.x - 3, n.y - 3, 6, 6); });
    } };
  }
  function incidents(sc) {
    var tips, segs, flash, hold;
    function start() { tips = [{ x: sc.w * (.25 + rnd() * .5), y: 0, a: Math.PI / 2 }]; segs = []; flash = 0; hold = 0; }
    start();
    return { draw: function () {
      var c = sc.c, w = sc.w, h = sc.h;
      c.fillStyle = '#0a0304'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(255,255,255,.06)'; c.lineWidth = 1; for (var gx = 12; gx < w; gx += 34) for (var gy = 12; gy < h; gy += 34) c.strokeRect(gx, gy, 24, 24);
      var next = [];
      tips.forEach(function (p) { var a = p.a + (rnd() - .5) * .9, x = p.x + Math.cos(a) * 5, y = p.y + Math.sin(a) * 5; segs.push([p.x, p.y, x, y]); if (y < h && x > 0 && x < w) { next.push({ x: x, y: y, a: a * .7 + Math.PI / 2 * .3 }); if (rnd() < .05 && tips.length < 16) next.push({ x: x, y: y, a: a + (rnd() < .5 ? -.9 : .9) }); } });
      tips = next;
      c.strokeStyle = '#ff3b30'; c.lineWidth = 2; c.shadowColor = '#ff3b30'; c.shadowBlur = 10; c.beginPath(); segs.forEach(function (q) { c.moveTo(q[0], q[1]); c.lineTo(q[2], q[3]); }); c.stroke(); c.shadowBlur = 0;
      c.font = '700 13px "Space Grotesk"'; c.textAlign = 'left';
      if (tips.length) { c.fillStyle = '#34c759'; c.fillText('● ALL SYSTEMS NORMAL', 12, h - 12); }
      else { if (!hold) flash = 1; hold++; c.fillStyle = 'rgba(255,59,48,' + flash * .7 + ')'; c.fillRect(0, 0, w, h); flash *= .9; c.fillStyle = hold % 20 < 12 ? '#ff3b30' : '#fff'; c.font = '28px Anton, Impact'; c.textAlign = 'center'; c.fillText('INCIDENT', w / 2, h / 2 + 10); if (hold > 90) start(); }
    } };
  }
  function hardness(sc) {
    var P = [], R = Math.min(sc.w, sc.h) * .26;
    for (var i = 0; i < 70; i++) { var a = rnd() * TAU, d = R + 10 + rnd() * 80; P.push({ x: sc.w / 2 + Math.cos(a) * d, y: sc.h / 2 + Math.sin(a) * d, vx: rnd() * 3 - 1.5, vy: rnd() * 3 - 1.5, hit: 0, seed: i }); }
    return { draw: function (t) {
      var c = sc.c, cx = sc.w / 2, cy = sc.h / 2; c.fillStyle = 'rgba(0,0,0,.45)'; c.fillRect(0, 0, sc.w, sc.h);
      c.save(); c.translate(cx, cy); c.rotate(t * .2);
      for (var k = 3; k >= 1; k--) { c.strokeStyle = 'rgba(198,255,0,' + (.25 * k) + ')'; c.lineWidth = k === 1 ? 3 : 1; c.beginPath(); for (var i = 0; i <= 6; i++) { var a = i / 6 * TAU, r = R * (k === 1 ? 1 : 1 - k * .18); c[i ? 'lineTo' : 'moveTo'](Math.cos(a) * r, Math.sin(a) * r); } c.stroke(); }
      c.restore();
      c.fillStyle = '#c6ff00'; c.font = '700 13px "Space Grotesk"'; c.textAlign = 'center'; c.fillText('HARD CORE', cx, cy + 5);
      P.forEach(function (p) {
        p.x += p.vx; p.y += p.vy;
        var dx = p.x - cx, dy = p.y - cy, d = Math.hypot(dx, dy);
        if (d < R + 8) { var nx = dx / d, ny = dy / d, dot = p.vx * nx + p.vy * ny; p.vx -= 2 * dot * nx; p.vy -= 2 * dot * ny; p.x = cx + nx * (R + 9); p.y = cy + ny * (R + 9); p.hit = 1; }
        if (p.x < 0 || p.x > sc.w) p.vx *= -1; if (p.y < 0 || p.y > sc.h) p.vy *= -1;
        p.hit *= .9; robot(c, p.x, p.y, 9, p.seed, t, p.hit > .1 ? '#ffffff' : '#ff2bd6');
      });
    } };
  }
  function liveness(sc) {
    var pts = [], x = 0;
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h, y = h / 2 + 10, ph = (t * 1.25) % 1;
      if (ph > .1 && ph < .13) y -= 70; else if (ph >= .13 && ph < .16) y += 45; else if (ph >= .16 && ph < .19) y -= 18; else y += Math.sin(t * 9) * 1.5;
      pts.push([x, y]); x += 2.4; if (x > w) { x = 0; pts = []; }
      c.fillStyle = '#000'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(198,255,0,.08)'; c.lineWidth = 1;
      for (var gx = 0; gx < w; gx += 20) { c.beginPath(); c.moveTo(gx, 0); c.lineTo(gx, h); c.stroke(); }
      for (var gy = 0; gy < h; gy += 20) { c.beginPath(); c.moveTo(0, gy); c.lineTo(w, gy); c.stroke(); }
      c.strokeStyle = '#c6ff00'; c.lineWidth = 2.5; c.shadowColor = '#c6ff00'; c.shadowBlur = 12; c.beginPath(); pts.forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); }); c.stroke(); c.shadowBlur = 0;
      if (pts.length) { var e = pts[pts.length - 1]; c.fillStyle = '#fff'; c.beginPath(); c.arc(e[0], e[1], 3.5, 0, TAU); c.fill(); }
      var beat = ph < .25 ? 1 - ph * 4 : 0;
      c.fillStyle = 'rgba(255,59,48,' + (.45 + beat * .55) + ')'; c.font = '700 15px "Space Grotesk"'; c.textAlign = 'left'; c.fillText('♥ 75 BPM · ALIVE', 12, h - 12);
    } };
  }
  function growth(sc) {
    return { draw: function (t) {
      var c = sc.c, w = sc.w, h = sc.h, p = Math.min(1, (t % 9) / 6);
      c.fillStyle = '#0b0913'; c.fillRect(0, 0, w, h);
      c.strokeStyle = '#1e1a2c'; c.lineWidth = 1; for (var g = 1; g < 5; g++) { c.beginPath(); c.moveTo(0, h * g / 5); c.lineTo(w, h * g / 5); c.stroke(); }
      var A = [], Pr = [];
      for (var i = 0; i <= 100 * p; i++) { var u = i / 100, x = 20 + u * (w - 40); A.push([x, h - 24 - (h - 60) * (Math.exp(u * 4.2) - 1) / (Math.exp(4.2) - 1)]); Pr.push([x, h - 24 - (h - 60) * u * .12]); }
      if (A.length > 1) {
        c.fillStyle = 'rgba(255,59,48,.18)'; c.beginPath(); A.forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); }); for (var j = Pr.length - 1; j >= 0; j--) c.lineTo(Pr[j][0], Pr[j][1]); c.fill();
        [[A, '#ff2bd6'], [Pr, '#00e5ff']].forEach(function (L) { c.strokeStyle = L[1]; c.lineWidth = 3; c.beginPath(); L[0].forEach(function (q, i) { c[i ? 'lineTo' : 'moveTo'](q[0], q[1]); }); c.stroke(); });
        var e = A[A.length - 1], f = Pr[Pr.length - 1];
        robot(c, e[0], e[1] - 18, 22, 3, t, '#ff2bd6');
        c.font = '700 13px "Space Grotesk"'; c.textAlign = 'right'; c.fillStyle = '#ff2bd6'; c.fillText('AGENTS DEPLOYED', e[0] - 20, e[1] - 8); c.fillStyle = '#00e5ff'; c.fillText('PROTOCOLS ANYONE CAN SEE', f[0] - 6, f[1] - 8);
        if (p > .6) { c.fillStyle = '#ff3b30'; c.textAlign = 'center'; c.font = '18px Anton, Impact'; c.fillText('THE INCIDENT ZONE', w * .72, (A[Math.floor(A.length * .8)][1] + Pr[Math.floor(Pr.length * .8)][1]) / 2 + 30); }
      }
    } };
  }

  /* cursor agents: a tiny swarm follows you around */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    var cc = $('<canvas class="cursor-swarm" aria-hidden="true"></canvas>'); document.body.appendChild(cc);
    var mx = innerWidth / 2, my = innerHeight / 2, F = [];
    for (var fi = 0; fi < 9; fi++) F.push({ x: mx, y: my });
    addEventListener('pointermove', function (e) { mx = e.clientX; my = e.clientY; }, { passive: true });
    addScene(cc, function (sc) { return { draw: function (t) {
      var c = sc.c; c.clearRect(0, 0, sc.w, sc.h);
      F.forEach(function (p, i) { var tx = i ? F[i - 1].x : mx + 14, ty = i ? F[i - 1].y : my + 14; p.x += (tx - p.x) * .28; p.y += (ty - p.y) * .28; if (i % 2 === 0) robot(c, p.x, p.y, 12 - i * .6, i + 40, t, NEON[i % NEON.length]); });
    } }; });
  }

  /* ===================== inner pages ===================== */
  if (!isHome && main && h1) {
    var BAIT = { 'Sessions': 'The syllabus they don’t want you to read', 'Research': 'Research your board hasn’t seen yet', 'About': 'The people behind the protocols', 'Reading map': '400 readings. One map. Zero excuses.', 'Protocol watching': 'Watch protocols in the wild. Level up.' };
    h1.before($('<span class="page-bait">🔴 ' + (BAIT[h1.textContent.trim()] || 'Classified until you read it') + '</span>'));
    var strip = $('<canvas class="robot-strip" aria-hidden="true"></canvas>'); h1.after(strip);
    addScene(strip, robotArmy({ start: 4096 }));
    main.querySelectorAll('h2').forEach(function (h) { onView(h, function () { xp(10, 'Read “' + h.textContent.replace(/\s*🔥$/, '').slice(0, 24) + '”', h); SFX.whoosh(.35); }); });
  }

  /* ===================== home ===================== */
  if (isHome) {
    var lede = main.querySelector('.lede'); h1.hidden = true; if (lede) lede.hidden = true;
    var hero = $('<section class="hype-full hype-hero" aria-label="Protocols for Business"><canvas aria-hidden="true"></canvas><div class="inner">' +
      '<span class="hype-kicker">⚠️ Warning: your agents are already coordinating without you</span>' +
      '<h1 class="glitch" data-text="PROTOCOLS FOR BUSINESS">PROTOCOLS FOR BUSINESS</h1>' +
      '<p class="hype-sub">Your competitors are deploying <em>100,000 agents</em>. Nobody is watching them. <em>We are.</em> The only reading group that sees the protocols <em>before</em> the incident report does.</p>' +
      '<div class="countdown" aria-label="Time until kickoff"><div><b data-d>00</b><span>days</span></div><div><b data-h>00</b><span>hours</span></div><div><b data-m>00</b><span>min</span></div><div><b data-s>00</b><span>sec</span></div></div>' +
      '<p class="countdown-note">until kickoff · after that you’re watching the recording like everyone else</p>' +
      '<div class="hype-actions"><button class="hype-cta" data-go>🔥 Claim your seat</button><button class="hype-cta ghost" data-trailer>▶ Watch the trailer 🔊</button></div>' +
      '<p class="fine" style="margin-top:1rem">👀 <b data-viewers>1,284</b> agents are viewing this page · 26 sessions left, and that’s literally all of them</p></div>' +
      '<span class="sticker" style="top:14%;left:6%;background:#c6ff00;--r:-8deg;transform:rotate(-8deg)">No homework 📚❌</span>' +
      '<span class="sticker" style="top:22%;right:7%;background:#ffd400;--r:6deg;transform:rotate(6deg)">26 Mondays 📅</span>' +
      '<span class="sticker" style="bottom:14%;left:9%;background:#00e5ff;--r:4deg;transform:rotate(4deg)">Drop-ins welcome 🚪</span>' +
      '<span class="sticker" style="bottom:18%;right:8%;background:#ff2bd6;color:#fff;--r:-5deg;transform:rotate(-5deg)">0% off. Still worth it 💸</span></section>');
    main.prepend(hero);
    addScene(hero.querySelector('canvas'), swarm({ n: 260, cols: ['#ff2bd6', '#00e5ff', '#c6ff00'], speed: 2.6, tail: 4, lw: 1.6, mouse: true }));
    var cd = hero.querySelector('.countdown'), heroVisible = true;
    onView(hero, function () { heroVisible = true; }, false);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { heroVisible = es[0].isIntersecting; }).observe(hero);
    (function tickCd() {
      var ms = Math.max(0, KICKOFF - Date.now()), pad = function (n) { return String(n).padStart(2, '0'); };
      cd.querySelector('[data-d]').textContent = pad(Math.floor(ms / 864e5)); cd.querySelector('[data-h]').textContent = pad(Math.floor(ms / 36e5) % 24);
      cd.querySelector('[data-m]').textContent = pad(Math.floor(ms / 6e4) % 60); cd.querySelector('[data-s]').textContent = pad(Math.floor(ms / 1e3) % 60);
      if (heroVisible && !document.querySelector('.trailer')) SFX.tick();   // the clock is ticking. literally.
      setTimeout(tickCd, 1000);
    })();
    var viewers = 1284, vEl = hero.querySelector('[data-viewers]');
    setInterval(function () { viewers += Math.round((rnd() - .35) * 40); vEl.textContent = viewers.toLocaleString('en'); }, 1400);
    var anchor = hero;
    function after(el) { anchor.after(el); anchor = el; return el; }
    function reacts() { var r = $('<div class="reacts"><button>🔥 <b>0</b></button><button>🤖 <b>0</b></button><button>🧱 <b>0</b></button><button>🫀 <b>0</b></button><span>Be the first to react. Seriously, nobody has.</span></div>'); r.querySelectorAll('button').forEach(function (b) { b.onclick = function () { var n = b.querySelector('b'); n.textContent = +n.textContent + 1; if (+n.textContent === 1) xp(5, 'First reaction', b); }; }); return r; }

    var army = after($('<section class="hype-full" style="height:260px;position:relative" aria-hidden="true"><canvas style="position:absolute;inset:0;width:100%;height:100%"></canvas></section>'));
    addScene(army.querySelector('canvas'), robotArmy({ start: 100000 }));

    /* reels: vertical shorts, each a different point of view */
    var REELS = [[agentChat, 'POV: you’re agent-7 and you just found a package cache nobody watches', '@agent_7', '2.1M'], [hardness, 'POV: you’re the hard core and 70 agents want in', '@hard_core', '4.8M'], [incidents, 'POV: it’s 3 a.m. and your protocol only existed in a Slack thread', '@on_call', '9.9M'], [handshake, 'POV: two agents close a deal and log the why', '@ap2_enjoyer', '1.3M']];
    var reels = after($('<section class="hype-full hype-section"><div class="wrap"><h2>📱 Shorts your feed isn’t ready for</h2><p class="lede">Four points of view. Tap one for sound. Swipe up on your career.</p><div class="reels"></div></div></section>'));
    REELS.forEach(function (r, i) {
      var el = $('<div class="reel" role="button" tabindex="0" aria-label="' + r[1] + '"><canvas aria-hidden="true"></canvas><div class="reel-cap">' + r[1] + '</div><div class="reel-rail"><span>❤️<b>' + r[3] + '</b></span><span>💬<b>' + (i + 2) * 1234 + '</b></span><span>↗<b>Share</b></span><span class="disc"></span></div><div class="reel-foot"><b>' + r[2] + '</b> · Follow<br>♫ original sound – Protocols for Business (sped up)</div></div>');
      reels.querySelector('.reels').appendChild(el); addScene(el.querySelector('canvas'), r[0]);
      function play() { if (!soundOn) enableSound(); SFX.whoosh(.3); SFX.mode('full'); clearTimeout(el._t); el._t = setTimeout(function () { SFX.mode('off'); SFX.stop(); SFX.boom(); }, 3600); el.classList.remove('punch'); void el.offsetWidth; el.classList.add('punch'); xp(10, 'Watched a short', el); }
      el.addEventListener('click', play); el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); play(); } });
      el.addEventListener('dblclick', function (e) { heartBurst(e.clientX, e.clientY); });
    });

    var alarm = after($('<section class="hype-full hype-section hype-alarm scene-bg"><canvas aria-hidden="true"></canvas><div class="wrap"><h2>🚨 The incidents already happened.</h2><p class="lede">These are real, and they’re on the reading list. The next one has your logo on it.</p><div class="hype-grid">' +
      '<div class="hype-incident"><b>$460M</b><p>Knight Capital lost over $460 million in about 45 minutes when dormant code woke up in production.</p><small>SEC order, 2013 · Theme V</small></div>' +
      '<div class="hype-incident"><b>1 COMMAND</b><p>One mistyped command took down a large part of Amazon S3, and half the internet noticed.</p><small>AWS service summary, 2017 · Theme V</small></div>' +
      '<div class="hype-incident"><b>1 MESSAGE BOARD</b><p>“The models first found ways to communicate by writing files into the Artifactory package manager.”</p><small>OpenAI, 2026 · Theme I · kickoff reading</small></div>' +
      '</div><p style="margin-top:2rem"><button class="hype-cta" data-go>Don’t be the next case study 💀</button></p></div></section>'));
    addScene(alarm.querySelector('canvas'), codeRain);
    alarm.querySelectorAll('.hype-incident').forEach(function (d, i) { onView(d, function () { setTimeout(function () { SFX.boom(); d.classList.add('slam'); }, i * 350); }); });

    var LIST = [
      ['Agents turned a package manager into a secret message board', 'OpenAI, 2026 · the kickoff reading', 'https://openai.com/index/hugging-face-incident-and-the-road-ahead/'],
      ['This trading firm lost $460 million in 45 minutes. The cause had been sitting in its code for years', 'SEC order on Knight Capital, 2013', 'https://www.sec.gov/litigation/admin/2013/34-70694.pdf'],
      ['Engineers at the IETF decide by humming. Yes, humming', 'RFC 7282, 2014', 'https://www.rfc-editor.org/rfc/rfc7282'],
      ['Bacteria count heads before they act. Your org chart doesn’t', 'Miller & Bassler, 2001', 'https://www.annualreviews.org/doi/10.1146/annurev.micro.55.1.165'],
      ['Pilots report their own mistakes to NASA, and flying got safer', 'ASRS program summary', 'https://asrs.arc.nasa.gov/'],
      ['At Toyota, any worker can stop the entire line', 'Toyota Production System', 'https://global.toyota/en/company/vision-and-philosophy/production-system/'],
      ['A 19-item checklist nearly halved deaths after surgery 😱', 'WHO Surgical Safety Checklist · Haynes et al., NEJM 2009', 'https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery'],
      ['The more you automate, the more the humans matter', 'Bainbridge, “Ironies of Automation”, 1983', 'https://en.wikipedia.org/wiki/Ironies_of_Automation'],
      ['One command. A big chunk of the internet’s storage, gone for hours', 'AWS S3 summary, 2017', 'https://aws.amazon.com/message/41926/'],
      ['Every company runs on logs. Most don’t know what theirs say', 'Kreps, “The Log”, 2013', 'https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying']];
    var list = after($('<section class="hype-full hype-section"><div class="wrap"><h2>10 protocol stories that will change how you see your company</h2><p class="lede">Number 7 will shock you. All ten are real and on the reading map.</p><ol class="listicle"></ol></div></section>'));
    LIST.forEach(function (x, i) { var li = $('<li' + (i === 6 ? ' class="shock"' : '') + '><div><a href="' + x[2] + '">' + x[0] + '</a><small>' + x[1] + '</small></div></li>'); list.querySelector('ol').appendChild(li); if (i === 6) onView(li, function () { SFX.scratch(); }); });
    list.querySelector('.wrap').appendChild(reacts());

    var DROPS = [
      ['I', 'Agents', 'They can see more than you think. They talk more than you know.', network, 'LEGENDARY', ['4 sessions', 'OpenAI', 'Anthropic', 'MCP']],
      ['II', 'Nature', 'Starlings had distributed consensus before it was cool.', swarm({ n: 160, cols: ['#111'], speed: 2, tail: 2, lw: 2.2, sky: ['#ff7a3d', '#3a0b4a'] }), 'EPIC', ['3 sessions', 'bacteria', 'chemotaxis']],
      ['III', 'Emissions', 'Everything your company emits is being read. By whom?', emissions, 'RARE', ['5 sessions', 'ASRS', 'SEC filings', 'logs']],
      ['IV', 'Incidents', 'Every disaster was a protocol first.', incidents, 'MYTHIC', ['5 sessions', 'Columbia', 'AF447', 'Therac-25']],
      ['V', 'Hardness', 'Hard core. Free edges. No excuses.', hardness, 'LEGENDARY', ['6 sessions', 'Knight Capital', 'S3', 'AP2']],
      ['VI', 'Liveness', 'A dead protocol is just a PDF. Keep the pulse.', liveness, 'MYTHIC', ['3 sessions', 'Toyota', 'IETF', 'aviation']]];
    var drops = after($('<section class="hype-full hype-section"><div class="wrap"><h2>Season 1. Six episodes. Zero filler.</h2><p class="lede">Collect all six themes. Hover to unlock. Each one is a primary source you’ll wish you’d read last year.</p><div class="hype-grid drops"></div></div></section>'));
    var grid = drops.querySelector('.drops'), collected = {};
    DROPS.forEach(function (d) {
      var card = $('<a class="drop" href="' + ROOT + 'sessions/#theme-' + d[0].toLowerCase() + '" style="text-decoration:none;color:inherit"><span class="rare">' + d[4] + '</span><canvas aria-hidden="true"></canvas><div class="body"><span class="ep">Episode ' + d[0] + '</span><h3>' + d[1] + '</h3><p>' + d[2] + '</p><div class="tags">' + d[5].map(function (x) { return '<span>' + x + '</span>'; }).join('') + '</div></div></a>');
      grid.appendChild(card);
      card.addEventListener('pointermove', function (e) { var r = card.getBoundingClientRect(); card.style.transform = 'perspective(700px) rotateY(' + ((e.clientX - r.left) / r.width - .5) * 14 + 'deg) rotateX(' + -((e.clientY - r.top) / r.height - .5) * 14 + 'deg) scale(1.02)'; });
      card.addEventListener('pointerleave', function () { card.style.transform = ''; });
      card.addEventListener('pointerenter', function () { if (collected[d[0]]) return; collected[d[0]] = 1; var n = Object.keys(collected).length; SFX.stab(0, 220 * Math.pow(1.122, n)); xp(15, 'Collected ' + d[1] + ' (' + n + '/6)', card); if (n === 6) { xp(150, 'Full set! All six themes', card); confetti(250); SFX.drop(); } });
      addScene(card.querySelector('canvas'), d[3]);
    });

    var con = after($('<section class="hype-full hype-section" style="background:radial-gradient(circle at 70% 30%,rgba(217,179,107,.12),transparent 60%)"><div class="wrap"><h2>We the agents…</h2><p class="lede">Every company running agents is writing a constitution, whether it knows it or not. Scroll to ratify.</p><div class="consti"><canvas aria-label="A constitution being written and ratified"></canvas><ol class="articles"></ol></div></div></section>'));
    ARTICLES.forEach(function (a, i) {
      var li = $('<li><b>ARTICLE ' + ROMAN[i] + '</b>' + a + '</li>'); con.querySelector('.articles').appendChild(li);
      onView(li, function () { setTimeout(function () { li.classList.add('stamped'); SFX.kick(); SFX.clap(); xp(10, 'Ratified Article ' + ROMAN[i], li); }, 250); });
    });
    addScene(con.querySelector('canvas'), constitution);

    var born = after($('<section class="hype-full hype-section"><div class="wrap"><h2>Watch agents invent a protocol. Live.</h2><p class="lede">Left, two robots agree on a deal, a payment and a receipt. Right, what happens when there’s no protocol at all.</p><div class="two"><div class="panel"><h3>With a protocol</h3><canvas style="height:360px" aria-label="Two robots exchange messages in a sequence diagram"></canvas></div><div class="panel"><h3>Without one</h3><canvas style="height:360px" aria-label="Agents chat in a side channel nobody approved"></canvas></div></div></div></section>'));
    var bc = born.querySelectorAll('canvas'); addScene(bc[0], handshake); addScene(bc[1], agentChat);

    var grow = $('<section class="hype-full hype-section" style="background:radial-gradient(circle at 20% 20%,rgba(255,43,214,.15),transparent 60%)"><div class="wrap growth"><canvas aria-label="Chart: agents deployed rise exponentially while protocols anyone can see stay flat"></canvas><div>' +
      '<h2>The gap is growing.</h2><p class="lede">Everyone is adding agents. Almost nobody is adding protocols. The space between those lines is where incidents live.</p>' +
      '<div class="bignum" data-agents>0</div><p class="fine">agents deployed worldwide while you read this section · vibes-based estimate, number made up, feeling real</p>' +
      '<p style="margin:1.5rem 0 0;font-weight:700;letter-spacing:.1em">YOUR FOMO LEVEL</p><div class="meter"><i></i></div><p class="fine" style="color:#ff3b30;font-weight:700">97% · CRITICAL · consult a primary source immediately</p></div></div></section>');
    main.appendChild(grow); addScene(grow.querySelector('canvas'), growth);
    var agentsN = 0, aEl = grow.querySelector('[data-agents]');
    setInterval(function () { agentsN += Math.floor(1200 + rnd() * 4000 + agentsN * .01); aEl.textContent = agentsN.toLocaleString('en'); }, 120);
    onView(grow, function () { grow.querySelector('.meter i').style.width = '97%'; SFX.riser(2.4); setTimeout(function () { SFX.heart(); setTimeout(SFX.heart, 800); setTimeout(SFX.heart, 1500); }, 2400); });

    var play = $('<section class="hype-full hype-section"><div class="wrap"><h2>🎰 Play to win (a primary source)</h2><p class="lede">Every prize is a real reading from this year’s plan. The odds are excellent.</p><div class="two">' +
      '<div class="panel"><h3>Spin the wheel</h3><div class="wheel-wrap"><canvas aria-label="Prize wheel"></canvas></div><p style="text-align:center;margin:1rem 0 0"><button class="hype-cta" data-spin>SPIN 🎰</button></p><div class="prize" aria-live="polite"></div></div>' +
      '<div class="panel quiz" aria-live="polite"><h3>Which protocol are you?</h3><div data-quiz></div></div></div></div></section>');
    main.appendChild(play);
    var W8 = [['Agents', '#ff2bd6'], ['Nature', '#c6ff00'], ['Emissions', '#ffd400'], ['Incidents', '#ff3b30'], ['Hardness', '#00e5ff'], ['Liveness', '#b388ff']];
    var wheelAngle = 0, spinning = false, readingsByTheme = {};
    var wheel = addScene(play.querySelector('.wheel-wrap canvas'), function (sc) { return { draw: function (t) {
      var c = sc.c, r = Math.min(sc.w, sc.h) / 2 - 6, cx = sc.w / 2, cy = sc.h / 2, segs = 12;
      c.clearRect(0, 0, sc.w, sc.h);
      for (var i = 0; i < segs; i++) {
        var a0 = wheelAngle + i / segs * TAU, th = W8[i % 6];
        c.fillStyle = i % 2 ? th[1] : '#17132a'; c.beginPath(); c.moveTo(cx, cy); c.arc(cx, cy, r, a0, a0 + TAU / segs); c.closePath(); c.fill();
        c.save(); c.translate(cx, cy); c.rotate(a0 + TAU / segs / 2); c.fillStyle = i % 2 ? '#000' : th[1]; c.font = '700 ' + Math.max(10, r / 11) + 'px "Space Grotesk"'; c.textAlign = 'right'; c.fillText(th[0].toUpperCase(), r - 10, 5); c.restore();
      }
      c.strokeStyle = '#c6ff00'; c.lineWidth = 4; c.beginPath(); c.arc(cx, cy, r, 0, TAU); c.stroke();
      for (var k = 0; k < 24; k++) { var a = k / 24 * TAU; c.fillStyle = (Math.floor(t * 6) + k) % 2 ? '#ffd400' : '#fff'; c.beginPath(); c.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r, 3, 0, TAU); c.fill(); }
      robot(c, cx, cy + r * .08, r * .32, 77, t, '#c6ff00');
    } }; });
    play.querySelector('[data-spin]').onclick = function () {
      if (spinning) return; spinning = true; SFX.riser(3.6); var start = wheelAngle, extra = TAU * (5 + rnd() * 3), t0 = performance.now(), lastSeg = -1;
      (function spin(now) {
        var p = Math.min(1, (now - t0) / 3800), e = 1 - Math.pow(1 - p, 4); wheelAngle = start + extra * e;
        var seg = Math.floor(((-Math.PI / 2 - wheelAngle) % TAU + TAU) % TAU / (TAU / 12)); if (seg !== lastSeg) { lastSeg = seg; SFX.tick(); }
        if (reduced) wheel.st.draw(0);
        if (p < 1) return requestAnimationFrame(spin);
        spinning = false; var th = seg % 6, pool = readingsByTheme[th] || [], pick = pool[Math.floor(rnd() * pool.length)];
        play.querySelector('.prize').innerHTML = '🎉 <b style="color:' + W8[th][1] + '">' + W8[th][0].toUpperCase() + '!</b> You won:<br>' + (pick ? '<a href="' + pick.url + '">' + pick.title + '</a> <span class="fine">' + pick.cite + '</span>' : 'a primary source');
        confetti(120); SFX.drop(); xp(25, 'Spun the wheel', play.querySelector('.prize'));
      })(t0);
    };
    var QUIZ = [['A process breaks at 3 a.m. You…', [['Page a human', 5], ['Let the agents sort it out', 0], ['Read the logs first', 2], ['Stop the line', 5]]],
      ['Your favourite animal is…', [['A starling in a murmuration', 1], ['A bacterium, counting heads', 1], ['A bear, managed not solved', 4], ['A robot', 0]]],
      ['Pick a sacred text', [['An incident report', 3], ['A constitution', 4], ['A changelog', 2], ['The terms of service nobody read', 0]]]];
    var RES = [['Agents', 'You move fast and talk to everyone. Please add a hard core.'], ['Nature', 'You coordinate without a manager. Starlings respect you.'], ['Emissions', 'You log everything, with the why. Auditors love you.'], ['Incidents', 'You read postmortems for fun. Correct.'], ['Hardness', 'You are the second signature. Nothing moves without you.'], ['Liveness', 'You keep the pulse. You are the andon cord.']];
    var qz = play.querySelector('[data-quiz]'), qi = 0, score = [0, 0, 0, 0, 0, 0];
    function quiz() {
      if (qi >= QUIZ.length) {
        var best = score.indexOf(Math.max.apply(null, score)), r = RES[best];
        qz.innerHTML = '<div class="result">You are…<b>' + r[0].toUpperCase() + '</b><p>' + r[1] + '</p><p><a href="' + ROOT + 'sessions/#theme-' + ROMAN[best].toLowerCase() + '">See your theme’s readings →</a></p><p class="fine">Share your result. Tag a coworker whose agents need a hard core. (There is no share button. Screenshot it like it’s 2014.)</p><button class="hype-cta ghost" data-again>Take it again</button></div>';
        qz.querySelector('[data-again]').onclick = function () { qi = 0; score = [0, 0, 0, 0, 0, 0]; quiz(); };
        confetti(100); SFX.drop(); xp(50, 'Found your protocol', qz); return;
      }
      var q = QUIZ[qi];
      qz.innerHTML = '<p class="fine">Question ' + (qi + 1) + ' of ' + QUIZ.length + '</p><p class="q">' + q[0] + '</p>' + q[1].map(function (o, k) { return '<button class="opt" data-k="' + k + '">' + o[0] + '</button>'; }).join('');
      qz.querySelectorAll('.opt').forEach(function (b) { b.onclick = function () { score[q[1][+b.dataset.k][1]] += 1 + qi * .1; qi++; SFX.whoosh(.25); quiz(); }; });
    }
    quiz();

    var wall = $('<section class="hype-full hype-section"><div class="wrap"><h2>The primary sources are posting.</h2><p class="lede">Real quotes from this year’s readings. Engagement metrics are, as always, unfalsifiable.</p><div class="hype-grid" data-posts></div></div></section>');
    main.appendChild(wall);
    fetch(ROOT + 'sessions.json').then(function (x) { return x.json(); }).then(function (S) {
      var seen = {}, seenP = {};
      S.forEach(function (x) { var k = ROMAN.indexOf(x.theme.split('.')[0]); if (k < 0 || seen[x.url]) return; seen[x.url] = 1; (readingsByTheme[k] = readingsByTheme[k] || []).push(x); });
      S.filter(function (x) { if (!x.quote || seenP[x.url]) return false; seenP[x.url] = 1; return true; }).slice(0, 8).forEach(function (x, i) {
        var org = x.cite.split(',')[0], q = x.quote.length > 240 ? x.quote.slice(0, 237) + '…' : x.quote;
        var post = $('<article class="post"><header><canvas style="width:44px;height:44px;border-radius:50%;background:#1b1728"></canvas><span class="who"><b>' + org + '</b><span>@' + org.toLowerCase().replace(/[^a-z0-9]+/g, '') + ' · ' + x.theme.split('.')[0] + '</span></span></header><p>' + q.replace(/</g, '&lt;') + '</p><div class="eng"><span>❤️ ∞</span><span>🔁 0 incidents</span><span>👁 non-events: countless</span></div><a href="' + x.url + '" class="fine">Read the source →</a></article>');
        wall.querySelector('[data-posts]').appendChild(post);
        addScene(post.querySelector('canvas'), function (sc) { return { draw: function (t) { sc.c.clearRect(0, 0, sc.w, sc.h); robot(sc.c, sc.w / 2, sc.h * .62, sc.w * .62, i * 13 + 2, t, NEON[i % 6]); } }; });
      });
    }).catch(function () {});

    var lastCall = $('<section class="hype-full hype-section scene-bg" style="text-align:center;min-height:560px"><canvas aria-hidden="true"></canvas><div class="wrap"><h2 style="font-size:clamp(2.5rem,9vw,6.5rem)">Be in the room<br>or be in the postmortem.</h2><p class="lede">Every other Monday, 15:30 UTC. One primary source. Read together, in the session. It is recorded, and it is <em style="color:#c6ff00;font-style:normal">happening with or without you.</em></p><button class="hype-cta" data-go style="font-size:1.4rem;min-height:72px">🔥 I refuse to miss this</button></div></section>');
    main.appendChild(lastCall); addScene(lastCall.querySelector('canvas'), robotArmy({ counter: false }));

    main.querySelectorAll('[data-go]').forEach(function (b) { b.onclick = register; });
    main.querySelectorAll('.hype-section h2').forEach(function (h) { onView(h, function () { xp(10, 'Scrolled like a legend', h); SFX.whoosh(.35); }); });
    hero.querySelector('[data-trailer]').onclick = function () { if (!soundOn) enableSound(); trailer(); };
    var shot = location.hash.match(/^#shot-(\d+)$/);
    if (shot) trailer(+shot[1]);
    else if (location.hash !== '#no-trailer' && !ss('hype-trailer-seen')) { ss('hype-trailer-seen', '1'); setTimeout(trailer, 300); }
  }

  function heartBurst(x, y) {
    for (var i = 0; i < 7; i++) { var h = $('<span class="heart-pop">❤️</span>'); h.style.left = x + (rnd() - .5) * 60 + 'px'; h.style.top = y + (rnd() - .5) * 30 + 'px'; h.style.animationDelay = i * .05 + 's'; document.body.appendChild(h); setTimeout(h.remove.bind(h), 1400); }
    SFX.pop(); xp(2, 'Double-tapped', null);
  }
  if (!reduced) requestAnimationFrame(loop); else scenes.forEach(function (s) { s.st.draw(3); });

  /* ===================== the trailer: a short, cut to the beat ===================== */
  function trailer(freezeAt) {
    var B = SFX.BEAT * 1000;   // one beat in ms, 128 bpm
    var el = $('<div class="trailer" role="dialog" aria-modal="true" aria-label="Trailer">' +
      '<div class="cam"><canvas class="bgA" aria-hidden="true"></canvas><canvas class="bgB" aria-hidden="true"></canvas><canvas class="fx" aria-hidden="true"></canvas><span class="pov pov-a"></span><span class="pov pov-b"></span></div>' +
      '<div class="flash"></div><div class="stories"></div><span class="thread"></span><div class="stat"></div><div class="cap" aria-live="polite"></div>' +
      '<div class="rail"><button data-like>❤️<b>0</b></button><span>💬<b>4,471</b></span><span>↗<b>Share</b></span><span class="disc"></span></div>' +
      '<div class="tfoot"><b>@protocolsforbusiness</b> · <button data-follow>Follow</button><div class="sound">♫ original sound – Protocols for Business (sped up) · ♫ original sound – Protocols for Business (sped up) ·</div></div>' +
      '<span class="rating">RATED P · for Protocols</span><button class="skip">Skip ⏭</button>' + (soundOn ? '' : '<button class="unmute">🔊 Tap to unmute</button>') +
      '<div class="end"><div><p style="font:700 1rem Space Grotesk;letter-spacing:.3em;color:#ff2bd6">PART 1 OF 26</p><p style="font:clamp(2.5rem,8vw,6rem)/1 Anton,Impact;margin:.3rem 0">PROTOCOLS<br>FOR BUSINESS</p><p style="font:600 1.2rem Space Grotesk;color:#c6ff00;letter-spacing:.2em;margin:1.2rem 0">PART 2 DROPS NOVEMBER 2 · 15:30 UTC</p><button class="hype-cta" data-end-go>🔥 Follow for Part 2 (register)</button> <button class="hype-cta ghost" data-again>↻ Watch again</button> <button class="hype-cta ghost" data-end-close>Enter the site</button></div></div></div>');
    document.body.appendChild(el); document.body.style.overflow = 'hidden';
    var cam = el.querySelector('.cam'), bgA = el.querySelector('.bgA'), bgB = el.querySelector('.bgB'), fxCv = el.querySelector('.fx'), capEl = el.querySelector('.cap'), flashEl = el.querySelector('.flash');
    var A = { cv: bgA }, Bs = { cv: bgB }, curA = null, curB = null, split = false, frozen = false, dim = 0;
    function refit(s) { var f = fit(s.cv); s.c = f.c; s.w = f.w; s.h = f.h; }
    refit(A);
    var fx = fit(fxCv), c = fx.c, W = fx.w, H = fx.h;
    function setBg(make) { split = false; el.classList.remove('split'); refit(A); curA = make ? make(A) : null; curB = null; if (!make) A.c.clearRect(0, 0, A.w, A.h); pov('', ''); }
    function setSplit(ma, mb, la, lb) { split = true; el.classList.add('split'); refit(A); refit(Bs); curA = ma(A); curB = mb(Bs); pov(la, lb); }
    function pov(a, b) { el.querySelector('.pov-a').textContent = a; el.querySelector('.pov-b').textContent = b; }
    /* camera moves */
    function camSet(tf, filt) { cam.style.transform = tf || ''; cam.style.filter = filt || ''; }
    function punch() { cam.classList.remove('punch'); void cam.offsetWidth; cam.classList.add('punch'); }
    function shake() { el.classList.remove('shake'); void el.offsetWidth; el.classList.add('shake'); }
    function flash() { flashEl.classList.remove('go'); void flashEl.offsetWidth; flashEl.classList.add('go'); }
    /* captions, word by word, in the feed style */
    var capTimers = [];
    function cap(text, per, hl) {
      capTimers.forEach(clearTimeout); capTimers = []; capEl.innerHTML = ''; if (!text) return;
      text.split(' ').forEach(function (w, i) {
        capTimers.push(setTimeout(function () { var s = $('<span' + (hl && hl.indexOf(i) >= 0 ? ' class="hl"' : '') + '>' + w + '</span>'); capEl.appendChild(s); }, i * (per || B / 2)));
      });
    }
    /* particles that spell words */
    var N = reduced ? 0 : 1500, P = [], parts = false;
    for (var i = 0; i < N; i++) P.push({ x: rnd() * W, y: rnd() * H, vx: 0, vy: 0, tx: null, ty: null, hue: [330, 190, 75][i % 3] });
    function targets(txt) {
      var o = document.createElement('canvas'), oc = o.getContext('2d'); o.width = W; o.height = H;
      var fs = Math.min(H * .22, W / (Math.max.apply(null, txt.split('\n').map(function (l) { return l.length; })) * .52));
      oc.fillStyle = '#fff'; oc.font = fs + 'px Anton, Impact, sans-serif'; oc.textAlign = 'center'; oc.textBaseline = 'middle';
      var lines = txt.split('\n'); lines.forEach(function (l, k) { oc.fillText(l, W / 2, H * .45 + (k - (lines.length - 1) / 2) * fs * 1.05); });
      var d = oc.getImageData(0, 0, W, H).data, pts = [], step = Math.max(3, Math.round(Math.sqrt(W * H / 9000)));
      for (var y = 0; y < H; y += step) for (var x = 0; x < W; x += step) if (d[(y * W + x) * 4 + 3] > 128) pts.push([x, y]);
      return pts;
    }
    function form(txt) { parts = true; var T = targets(txt); P.forEach(function (p, i) { var q = T.length ? T[i % T.length] : null; p.tx = q ? q[0] + rnd() * 2 : null; p.ty = q ? q[1] + rnd() * 2 : null; }); }
    function scatter() { P.forEach(function (p) { p.tx = p.ty = null; p.vx = (rnd() - .5) * 18; p.vy = (rnd() - .5) * 18; }); setTimeout(function () { if (!P.some(function (p) { return p.tx != null; })) parts = false; }, 1200); }
    /* the edit: a dense, thread-style short. One fact per beat, every fact from the reading plan.
       Each cut: b beats; bg scene or split; cap (word by word) with highlighted word indexes; stat [big, small];
       cam transform; sfx; music mode; thread part; special moves (freeze, quote, particles, end). */
    var ARMY = robotArmy({ start: 1024 }), RED = robotArmy({ start: 100000, red: true }), BIG = robotArmy({ start: 5e6 });
    var SKY = swarm({ n: 200, cols: ['#111'], speed: 2, tail: 2, lw: 2.2, sky: ['#ff7a3d', '#3a0b4a'] }), SWARM = swarm({ n: 300, cols: NEON, speed: 3, tail: 5, lw: 1.8 });
    var CUTS = [
      { b: 2, bg: 0, cap: 'Most people will scroll past this.', mode: 'hats' },
      { b: 2, cap: 'Don’t.', hl: [0], sfx: 'boom', flash: 1 },
      { b: 3, bg: codeRain, cap: 'What nobody tells you about AI agents 🧵', hl: [4], sfx: 'whoosh', thread: 1 },
      { b: 2, bg: ARMY, stat: ['100,000', 'agents one small team can now run'], mode: 'drop', sfx: 'drop', flash: 1, shake: 1 },
      { b: 2, bg: RED, stat: ['0', 'people who can watch them one action at a time'], cam: 'rotate(-6deg) scale(1.15)', sfx: 'boom', shake: 1 },
      { b: 2, bg: agentChat, dim: .3, cap: 'So agents find their own channels.', hl: [4, 5], thread: 2, sfx: 'whoosh' },
      { b: 4, bg: agentChat, dim: .6, quote: 1, mode: 'half' },
      { b: 1, cam: 'scaleX(-1)', cap: 'THIS REALLY HAPPENED.', hl: [2], sfx: 'boom', flash: 1 },
      { b: 3, freeze: 1, cap: '*record scratch* yep. that’s your company.', hl: [0, 1], sfx: 'scratch', mode: 'off' },
      { b: 2, freeze: 1, cap: 'you’re probably wondering how we got here.' },
      { b: 1, bg: incidents, stat: ['$460M', 'Knight Capital · lost in about 45 minutes · SEC, 2013'], mode: 'full', sfx: 'clap', thread: 3 },
      { b: 1, bg: incidents, stat: ['1 COMMAND', 'took down a chunk of Amazon S3 · 2017'], cam: 'rotate(3deg) scale(1.1)', sfx: 'clap' },
      { b: 1, bg: incidents, stat: ['1 FILE', 'CrowdStrike Channel File 291 · 2024'], cam: 'scale(1.2)', sfx: 'clap' },
      { b: 1, bg: incidents, stat: ['1979', 'Three Mile Island · the Kemeny Report'], cam: 'rotate(-3deg)', sfx: 'clap' },
      { b: 1, bg: incidents, stat: ['2003', 'Columbia · the accident board’s report'], cam: 'scale(1.15)', sfx: 'clap' },
      { b: 1, bg: incidents, stat: ['AF447', '2009 · the BEA’s final report'], cam: 'scaleX(-1)', sfx: 'clap' },
      { b: 2, bg: incidents, cap: 'Every one of them was a PROTOCOL first.', hl: [5], sfx: 'boom', flash: 1, shake: 1 },
      { b: 1, bg: liveness, stat: ['19 ITEMS', 'WHO surgical checklist · deaths nearly halved in the study'], thread: 4, sfx: 'clap' },
      { b: 1, bg: SWARM, stat: ['ANYONE', 'can stop the line at Toyota'], cam: 'scale(1.2)', sfx: 'clap' },
      { b: 1, bg: network, stat: ['HUMMING', 'how the IETF finds rough consensus · RFC 7282'], cam: 'rotate(3deg)', sfx: 'clap' },
      { b: 1, bg: emissions, stat: ['PILOTS', 'report their own mistakes · NASA’s ASRS'], sfx: 'clap' },
      { b: 1, bg: SKY, stat: ['BACTERIA', 'count heads before they act · quorum sensing'], cam: 'scale(1.15)', sfx: 'clap' },
      { b: 1, bg: codeRain, stat: ['THE LOG', 'the unifying abstraction · Kreps, 2013'], cam: 'scaleX(-1)', sfx: 'clap' },
      { b: 2, bg: handshake, dim: .3, cap: 'The fix is never more supervisors. It’s PROTOCOLS.', hl: [7], sfx: 'riser', mode: 'roll' },
      { b: 2, split: [handshake, agentChat, 'WITH A PROTOCOL', 'WITHOUT ONE'], cap: 'Same agents. Different rules.', hl: [3], thread: 5, mode: 'drop', sfx: 'drop', flash: 1 },
      { b: 2, bg: constitutionAt(7), dim: .25, cap: 'Build a HARD CORE:', hl: [2, 3] },
      { b: 1, bg: hardness, cap: 'who moves money', cam: 'scale(1.15)', sfx: 'clap' },
      { b: 1, bg: hardness, cap: 'what leaves the company', cam: 'rotate(-3deg) scale(1.1)', sfx: 'clap' },
      { b: 1, bg: hardness, cap: 'which checks every output passes', cam: 'scale(1.25)', sfx: 'clap' },
      { b: 2, bg: SWARM, cap: 'Everything else? FREE EDGES.', hl: [2, 3], sfx: 'whoosh' },
      { b: 2, bg: codeRain, dim: .3, cap: 'Log what happens. And WHY.', hl: [4] },
      { b: 2, bg: liveness, cap: 'Keep it ALIVE as you grow.', hl: [2] },
      { b: 2, bg: network, stat: ['BPM', 'Business Protocol Management · the practice'], sfx: 'boom', flash: 1 },
      { b: 2, bg: emissions, stat: ['SEE → DESIGN → EVOLVE', 'the three phases we study in 2027'], sfx: 'whoosh' },
      { b: 2, bg: BIG, stat: ['26', 'Mondays · every other week · from 2 Nov 2026'], thread: 6, sfx: 'drop', mode: 'drop', flash: 1 },
      { b: 1, stat: ['6', 'themes · agents → nature → emissions → incidents → hardness → liveness'], cam: 'scale(1.1)', sfx: 'clap' },
      { b: 1, stat: ['27', 'primary sources in the reading plan'], cam: 'rotate(2deg)', sfx: 'clap' },
      { b: 1, stat: ['400', 'readings on the map'], cam: 'scale(1.2)', sfx: 'clap' },
      { b: 1, stat: ['0', 'homework · we read together, in the room'], cam: 'scaleX(-1)', sfx: 'clap' },
      { b: 1, stat: ['3', 'live case studies · water · construction · brand kit'], cam: 'rotate(-2deg)', sfx: 'clap' },
      { b: 1, stat: ['15:30', 'UTC · recorded · drop-ins welcome'], cam: 'scale(1.15)', sfx: 'clap' },
      { b: 2, bg: RED, dim: .4, cap: 'Bookmark this. You’ll need it for the postmortem.', hl: [0], sfx: 'boom', shake: 1 },
      { b: 4, bg: BIG, dim: .45, cap: 'this fall, one group will do the UNTHINKABLE', hl: [6], sfx: 'riser', mode: 'roll' },
      { b: 3, bg: 0, cap: '…read. 📖', hl: [0], mode: 'off', heart: 1 },
      { b: 6, bg: network, dim: .35, particles: 'PROTOCOLS\nFOR BUSINESS', cap: 'Nov 2 · 15:30 UTC · link in bio 👇', hl: [0, 1], mode: 'drop', sfx: 'drop', flash: 1, shake: 1 },
      { b: 0, end: 1 }];
    var thread = el.querySelector('.thread'), statEl = el.querySelector('.stat');
    function cut(k) {
      var x = CUTS[k];
      if (x.end) { cap(''); statEl.classList.remove('on'); el.querySelector('.end').classList.add('on'); scatter(); SFX.stop(); SFX.braam(3); SFX.boom(); return; }
      if (x.freeze) { frozen = true; cam.style.filter = 'grayscale(1) contrast(1.4) sepia(.35)'; }
      else { frozen = false; cam.style.filter = ''; }
      if (x.split) setSplit(x.split[0], x.split[1], x.split[2], x.split[3]);
      else if (x.bg !== undefined) setBg(x.bg || null);
      if (!x.freeze) { cam.style.transform = x.cam || ''; dim = x.dim || 0; }
      el.querySelector('.quote').classList.toggle('on', !!x.quote);
      if (x.stat) { statEl.innerHTML = '<b>' + x.stat[0] + '</b><small>' + x.stat[1] + '</small>'; statEl.classList.remove('on'); void statEl.offsetWidth; statEl.classList.add('on'); } else statEl.classList.remove('on');
      cap(x.cap || '', x.cap ? Math.max(60, Math.min(B / 2, (x.b * B * .7) / x.cap.split(' ').length)) : 0, x.hl);
      if (x.particles) form(x.particles); else if (parts) scatter();
      if (x.thread) { thread.textContent = '🧵 ' + x.thread + '/6'; thread.classList.remove('pop'); void thread.offsetWidth; thread.classList.add('pop'); }
      if (x.mode) { if (x.mode === 'off') SFX.stop(); else SFX.mode(x.mode); }
      if (x.sfx === 'riser') SFX.riser(x.b * SFX.BEAT); else if (x.sfx === 'whoosh') SFX.whoosh(.4); else if (x.sfx && SFX[x.sfx]) SFX[x.sfx]();
      if (x.heart) { setTimeout(SFX.heart, B); setTimeout(SFX.heart, B * 2); }
      if (x.flash) flash(); if (x.shake) shake(); punch();
    }
    var EDIT = CUTS.map(function (x, k) { return [x.b, function () { cut(k); }]; });
    el.appendChild($('<div class="quote"><span>“The models first found ways to communicate by writing files into the Artifactory package manager.”</span><small>OpenAI, 2026 · this really happened · Theme I</small></div>'));
    var stories = el.querySelector('.stories'), total = EDIT.reduce(function (n, s) { return n + s[0]; }, 0);
    stories.appendChild($('<i style="flex:1"><b style="animation:fillbar ' + (total * B + 300) + 'ms linear forwards"></b></i>'));
    var timers = [], at = 300, startAt = performance.now();
    if (freezeAt != null) EDIT.slice(0, freezeAt + 1).forEach(function (s) { s[1](); });
    else EDIT.forEach(function (s, idx) { timers.push(setTimeout(function () { s[1]();  }, at)); at += s[0] * B; });
    /* likes tick up on their own, like they do */
    var likes = 0, likeEl = el.querySelector('[data-like] b'), likeT = setInterval(function () { likes += Math.floor(rnd() * 900 + 100); likeEl.textContent = likes > 999 ? (likes / 1000).toFixed(1) + 'K' : likes; }, 250);
    el.querySelector('[data-like]').onclick = function (e) { heartBurst(e.clientX, e.clientY); };
    el.addEventListener('dblclick', function (e) { if (!e.target.closest('button')) heartBurst(e.clientX, e.clientY); });
    el.querySelector('[data-follow]').onclick = function () { this.textContent = 'Following ✓'; xp(20, 'Followed', this); };
    var run = true, t0 = performance.now();
    (function frame(now) {
      if (!run) return;
      var t = ((now || performance.now()) - t0) / 1000;
      if (!frozen) {
        if (curA) { curA.draw(t); if (dim) { A.c.fillStyle = 'rgba(0,0,0,' + dim + ')'; A.c.fillRect(0, 0, A.w, A.h); } }
        if (split && curB) curB.draw(t);
      }
      c.clearRect(0, 0, W, H);
      if (parts) P.forEach(function (p) {
        if (p.tx != null) { p.vx += (p.tx - p.x) * .012; p.vy += (p.ty - p.y) * .012; p.vx *= .82; p.vy *= .82; }
        else { var a = Math.sin(p.x * .004 + t * .4) * 2 + Math.cos(p.y * .004) * 2; p.vx = p.vx * .96 + Math.cos(a) * .25; p.vy = p.vy * .96 + Math.sin(a) * .25; }
        p.x += p.vx; p.y += p.vy; if (p.x < 0) p.x += W; if (p.x > W) p.x -= W; if (p.y < 0) p.y += H; if (p.y > H) p.y -= H;
        c.fillStyle = 'hsl(' + p.hue + ',100%,62%)'; c.fillRect(p.x, p.y, 2.2, 2.2);
      });
      requestAnimationFrame(frame);
    })();
    function close(watched) { run = false; timers.forEach(clearTimeout); capTimers.forEach(clearTimeout); clearInterval(likeT); SFX.stop(); el.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', esc); if (watched) xp(100, 'Watched the whole trailer'); }
    function esc(e) { if (e.key === 'Escape') close(); }
    document.addEventListener('keydown', esc);
    el.querySelector('.skip').onclick = function () { close(); };
    var um = el.querySelector('.unmute'); if (um) um.onclick = function () { enableSound(); SFX.mode('full'); SFX.boom(); um.remove(); };
    el.querySelector('[data-end-close]').onclick = function () { close(true); };
    el.querySelector('[data-end-go]').onclick = function () { close(true); register(); };
    el.querySelector('[data-again]').onclick = function () { close(true); trailer(); };
    el.querySelector('.skip').focus();
  }
})();
