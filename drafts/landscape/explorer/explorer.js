// Reading landscape explorer: one syllabus in six movements, with a keyboard- and screen-reader-usable map.
const DATA_URL = document.querySelector('meta[name="landscape-data"]')?.content || 'landscape.json';
const D = await (await fetch(DATA_URL)).json();
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const HIGH = matchMedia('(prefers-contrast: more)').matches;
const COARSE = matchMedia('(pointer: coarse)').matches;
const byId = Object.fromEntries(D.readings.map(r => [r.id, r]));
const areaById = Object.fromEntries(D.areas.map(a => [a.id, a]));
const S = D.paths.find(p => p.type === 'movements');
const M = S.movements;
const syllabusIds = new Set(M.flatMap(m => m.stops));
document.getElementById('count').textContent = D.readings.length;

// ---------- text helpers ----------
const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fmt = iso => new Date(iso + 'T12:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
const statusEl = document.getElementById('status');
function announce(text) { statusEl.textContent = ''; setTimeout(() => { statusEl.textContent = text; }, 30); }
const listJoin = xs => xs.length < 2 ? xs.join('') : xs.slice(0, -1).join(', ') + ' and ' + xs[xs.length - 1];

// Number areas in reading order across the map (top row first, left to right).
const areaOrder = [...D.areas].sort((a, b) => (Math.round(a.y * 4) - Math.round(b.y * 4)) || (a.x - b.x));
areaOrder.forEach((a, i) => { a.num = i + 1; });
const sessionOf = {};
const companionOf = {};
{ let k = 0; M.forEach(m => m.stops.forEach(id => {
  if ((m.companions || []).includes(id)) { sessionOf[id] = k - 1; companionOf[id] = true; } else sessionOf[id] = k++;
})); }
const sessionText = id => `${companionOf[id] ? 'Read alongside session' : 'Session'} ${sessionOf[id] + 1} · ${fmt(D.slots[sessionOf[id]])}`;

function composition(m) {
  const counts = {};
  m.stops.forEach(id => { const a = areaById[byId[id].area]; counts[a.name] = (counts[a.name] || 0) + 1; });
  const parts = Object.entries(counts).sort((a, b) => b[1] - a[1]).map(([n, c]) => `${n} (${c})`);
  return parts.length === 1 ? `All its readings sit in ${parts[0].replace(/ \(\d+\)$/, '')}.` : `It draws from ${listJoin(parts)}.`;
}
function neighbours(r, n = 6) {
  return D.readings.filter(o => o !== r).map(o => [o, (o.x - r.x) ** 2 + (o.y - r.y) ** 2]).sort((a, b) => a[1] - b[1]).slice(0, n).map(a => a[0]);
}
document.getElementById('map-summary').textContent =
  `The map places ${D.readings.length} readings by what they say, in ${D.areas.length} areas: ` +
  areaOrder.map(a => `${a.num}, ${a.name}`).join('; ') + `. The year’s syllabus moves through six themes: ` +
  M.map(m => `${m.n}, ${m.name}`).join('; ') + '.';

// ---------- panel ----------
const detail = document.getElementById('detail');
const routeOl = document.getElementById('route');
document.getElementById('path-why').textContent = S.why;
document.getElementById('legend').innerHTML = areaOrder.map(a =>
  `<li><span class="num" style="background:${a.ink}" aria-hidden="true">${a.num}</span>${esc(a.name)}</li>`).join('');
routeOl.innerHTML = M.map((m, i) => `<li data-i="${i}"><button type="button" class="list-btn" data-m="${i}">${esc(m.n)}. ${esc(m.name)}</button>
  <ul>${m.stops.map(id => `<li><button type="button" class="list-btn" data-id="${id}">${esc(byId[id].title)}</button><span class="d">${sessionText(id)}</span></li>`).join('')}</ul></li>`).join('');
routeOl.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  stopTour();
  if (b.dataset.m) showMovement(+b.dataset.m, { focusPanel: true });
  else selectReading(b.dataset.id, { fly: true, focusPanel: true });
});
document.getElementById('all').innerHTML = areaOrder.map(a => `<h3>${a.num}. ${esc(a.name)}</h3><ul>${
  D.readings.filter(r => r.area === a.id).map(r => `<li><a href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.title)}</a>${r.read ? ' <span class="muted small">(already read)</span>' : ''}</li>`).join('')}</ul>`).join('');
