/* Reading map (2D). Progressive detail: theme tags preview their readings on hover or focus,
   a click pins a theme or a reading, and zooming in reveals reading titles. The map is plain SVG. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var D = JSON.parse(document.getElementById('map-data').textContent);
  var svg = document.getElementById('map'), wrap = svg.parentNode, info = document.getElementById('map-info');
  var tip = wrap.querySelector('.map-tip'), spokes = svg.querySelector('.spokes'), names = svg.querySelector('.names');
  var chips = document.querySelectorAll('.map-filters button');
  var VB = svg.viewBox.baseVal, W = VB.width, H = VB.height;
  var view = { x: 0, y: 0, w: W, h: H }, pinned = 0, current = -1, leaveTimer = null;
  var dots = {}; svg.querySelectorAll('circle[data-i]').forEach(function (c) { dots[c.dataset.i] = c; });
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
  function syllabusIds() { return D.items.map(function (it, i) { return it.th ? i : -1; }).filter(function (i) { return i >= 0; }); }

  /* show a theme: spokes from its tag, its reading names, everything else faded */
  function show(n) {
    current = n;
    clear(spokes);
    svg.setAttribute('data-focus', n ? String(n) : '');
    svg.querySelectorAll('.tag').forEach(function (g) { g.classList.toggle('on', +g.dataset.th === n); });
    if (!n) { drawNames(zoom() >= 2 ? syllabusIds() : []); return; }
    var th = D.themes[n - 1], z = zoom();
    themeIds(n).forEach(function (i) {
      var c = dots[i];
      el('line', { x1: th.x, y1: th.y, x2: c.getAttribute('cx'), y2: c.getAttribute('cy'), 'stroke-width': (1.2 / z).toFixed(2) }, spokes);
    });
    drawNames(themeIds(n));
  }
  function pinTheme(n) {
    pinned = n;
    chips.forEach(function (b) { b.setAttribute('aria-pressed', String(+b.dataset.th === n)); });
    show(n);
    if (!n) { info.innerHTML = '<p class="muted">Hover over a theme tag or a dot, or select one to pin it here.</p>'; return; }
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
  function setView(v) {
    var z = Math.min(Math.max(W / v.w, 1), 6), w = W / z, h = H / z;
    view = { x: Math.min(Math.max(v.x, 0), W - w), y: Math.min(Math.max(v.y, 0), H - h), w: w, h: h };
    svg.setAttribute('viewBox', [view.x, view.y, view.w, view.h].join(' '));
    svg.style.setProperty('--z', zoom());
    svg.classList.toggle('zoomed', zoom() > 1.01);
    show(pinned);
  }
  function zoomAt(f, cx, cy) {
    var w = view.w / f, h = view.h / f;
    setView({ x: cx - (cx - view.x) / f, y: cy - (cy - view.y) / f, w: w, h: h });
  }
  function toSvg(ev) { var r = svg.getBoundingClientRect(); return { x: view.x + (ev.clientX - r.left) / r.width * view.w, y: view.y + (ev.clientY - r.top) / r.height * view.h }; }
  wrap.querySelectorAll('.map-zoom button').forEach(function (b) {
    b.addEventListener('click', function () {
      var cx = view.x + view.w / 2, cy = view.y + view.h / 2;
      if (b.dataset.z === 'in') zoomAt(1.6, cx, cy); else if (b.dataset.z === 'out') zoomAt(1 / 1.6, cx, cy); else setView({ x: 0, y: 0, w: W, h: H });
    });
  });
  svg.addEventListener('dblclick', function (ev) { var p = toSvg(ev); zoomAt(1.8, p.x, p.y); });
  var drag = null;
  svg.addEventListener('pointerdown', function (ev) { if (zoom() > 1.01 && !ev.target.closest('circle,.tag')) { drag = { x: ev.clientX, y: ev.clientY, v: view }; svg.setPointerCapture(ev.pointerId); } });
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
  svg.addEventListener('click', function (ev) { var c = ev.target.closest('circle'); if (c) { tip.hidden = true; pinReading(+c.dataset.i); } });
  svg.addEventListener('keydown', function (ev) {
    var c = ev.target.closest && ev.target.closest('circle');
    if (c && (ev.key === 'Enter' || ev.key === ' ')) { ev.preventDefault(); pinReading(+c.dataset.i); }
  });
  chips.forEach(function (b) { b.addEventListener('click', function () { pinTheme(+b.dataset.th); }); });

  info.innerHTML = '<p class="muted">Hover over a theme tag or a dot, or select one to pin it here.</p>';
  var m = location.hash.match(/^#m(\d)$/);
  if (m) pinTheme(+m[1]);
})();
