// render score.html in headless Chrome and save the WAV it produces
import { spawn } from "node:child_process"; import fs from "node:fs";
const [url, out] = process.argv.slice(2);
const p = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", ["--headless=new", "--remote-debugging-port=9336", "--autoplay-policy=no-user-gesture-required", "--user-data-dir=" + process.env.SPDIR + "/score-prof-" + process.pid, "about:blank"], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let tabs; for (let i = 0; i < 60; i++) { try { tabs = await (await fetch("http://127.0.0.1:9336/json")).json(); if (tabs.find((t) => t.type === "page")) break; } catch {} await sleep(200); }
const ws = new WebSocket(tabs.find((t) => t.type === "page").webSocketDebuggerUrl); await new Promise((r) => (ws.onopen = r));
let id = 0; const pend = new Map(); const errs = [];
ws.onmessage = (e) => { const m = JSON.parse(e.data); if (pend.has(m.id)) { pend.get(m.id)(m.result); pend.delete(m.id); } if (m.method === "Runtime.exceptionThrown") errs.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text); };
const send = (method, params = {}) => new Promise((r) => { pend.set(++id, r); ws.send(JSON.stringify({ id, method, params })); });
const ev = async (expr) => (await send("Runtime.evaluate", { expression: expr, returnByValue: true })).result.value;
await send("Runtime.enable"); await send("Page.enable"); await send("Page.navigate", { url });
for (let i = 0; i < 400; i++) { if (await ev("!!window.__done")) break; await sleep(250); }
console.log("errors", JSON.stringify(errs));
console.log("events", await ev("window.__events"), "harmony issues", JSON.stringify(await ev("window.__harmony")));
console.log("render", JSON.stringify(await ev("window.__done")));
const n = await ev("window.__wav.length"), chunks = []; const CH = 1 << 20;
for (let o = 0; o < n; o += CH) { const b64 = await ev(`(()=>{const a=window.__wav.subarray(${o},${Math.min(n, o + CH)});let s='';for(let i=0;i<a.length;i+=8192)s+=String.fromCharCode.apply(null,a.subarray(i,i+8192));return btoa(s)})()`); chunks.push(Buffer.from(b64, "base64")); }
fs.writeFileSync(out, Buffer.concat(chunks)); console.log("wrote", out, n, "bytes");
p.kill(); process.exit(0);