detail.addEventListener('click', e => {
  const b = e.target.closest('button[data-id]'); if (!b) return;
  selectReading(b.dataset.id, { fly: true, focusPanel: true });
});

function renderOverview() {
  detail.innerHTML = `<h2 id="detail-title" tabindex="-1">About this map</h2>
    <p>Each point is a passage of a reading, placed by what it says. Readings that say similar things sit close together, and the terrain rises where many of them cluster.</p>
    <p>The year’s syllabus moves through six themes. Its 27 readings are marked in blue, and the rest of the map is faded. Select a theme to see where its readings sit.</p>`;
}
function renderMovement(m) {
  detail.innerHTML = `<span class="tag" style="background:var(--soft);color:var(--link-strong)">Theme ${esc(m.n)} of ${M.length}</span>
    <h2 id="detail-title" tabindex="-1">${esc(m.name)}</h2><p>${esc(m.blurb)}</p><p class="muted small">${esc(composition(m))}</p>
    <h3>Readings in this theme</h3><ul class="near">${m.stops.map(id => `<li><button type="button" class="list-btn" data-id="${id}">${esc(byId[id].title)}</button><span class="muted">${esc(byId[id].cite)} · ${sessionText(id).toLowerCase()}</span></li>`).join('')}</ul>`;
}
function renderReading(r) {
  const a = areaById[r.area], s = sessionOf[r.id];
  detail.innerHTML = `<span class="tag" style="background:${a.color};color:${a.ink}">Area ${a.num}: ${esc(a.name)}</span>
    ${r.read ? ' <span class="tag" style="background:#eceae4;color:#3d3c39">Already read by the group</span>' : ''}
    <h2 id="detail-title" tabindex="-1"><a href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.title)}</a></h2>
    <p class="muted small">${esc(r.cite)}${s !== undefined ? ` · ${sessionText(r.id).toLowerCase()}` : ''}</p>
    ${r.quote ? `<blockquote>“${esc(r.quote)}”</blockquote>` : ''}
    <h3>Nearby on the map</h3><ul class="near">${neighbours(r).map(o => `<li><button type="button" class="list-btn" data-id="${o.id}">${esc(o.title)}</button><span class="muted">Area ${areaById[o.area].num}: ${esc(areaById[o.area].name)}</span></li>`).join('')}</ul>`;
}
function focusDetail() { const h = document.getElementById('detail-title'); if (h) h.focus({ preventScroll: false }); }
renderOverview();

// ---------- 3D view (optional: everything above works without it) ----------
const canGL = (() => { try { const c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); } catch { return false; } })();
let view = { focus() {}, flyReading() {}, flyMovement() {}, overview() {}, select() {} };
const sceneEl = document.getElementById('scene');
if (!canGL) {
  document.getElementById('nogl').hidden = false;
  sceneEl.hidden = true;
  document.querySelector('.legend').hidden = true;
  document.getElementById('hint').hidden = true;
} else {
  view = await build3D();
}

