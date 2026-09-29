/* Reading map (2D): theme filters and reading details. The map itself is plain SVG. */
(function () {
  var D = JSON.parse(document.getElementById('map-data').textContent);
  var svg = document.getElementById('map'), info = document.getElementById('map-info');
  var chips = document.querySelectorAll('.map-filters button');
  var esc = function (s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var fmt = function (iso) { return new Date(iso + 'T12:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' }); };
  var when = function (it) { return it.s == null ? '' : (it.co ? 'Read alongside session ' : 'Session ') + (it.s + 1) + ' · ' + fmt(D.slots[it.s]); };

  function setTheme(n) {
    chips.forEach(function (b) { b.setAttribute('aria-pressed', String(+b.dataset.th === n)); });
    svg.setAttribute('data-focus', n ? String(n) : '');
    if (!n) { info.innerHTML = '<p class="muted">Select a blue dot, or choose a theme above.</p>'; return; }
    var th = D.themes[n - 1];
    var list = D.items.map(function (it, i) { return [it, i]; }).filter(function (p) { return p[0].th === n; })
      .sort(function (a, b) { return a[0].s - b[0].s; })
      .map(function (p) { return '<li><a href="' + esc(p[0].u) + '">' + esc(p[0].t) + '</a> <span class="muted">' + esc(p[0].c) + ' · ' + when(p[0]) + '</span></li>'; }).join('');
    info.innerHTML = '<h2>' + esc(th.n) + '. ' + esc(th.name) + '</h2><p>' + esc(th.blurb) + '</p><ol>' + list + '</ol>';
  }
  function showReading(i) {
    var it = D.items[i];
    svg.querySelectorAll('.on').forEach(function (c) { c.classList.remove('on'); });
    var dot = svg.querySelector('[data-i="' + i + '"]'); if (dot) dot.classList.add('on');
    var theme = it.th ? D.themes[it.th - 1] : null;
    info.innerHTML = '<h2><a href="' + esc(it.u) + '">' + esc(it.t) + '</a></h2>' +
      '<p class="muted">' + esc(it.c) + '</p>' +
      '<p class="small">' + esc(it.a) + (theme ? ' · Theme ' + esc(theme.n) + ', ' + esc(theme.name) + ' · ' + when(it) : '') +
      (it.rd ? ' · already read by the SIG' : '') + '</p>';
  }
  chips.forEach(function (b) { b.addEventListener('click', function () { setTheme(+b.dataset.th); }); });
  svg.addEventListener('click', function (ev) {
    var c = ev.target.closest('circle'); if (c) showReading(+c.dataset.i);
  });
  svg.addEventListener('keydown', function (ev) {
    var c = ev.target.closest && ev.target.closest('circle');
    if (c && (ev.key === 'Enter' || ev.key === ' ')) { ev.preventDefault(); showReading(+c.dataset.i); }
  });
  var m = location.hash.match(/^#m(\d)$/);
  if (m) setTheme(+m[1]);
})();
