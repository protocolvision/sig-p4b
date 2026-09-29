/* Reading map (2D). Progressive detail: theme tags preview their readings on hover or focus,
   a click pins a theme or a reading, and zooming in reveals reading titles. The map is plain SVG. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var D = JSON.parse(document.getElementById('map-data').textContent);
  var svg = document.getElementById('map'), wrap = svg.parentNode, info = document.getElementById('map-info');
  var tip = wrap.querySelector('.map-tip'), spokes = svg.querySelector('.spokes'), names = svg.querySelector('.names');
  var chips = document.querySelectorAll('.map-filters button');
  var VB = svg.viewBox.baseVal, W = VB.width, H = VB.height;
  var view = { x: 0, y: 0, w: W, h: H }, pinned = 0, current = -1, leaveTimer = null, area = -1, anim = 0;
  var hullG = svg.querySelector('.hull'), areaLabels = svg.querySelectorAll('text.area');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DEFAULT = '<p class="muted">Hover over a theme tag or a dot, or select one to pin it here. Select an area name, or click anywhere on the map, to look closer at that part.</p>';
  var dots = {}; svg.querySelectorAll('.dots circle[data-i]').forEach(function (c) { dots[c.dataset.i] = c; });
  var esc = function (s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var fmt = function (iso) { return new Date(iso + 'T12:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' }); };
  var when = function (it) { return it.s == null ? '' : (it.co ? 'Read alongside session ' : 'Session ') + (it.s + 1) + ' · ' + fmt(D.slots[it.s]); };
  var short = function (t) { return t.length > 38 ? t.slice(0, 36) + '…' : t; };
  var zoom = function () { return W / view.w; };

  function el(tag, attrs, parent) { var e = document.createElementNS(NS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); parent.appendChild(e); return e; }
  function clear(g) { while (g.firstChild) g.removeChild(g.firstChild); }

  /* names beside dots; text size stays constant on screen as you zoom */
  function drawNames(ids) {
    clear(names);
    var z = zoom(), fs = 15 / z, lh = 19 / z, placed = [];
    var tag = current && svg.querySelector('.tag[data-th="' + current + '"] rect');
    if (tag) {   // the open theme tag counts as taken space, so names move clear of it
      var th = D.themes[current - 1], tw = +tag.getAttribute('width');
      placed.push({ x: th.x - tw / 2, y: th.y - 4, w: tw }, { x: th.x - tw / 2, y: th.y + 12, w: tw });
    }
    ids.slice().sort(function (a, b) { return dots[a].getAttribute('cy') - dots[b].getAttribute('cy'); }).forEach(function (i) {
      var c = dots[i], cx = +c.getAttribute('cx'), cy = +c.getAttribute('cy'), label = short(D.items[i].t);
      var w = label.length * 7.2 / z, right = cx + 9 / z + w < view.x + view.w;
      var x = right ? cx + 9 / z : cx - 9 / z - w, y = cy + 5 / z;
      for (var k = 0; k < 12; k++) {   // nudge down until it clears the names already placed
        var hit = placed.some(function (p) { return x < p.x + p.w && p.x < x + w && Math.abs(p.y - y) < lh; });
        if (!hit) break; y += lh;
      }
      placed.push({ x: x, y: y, w: w });
      if (Math.abs(y - (cy + 5 / z)) > 1) el('line', { x1: cx, y1: cy, x2: right ? x : x + w, y2: y - 5 / z, class: 'leader', 'stroke-width': (1 / z).toFixed(2) }, names);
      var t = el('text', { x: x, y: y, 'font-size': fs.toFixed(2) }, names);
      t.textContent = label;
    });
  }
  function themeIds(n) { return D.items.map(function (it, i) { return it.th === n ? i : -1; }).filter(function (i) { return i >= 0; }); }
  function areaIds(k) { return D.items.map(function (it, i) { return it.ar === k ? i : -1; }).filter(function (i) { return i >= 0; }); }
  /* in a busy area, name only this year's readings; the panel lists the rest */
  function areaNameIds() { var ids = areaIds(area); return ids.length <= 24 ? ids : ids.filter(function (i) { return D.items[i].th; }); }
  function syllabusIds() { return D.items.map(function (it, i) { return it.th ? i : -1; }).filter(function (i) { return i >= 0; }); }

  /* show a theme: spokes from its tag, its reading names, everything else faded */
  function show(n) {
    current = n;
    clear(spokes);
    svg.setAttribute('data-focus', n ? String(n) : '');
    svg.querySelectorAll('.tag').forEach(function (g) { g.classList.toggle('on', +g.dataset.th === n); });
    if (!n) { drawNames(area >= 0 ? areaNameIds() : zoom() >= 2 ? syllabusIds() : []); return; }
    var th = D.themes[n - 1], z = zoom();
    themeIds(n).forEach(function (i) {
      var c = dots[i];
      el('line', { x1: th.x, y1: th.y, x2: c.getAttribute('cx'), y2: c.getAttribute('cy'), 'stroke-width': (1.2 / z).toFixed(2) }, spokes);
    });
    drawNames(themeIds(n));
  }
  function pinTheme(n) {
    if (n && area >= 0) setArea(-1);
    pinned = n;
    chips.forEach(function (b) { b.setAttribute('aria-pressed', String(+b.dataset.th === n)); });
    show(n);
    if (!n) { info.innerHTML = DEFAULT; return; }
    var th = D.themes[n - 1];
    var list = themeIds(n).sort(function (a, b) { return D.items[a].s - D.items[b].s; }).map(function (i) {
      var it = D.items[i];
      return '<li><a href="' + esc(it.u) + '">' + esc(it.t) + '</a> <span class="muted">' + esc(it.c) + ' · ' + when(it) + '</span></li>';
    }).join('');
    info.innerHTML = '<h2>' + esc(th.n) + '. ' + esc(th.name) + '</h2><p>' + esc(th.blurb) + '</p><ol>' + list + '</ol>';
  }
  function pinReading(i) {
    var it = D.items[i], th = it.th ? D.themes[it.th - 1] : null;
    svg.querySelectorAll('circle.on').forEach(function (c) { c.classList.remove('on'); });
    dots[i].classList.add('on');
    info.innerHTML = '<h2><a href="' + esc(it.u) + '">' + esc(it.t) + '</a></h2><p class="muted">' + esc(it.c) + '</p>' +
      '<p class="small">' + esc(it.a) + (th ? ' · Theme ' + esc(th.n) + ', ' + esc(th.name) + ' · ' + when(it) : '') + (it.rd ? ' · already read by the SIG' : '') + '</p>';
  }

  /* hover card for any dot */
  function showTip(c) {
    var it = D.items[c.dataset.i], th = it.th ? D.themes[it.th - 1] : null;
    tip.innerHTML = '<strong>' + esc(it.t) + '</strong><span>' + esc(it.a) + (th ? ' · ' + esc(th.n) + ' ' + esc(th.short) : '') + '</span>';
    var r = c.getBoundingClientRect(), w = wrap.getBoundingClientRect();
    tip.hidden = false;
    var left = Math.min(r.left - w.left + 12, w.width - tip.offsetWidth - 4);
    tip.style.left = Math.max(4, left) + 'px'; tip.style.top = (r.top - w.top - tip.offsetHeight - 8) + 'px';
  }

  /* zoom and pan by changing the viewBox */
  /* an area: zoom to fit its readings, shade its outline, fade the rest, list it below */
  function setArea(k) {
    area = k;
    svg.setAttribute('data-area', k < 0 ? '' : String(k));
    clear(hullG);
    areaLabels.forEach(function (t) { t.classList.toggle('on', +t.dataset.a === k); });
    D.items.forEach(function (it, i) {
      dots[i].classList.toggle('in', it.ar === k);
      if (it.ar === k) el('circle', { cx: dots[i].getAttribute('cx'), cy: dots[i].getAttribute('cy'), r: 30 }, hullG);
    });
  }
  function pinArea(k) {
    if (pinned) pinTheme(0);
    setArea(k);
    if (k < 0) { info.innerHTML = DEFAULT; animateTo({ x: 0, y: 0, w: W, h: H }); return; }
    var ids = areaIds(k), xs = ids.map(function (i) { return +dots[i].getAttribute('cx'); }), ys = ids.map(function (i) { return +dots[i].getAttribute('cy'); });
    var x0 = Math.min.apply(null, xs) - 60, x1 = Math.max.apply(null, xs) + 260, y0 = Math.min.apply(null, ys) - 60, y1 = Math.max.apply(null, ys) + 60;
    var z = Math.min(W / (x1 - x0), H / (y1 - y0), 4), w = W / z, h = H / z;
    animateTo({ x: (x0 + x1) / 2 - w / 2, y: (y0 + y1) / 2 - h / 2, w: w, h: h });
    ids.sort(function (a, b) { var A = D.items[a], B = D.items[b]; return (A.th ? 0 : 1) - (B.th ? 0 : 1) || (A.s || 0) - (B.s || 0) || A.t.localeCompare(B.t); });
    var plan = ids.filter(function (i) { return D.items[i].th; }).length;
    var li = function (i) { var it = D.items[i]; return '<li><a href="' + esc(it.u) + '">' + esc(it.t) + '</a> <span class="muted">' + esc(it.c) + (it.th ? ' · Theme ' + esc(D.themes[it.th - 1].n) : '') + '</span></li>'; };
    info.innerHTML = '<h2>' + esc(D.areas[k]) + '</h2><p class="muted">' + ids.length + ' readings' + (plan ? ', ' + plan + ' of them in this year’s plan' : '') + '. <button type="button" class="btn-quiet" data-close>Show the whole map</button></p><ul>' + ids.map(li).join('') + '</ul>';
    info.querySelector('[data-close]').addEventListener('click', function () { pinArea(-1); });
  }
  function animateTo(v) {
    cancelAnimationFrame(anim);
    if (reduced) { setView(v); return; }
    var from = view, t0 = performance.now();
    (function step(t) {
      var p = Math.min((t - t0) / 380, 1), e = 1 - Math.pow(1 - p, 3), mix = function (a, b) { return a + (b - a) * e; };
      setView({ x: mix(from.x, v.x), y: mix(from.y, v.y), w: mix(from.w, v.w), h: mix(from.h, v.h) }, p < 1);
      if (p < 1) anim = requestAnimationFrame(step);
    })(t0);
  }
  function setView(v, quiet) {
    var z = Math.min(Math.max(W / v.w, 1), 6), w = W / z, h = H / z;
    view = { x: Math.min(Math.max(v.x, 0), W - w), y: Math.min(Math.max(v.y, 0), H - h), w: w, h: h };
    svg.setAttribute('viewBox', [view.x, view.y, view.w, view.h].join(' '));
    svg.style.setProperty('--z', zoom());
    svg.classList.toggle('zoomed', zoom() > 1.01);
    var z = zoom();   // tags keep their screen size
    svg.querySelectorAll('.tag').forEach(function (g) { var th = D.themes[g.dataset.th - 1]; g.setAttribute('transform', 'translate(' + th.x + ',' + th.y + ') scale(' + (1 / z).toFixed(4) + ')'); });
    if (quiet) clear(names); else show(pinned);
  }
  function zoomAt(f, cx, cy) {
    var w = view.w / f, h = view.h / f;
    setView({ x: cx - (cx - view.x) / f, y: cy - (cy - view.y) / f, w: w, h: h });
  }
  function toSvg(ev) { var r = svg.getBoundingClientRect(); return { x: view.x + (ev.clientX - r.left) / r.width * view.w, y: view.y + (ev.clientY - r.top) / r.height * view.h }; }
  wrap.querySelectorAll('.map-zoom button').forEach(function (b) {
    b.addEventListener('click', function () {
      var cx = view.x + view.w / 2, cy = view.y + view.h / 2;
      if (b.dataset.z === 'in') zoomAt(1.6, cx, cy); else if (b.dataset.z === 'out') zoomAt(1 / 1.6, cx, cy); else if (area >= 0) pinArea(-1); else setView({ x: 0, y: 0, w: W, h: H });
    });
  });
  svg.addEventListener('dblclick', function (ev) { var p = toSvg(ev); zoomAt(1.8, p.x, p.y); });
  var drag = null, down = null;
  svg.addEventListener('pointerdown', function (ev) { down = { x: ev.clientX, y: ev.clientY }; if (zoom() > 1.01 && !ev.target.closest('circle,.tag')) { drag = { x: ev.clientX, y: ev.clientY, v: view }; svg.setPointerCapture(ev.pointerId); } });
  svg.addEventListener('pointermove', function (ev) {
    if (!drag) return;
    var r = svg.getBoundingClientRect();
    setView({ x: drag.v.x - (ev.clientX - drag.x) / r.width * drag.v.w, y: drag.v.y - (ev.clientY - drag.y) / r.height * drag.v.h, w: drag.v.w, h: drag.v.h });
  });
  svg.addEventListener('pointerup', function () { drag = null; });

  /* wiring: tags preview on hover or focus, pin on click; dots show a card, pin on click */
  svg.querySelectorAll('.tag').forEach(function (g) {
    var n = +g.dataset.th;
    g.addEventListener('mouseenter', function () { clearTimeout(leaveTimer); if (current !== n) show(n); });
    g.addEventListener('mouseleave', function () { clearTimeout(leaveTimer); leaveTimer = setTimeout(function () { show(pinned); }, 150); });
    g.addEventListener('focus', function () { show(n); });
    g.addEventListener('blur', function () { show(pinned); });
    g.addEventListener('click', function () { pinTheme(pinned === n ? 0 : n); });
    g.addEventListener('keydown', function (ev) { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); pinTheme(pinned === n ? 0 : n); } });
  });
  svg.addEventListener('mouseover', function (ev) { var c = ev.target.closest('circle'); if (c) showTip(c); });
  svg.addEventListener('mouseout', function (ev) { if (ev.target.closest('circle')) tip.hidden = true; });
  svg.addEventListener('focusin', function (ev) { var c = ev.target.closest('circle'); if (c) showTip(c); });
  svg.addEventListener('focusout', function () { tip.hidden = true; });
  svg.addEventListener('click', function (ev) {
    if (down && Math.hypot(ev.clientX - down.x, ev.clientY - down.y) > 5) return;   // that was a drag
    var c = ev.target.closest('circle[data-i]'), lab = ev.target.closest('text.area');
    if (c) { tip.hidden = true; pinReading(+c.dataset.i); return; }
    if (lab) { pinArea(+lab.dataset.a); return; }
    if (ev.target.closest('.tag')) return;
    var p = toSvg(ev), best = -1, bd = 45 / zoom();   // elsewhere: open the area of the nearest reading
    D.items.forEach(function (it, i) { var d = Math.hypot(dots[i].getAttribute('cx') - p.x, dots[i].getAttribute('cy') - p.y); if (d < bd) { bd = d; best = i; } });
    if (best >= 0 && D.items[best].ar !== area) pinArea(D.items[best].ar);
  });
  svg.addEventListener('keydown', function (ev) {
    var c = ev.target.closest && ev.target.closest('circle');
    if (c && (ev.key === 'Enter' || ev.key === ' ')) { ev.preventDefault(); pinReading(+c.dataset.i); }
    var lab = ev.target.closest && ev.target.closest('text.area');
    if (lab && (ev.key === 'Enter' || ev.key === ' ')) { ev.preventDefault(); pinArea(+lab.dataset.a); }
    if (ev.key === 'Escape' && area >= 0) pinArea(-1);
  });
  chips.forEach(function (b) { b.addEventListener('click', function () { pinTheme(+b.dataset.th); }); });

  info.innerHTML = DEFAULT;
  var m = location.hash.match(/^#m(\d)$/);
  if (m) pinTheme(+m[1]);
  var ma = location.hash.match(/^#a(\d+)$/);
  if (ma && D.areas[+ma[1]]) pinArea(+ma[1]);
})();