// ---------- movements, readings, tour ----------
let step = -1, tour = null;
const playBtn = document.getElementById('play');
function markRoute(i) { routeOl.querySelectorAll(':scope > li').forEach(li => li.classList.toggle('on', +li.dataset.i === i)); }
function showMovement(i, opts = {}) {
  step = Math.max(0, Math.min(M.length - 1, i));
  const m = M[step];
  renderMovement(m); markRoute(step);
  view.focus(step);
  view.flyMovement(step);
  announce(`Theme ${m.n}, ${m.name}. ${m.stops.length} readings. ${composition(m)}`);
  if (opts.focusPanel) focusDetail();
}
function selectReading(id, opts = {}) {
  const r = byId[id];
  renderReading(r);
  view.select(id);
  if (opts.fly) view.flyReading(id);
  announce(`${r.title}. Area ${areaById[r.area].num}, ${areaById[r.area].name}.`);
  if (opts.focusPanel) focusDetail();
}
function overview() {
  stopTour(); step = -1; markRoute(-1); renderOverview(); view.focus('all'); view.select(null); view.overview();
  playBtn.textContent = 'Play the year';
  announce('Overview of the whole map.');
}
async function runTour() {
  const my = tour = {};
  playBtn.textContent = 'Pause';
  for (let k = step + 1; k < M.length; k++) {
    if (tour !== my) return;
    showMovement(k);
    await new Promise(r => setTimeout(r, REDUCED ? 8000 : 6000));
  }
  stopTour();
}
function stopTour() { tour = null; playBtn.textContent = step >= 0 && step < M.length - 1 ? 'Resume' : 'Play the year'; }
playBtn.addEventListener('click', () => { if (tour) stopTour(); else { if (step >= M.length - 1) step = -1; runTour(); } });
document.getElementById('next').addEventListener('click', () => { stopTour(); showMovement(step + 1); });
document.getElementById('prev').addEventListener('click', () => { stopTour(); showMovement(step < 0 ? 0 : step - 1); });
document.getElementById('reset').addEventListener('click', overview);
const deep = location.hash.match(/^#m(\d)$/);
if (deep) showMovement(+deep[1] - 1); else view.focus('all');

// ---------- suggest a reading with an AI assistant ----------
document.querySelector('[data-copy="llm-prompt"]')?.addEventListener('click', e => {
  const text = document.getElementById('llm-prompt').textContent, status = document.getElementById('copy-status');
  const selectIt = () => { const r = document.createRange(); r.selectNodeContents(document.getElementById('llm-prompt')); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); status.textContent = 'Selected. Press Cmd+C or Ctrl+C to copy.'; };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(() => { status.textContent = 'Copied.'; }, selectIt); else selectIt();
});

// =====================================================================
async function build3D() {
  const THREE = await import('three');
  const { OrbitControls } = await import('three/addons/controls/OrbitControls.js');
  const G = D.grid, SIZE = 10, HMAX = 2.1;
  function heightAt(x, y) {
    const fx = Math.min(Math.max(x * G - 0.5, 0), G - 1.001), fy = Math.min(Math.max(y * G - 0.5, 0), G - 1.001);
    const i = Math.floor(fx), j = Math.floor(fy), u = fx - i, v = fy - j;
    const h = (c, r) => D.height[r * G + c];
    return (h(i, j) * (1 - u) + h(i + 1, j) * u) * (1 - v) + (h(i, j + 1) * (1 - u) + h(i + 1, j + 1) * u) * v;
  }
  const world = (x, y, lift = 0) => new THREE.Vector3((x - 0.5) * SIZE, heightAt(x, y) * HMAX + lift, (y - 0.5) * SIZE);

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0xfbfaf7);
  renderer.domElement.setAttribute('aria-hidden', 'true');
  sceneEl.appendChild(renderer.domElement);
  const scene = new THREE.Scene();
  const fog = new THREE.Fog(0xfbfaf7, 20, 36);
  scene.fog = fog;
  const camera = new THREE.PerspectiveCamera(42, 1, 0.05, 100);
  const HOME = { pos: new THREE.Vector3(0, 8.5, 9.5), target: new THREE.Vector3(0, 0.3, 0.4) };
  camera.position.copy(HOME.pos);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.copy(HOME.target);
  controls.enableDamping = !REDUCED;
  controls.maxPolarAngle = Math.PI * 0.46;
  controls.minDistance = 1.2; controls.maxDistance = 20;
  controls.enableKeys = false;

  // touch: page scrolls until the reader chooses to explore the map
  const exploreBtn = document.getElementById('explore');
  if (COARSE) {
    controls.enabled = false; exploreBtn.hidden = false;
    exploreBtn.addEventListener('click', () => {
      const on = !controls.enabled;
      controls.enabled = on; sceneEl.classList.toggle('gestures', on);
      exploreBtn.textContent = on ? 'Done exploring' : 'Explore the map';
      exploreBtn.style.top = on ? 'auto' : ''; exploreBtn.style.bottom = on ? '5rem' : '';
    });
  }

  // terrain
  const pos = new Float32Array(G * G * 3), col = new Float32Array(G * G * 3);
  const white = new THREE.Color('#ffffff'), tmp = new THREE.Color();
  for (let r = 0; r < G; r++) for (let c = 0; c < G; c++) {
    const k = r * G + c, h = D.height[k];
    pos.set([((c + 0.5) / G - 0.5) * SIZE, h * HMAX, ((r + 0.5) / G - 0.5) * SIZE], k * 3);
    tmp.set(areaById[D.areaGrid[k]].color);
    const t = white.clone().lerp(tmp, 0.3 + 0.7 * Math.min(1, h * 1.4));
    col.set([t.r, t.g, t.b], k * 3);
  }
  const idx = [];
  for (let r = 0; r < G - 1; r++) for (let c = 0; c < G - 1; c++) { const a = r * G + c; idx.push(a, a + G, a + 1, a + 1, a + G, a + G + 1); }
  const tg = new THREE.BufferGeometry();
  tg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  tg.setAttribute('color', new THREE.BufferAttribute(col, 3));
  tg.setIndex(idx); tg.computeVertexNormals();
  // area boundaries: a cell is on a border when its neighbour belongs to another area
  const border = new Float32Array(G * G);
  for (let r = 0; r < G; r++) for (let c = 0; c < G; c++) {
    const k = r * G + c, a = D.areaGrid[k];
    border[k] = (c + 1 < G && D.areaGrid[k + 1] !== a) || (r + 1 < G && D.areaGrid[k + G] !== a) ? 1 : 0;
  }
  tg.setAttribute('border', new THREE.BufferAttribute(border, 1));
  const terrainMat = new THREE.ShaderMaterial({
    vertexColors: true, fog: true,
    uniforms: THREE.UniformsUtils.merge([THREE.UniformsLib.fog, { uDim: { value: 0 }, uContour: { value: HIGH ? 0.55 : 0.3 } }]),
    vertexShader: `
      attribute float border;
      varying vec3 vColor; varying float vH; varying vec3 vN; varying float vB;
      #include <fog_pars_vertex>
      void main() {
        vColor = color; vH = position.y; vN = normal; vB = border;
        vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
        gl_Position = projectionMatrix * mvPosition;
        #include <fog_vertex>
      }`,
    fragmentShader: `
      varying vec3 vColor; varying float vH; varying vec3 vN; varying float vB;
      uniform float uDim; uniform float uContour;
      #include <fog_pars_fragment>
      void main() {
        float light = 0.64 + 0.36 * max(dot(normalize(vN), normalize(vec3(-0.35, 1.0, 0.45))), 0.0);
        vec3 base = vColor * light;
        float c = vH * 9.0;
        float f = abs(fract(c - 0.5) - 0.5) / max(fwidth(c), 1e-3);
        float line = (1.0 - min(f, 1.0)) * smoothstep(0.02, 0.08, vH);
        base = mix(base, vec3(0.38, 0.36, 0.33), line * uContour);
        base = mix(base, vec3(0.30, 0.29, 0.27), smoothstep(0.35, 0.9, vB) * 0.45);
        float lum = dot(base, vec3(0.299, 0.587, 0.114));
        base = mix(base, mix(vec3(lum), vec3(0.984, 0.980, 0.968), 0.55), uDim * 0.8);
        gl_FragColor = vec4(base, 1.0);
        #include <fog_fragment>
      }`
  });
  scene.add(new THREE.Mesh(tg, terrainMat));

  // passages
  const dotTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d'); x.beginPath(); x.arc(32, 32, 26, 0, Math.PI * 2); x.fillStyle = '#fff'; x.fill(); return new THREE.CanvasTexture(c); })();
  const pp = [], pc = [], pOwner = [];
  D.readings.forEach((r, k) => { const ink = new THREE.Color(areaById[r.area].ink); r.p.forEach(([x, y]) => { const v = world(x, y, 0.03); pp.push(v.x, v.y, v.z); pc.push(ink.r, ink.g, ink.b); pOwner.push(k); }); });
  const pcBase = Float32Array.from(pc);
  const pg = new THREE.BufferGeometry();
  pg.setAttribute('position', new THREE.Float32BufferAttribute(pp, 3));
  pg.setAttribute('color', new THREE.Float32BufferAttribute(pc, 3));
  const passageMat = new THREE.PointsMaterial({ size: 0.07, map: dotTex, vertexColors: true, transparent: true, opacity: HIGH ? 0.85 : 0.6, alphaTest: 0.2, depthWrite: false });
  scene.add(new THREE.Points(pg, passageMat));

  // reading markers
  const markers = new THREE.InstancedMesh(new THREE.SphereGeometry(1, 16, 12), new THREE.MeshLambertMaterial(), D.readings.length);
  const m4 = new THREE.Matrix4(), q = new THREE.Quaternion();
  const COBALT = new THREE.Color('#004fcc'), MUTED = new THREE.Color('#c9c4b9'), PAPER = new THREE.Color('#fbfaf7'), GREY = new THREE.Color('#5f5e5a');
  let focusSet = null, selectedId = null;
  function styleMarkers() {
    D.readings.forEach((r, i) => {
      let c, s;
      if (focusSet) [c, s] = focusSet.has(r.id) ? [COBALT, focusSet.size > 10 ? 0.095 : 0.12] : [MUTED, 0.03];
      else [c, s] = syllabusIds.has(r.id) ? [COBALT, 0.08] : r.read ? [GREY, 0.075] : [new THREE.Color(areaById[r.area].ink), 0.05];
      if (r.id === selectedId) s = Math.max(s, 0.14);
      m4.compose(world(r.x, r.y, 0.07), q, new THREE.Vector3(s, s, s));
      markers.setMatrixAt(i, m4); markers.setColorAt(i, c);
    });
    markers.instanceMatrix.needsUpdate = true; markers.instanceColor.needsUpdate = true;
  }
  scene.add(markers);
  scene.add(new THREE.HemisphereLight(0xffffff, 0xd8d2c4, 1.6));
  const sun = new THREE.DirectionalLight(0xffffff, 1.2); sun.position.set(-4, 8, 5); scene.add(sun);

  // glow halos for the focused movement (off in high contrast)
  const haloTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 128; const x = c.getContext('2d'), g = x.createRadialGradient(64, 64, 4, 64, 64, 62);
    g.addColorStop(0, 'rgba(0,79,204,0.9)'); g.addColorStop(0.35, 'rgba(0,79,204,0.4)'); g.addColorStop(1, 'rgba(0,79,204,0)'); x.fillStyle = g; x.fillRect(0, 0, 128, 128); return new THREE.CanvasTexture(c); })();
  const glowMat = new THREE.PointsMaterial({ size: 0.9, map: haloTex, transparent: true, depthWrite: false, opacity: 0.75 });
  const glowGeo = new THREE.BufferGeometry();
  const glowPts = new THREE.Points(glowGeo, glowMat); glowPts.visible = !HIGH; scene.add(glowPts);

  // trail through the six movements
  const trailPts = M.map(m => world(m.x, m.y, 0.3));
  const smooth = new THREE.CatmullRomCurve3(trailPts, false, 'centripetal').getPoints(1400)
    .map(p => new THREE.Vector3(p.x, Math.max(p.y, heightAt(p.x / SIZE + 0.5, p.z / SIZE + 0.5) * HMAX + 0.1), p.z));
  const trail = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(smooth), 1800, 0.016, 8),
    new THREE.MeshBasicMaterial({ color: 0x004fcc, transparent: true, opacity: 0.8 }));
  scene.add(trail);

  // labels (decorative on the map; the same information is in the panel)
  const layer = document.getElementById('labels');
  const labels = [];
  function addLabel(el, v3) { layer.appendChild(el); const l = { el, v3 }; labels.push(l); return l; }
  const areaLabels = areaOrder.map(a => {
    const el = document.createElement('div'); el.className = 'lbl area'; el.style.color = a.ink; el.setAttribute('aria-hidden', 'true');
    el.innerHTML = `<span class="n"><span>${a.num}</span></span>${esc(a.name)}`;
    return { a, l: addLabel(el, world(a.x, a.y, 0.45)) };
  });
  const moveLabels = M.map((m, i) => {
    const el = document.createElement('div'); el.className = 'lbl stop'; el.setAttribute('aria-hidden', 'true');
    el.textContent = `${m.n} · ${m.name}`;
    return addLabel(el, world(m.x, m.y, 0.3));
  });
  let readingLabels = [];
  const tip = document.createElement('div'); tip.className = 'tip'; tip.hidden = true; document.querySelector('.stage').appendChild(tip);

  // focus a movement: its readings pop, everything else fades
  let dimTarget = 0;
  function focus(i) {
    const all = i === 'all';
    const m = all || i === null ? null : M[i];
    focusSet = m ? new Set(m.stops) : all ? new Set(syllabusIds) : null;
    dimTarget = m ? 1 : all ? 0.75 : 0;
    scene.fog = focusSet ? null : fog;
    const colAttr = pg.getAttribute('color');
    for (let k = 0; k < pOwner.length; k++) {
      const id = D.readings[pOwner[k]].id;
      let c = new THREE.Color(pcBase[k * 3], pcBase[k * 3 + 1], pcBase[k * 3 + 2]);
      if (focusSet) c = focusSet.has(id) ? COBALT.clone() : c.lerp(PAPER, 0.82);
      colAttr.setXYZ(k, c.r, c.g, c.b);
    }
    colAttr.needsUpdate = true;
    passageMat.opacity = focusSet ? 0.9 : (HIGH ? 0.85 : 0.6);
    trail.material.opacity = focusSet ? 0.4 : 0.8;
    glowGeo.setFromPoints(m ? m.stops.map(id => world(byId[id].x, byId[id].y, 0.1)) : []);
    trail.material.opacity = all ? 0.85 : m ? 0.4 : 0.8;
    styleMarkers();
    const areasIn = new Set(m ? m.stops.map(id => byId[id].area) : []);
    areaLabels.forEach(({ a, l }) => l.el.classList.toggle('other', !!m && !areasIn.has(a.id)));
    moveLabels.forEach((l, j) => { l.el.classList.toggle('on', j === i); l.el.classList.toggle('other', !!m && j !== i); });
    readingLabels.forEach(l => { l.el.remove(); labels.splice(labels.indexOf(l), 1); });
    readingLabels = m ? m.stops.map(id => {
      const r = byId[id], b = document.createElement('button');
      b.type = 'button'; b.className = 'lbl rd';
      b.textContent = r.title.length > 44 ? r.title.slice(0, 42) + '…' : r.title;
      b.setAttribute('aria-label', r.title);
      b.addEventListener('click', () => selectReading(id, { fly: true }));
      return addLabel(b, world(r.x, r.y, 0.12));
    }) : [];
    layer.classList.toggle('focused', !!m);
  }

  // camera
  let anim = null;
  function flyTo(target, dist) {
    const dir = camera.position.clone().sub(controls.target).setY(0).normalize();
    if (!isFinite(dir.x)) dir.set(0, 0, 1);
    const endP = target.clone().add(dir.multiplyScalar(dist)).add(new THREE.Vector3(0, dist * 0.75, 0));
    if (REDUCED) { camera.position.copy(endP); controls.target.copy(target); return; }
    const sP = camera.position.clone(), sT = controls.target.clone(), t0 = performance.now();
    anim = now => { const k = Math.min(1, (now - t0) / 1300), e = k < .5 ? 2 * k * k : 1 - (-2 * k + 2) ** 2 / 2;
      camera.position.lerpVectors(sP, endP, e); controls.target.lerpVectors(sT, target, e); if (k >= 1) anim = null; };
  }
  function flyMovement(i) {
    const m = M[i];
    const spread = Math.max(...m.stops.map(id => Math.hypot(byId[id].x - m.x, byId[id].y - m.y))) * SIZE;
    flyTo(world(m.x, m.y, 0.1), Math.max(2.8, spread * 2.3));
  }
  function flyReading(id) { const r = byId[id]; flyTo(world(r.x, r.y, 0.1), 2.6); }
  function goHome() {
    if (REDUCED) { camera.position.copy(HOME.pos); controls.target.copy(HOME.target); return; }
    const sP = camera.position.clone(), sT = controls.target.clone(), t0 = performance.now();
    anim = now => { const k = Math.min(1, (now - t0) / 1300), e = k * k * (3 - 2 * k);
      camera.position.lerpVectors(sP, HOME.pos, e); controls.target.lerpVectors(sT, HOME.target, e); if (k >= 1) anim = null; };
  }

  // keyboard: arrows turn, +/- zoom, N/P movements, Escape or Home for the overview
  const sph = new THREE.Spherical();
  function orbit(dTheta, dPhi, zoom) {
    const off = camera.position.clone().sub(controls.target);
    sph.setFromVector3(off);
    sph.theta += dTheta;
    sph.phi = Math.min(Math.max(sph.phi + dPhi, 0.15), controls.maxPolarAngle);
    sph.radius = Math.min(Math.max(sph.radius * zoom, controls.minDistance), controls.maxDistance);
    off.setFromSpherical(sph); camera.position.copy(controls.target).add(off);
  }
  sceneEl.addEventListener('keydown', e => {
    const k = e.key;
    const act = {
      ArrowLeft: () => orbit(-0.15, 0, 1), ArrowRight: () => orbit(0.15, 0, 1),
      ArrowUp: () => orbit(0, -0.08, 1), ArrowDown: () => orbit(0, 0.08, 1),
      '+': () => orbit(0, 0, 0.85), '=': () => orbit(0, 0, 0.85), '-': () => orbit(0, 0, 1.18), '_': () => orbit(0, 0, 1.18),
      n: () => { stopTour(); showMovement(step + 1); }, N: () => { stopTour(); showMovement(step + 1); },
      p: () => { stopTour(); showMovement(step < 0 ? 0 : step - 1); }, P: () => { stopTour(); showMovement(step < 0 ? 0 : step - 1); },
      Escape: overview, Home: overview,
    }[k];
    if (act) { e.preventDefault(); act(); }
  });

  // pointer picking
  const ray = new THREE.Raycaster(), mouse = new THREE.Vector2();
  function pick(ev) {
    const b = renderer.domElement.getBoundingClientRect();
    mouse.set(((ev.clientX - b.left) / b.width) * 2 - 1, -((ev.clientY - b.top) / b.height) * 2 + 1);
    ray.setFromCamera(mouse, camera);
    const hit = ray.intersectObject(markers)[0];
    return hit ? [D.readings[hit.instanceId], ev.clientX - b.left, ev.clientY - b.top] : null;
  }
  renderer.domElement.addEventListener('pointermove', ev => {
    if (ev.pointerType !== 'mouse') return;
    const h = pick(ev);
    tip.hidden = !h; renderer.domElement.style.cursor = h ? 'pointer' : '';
    if (h) { tip.textContent = h[0].title; tip.style.left = h[1] + 14 + 'px'; tip.style.top = h[2] + 10 + 'px'; }
  });
  let downAt = null;
  renderer.domElement.addEventListener('pointerdown', ev => { downAt = [ev.clientX, ev.clientY]; if (tour) stopTour(); });
  renderer.domElement.addEventListener('pointerup', ev => {
    if (!downAt || Math.hypot(ev.clientX - downAt[0], ev.clientY - downAt[1]) > 5) return;
    const h = pick(ev);
    if (h) selectReading(h[0].id, { fly: true });
    else if (focusSet) overview();
  });

  // render loop
  function resize() { const w = sceneEl.clientWidth, h = sceneEl.clientHeight; renderer.setSize(w, h); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  new ResizeObserver(resize).observe(sceneEl); resize();
  const v = new THREE.Vector3();
  styleMarkers();
  renderer.setAnimationLoop(now => {
    if (anim) anim(now);
    const u = terrainMat.uniforms.uDim; u.value += (dimTarget - u.value) * (REDUCED ? 1 : 0.08);
    glowMat.opacity = REDUCED ? 0.75 : 0.6 + 0.22 * Math.sin(now / 450);
    controls.update();
    renderer.render(scene, camera);
    const w = sceneEl.clientWidth, h = sceneEl.clientHeight, placed = [];
    labels.forEach(l => {
      v.copy(l.v3).project(camera);
      const vis = v.z < 1 && Math.abs(v.x) < 1.05 && Math.abs(v.y) < 1.05;
      l.el.style.visibility = vis ? '' : 'hidden';
      if (!vis) return;
      let x = (v.x + 1) / 2 * w, y = (1 - v.y) / 2 * h;
      if (!l.el.classList.contains('area')) {
        const lw = l.el.offsetWidth || 120, lh = (l.el.offsetHeight || 20) + 4;
        for (let t = 0; t < 10; t++) {
          const hit = placed.find(p => Math.abs(p.x - x) < (p.w + lw) / 2 + 6 && Math.abs(p.y - y) < lh);
          if (!hit) break; y = hit.y + lh;
        }
        placed.push({ x, y, w: lw });
      }
      l.el.style.left = x + 'px'; l.el.style.top = y + 'px';
    });
  });

  return {
    focus, flyMovement, flyReading, overview: goHome,
    select(id) { selectedId = id; styleMarkers(); },
  };
}
