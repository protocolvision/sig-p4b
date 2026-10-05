// node --test site/mentions.test.mjs : checks Webmention target parsing and structural verification with a fake web.
import { test } from "node:test";
import assert from "node:assert/strict";
import { targetId, verifyDoc } from "./mentions.js";

const O = "https://protocolsforbusiness.com/blyg/", ID = "03k800kerdjkv2b55bbca4b2jc";
const web = new Map();
globalThis.fetch = async (url) => {
  const r = web.get(String(url));
  if (!r) return new Response("nope", { status: 404 });
  if (r.redirect) return new Response(null, { status: 302, headers: { Location: r.redirect } });
  return new Response(r.body, { status: 200, headers: { "Content-Type": r.type || "application/json" } });
};
const item = (extra) => JSON.stringify({ blyg: "0.3", id: "aaaaaaaaaaaaaaaaaaaaaaaaaa", kind: "thread", origin: "https://other.example/blyg/",
  version: 3, page: "t/aaaaaaaaaaaaaaaaaaaaaaaaaa/", author: { name: "Ada" }, transclusions: [], ...extra });

test("target must be one of our item pages or item files", () => {
  assert.equal(targetId(O + "t/" + ID + "/", O), ID);
  assert.equal(targetId(O + "items/" + ID + ".json", O), ID);
  assert.equal(targetId("https://evil.example/blyg/t/" + ID + "/", O), null);
  assert.equal(targetId(O + "about/", O), null);
});

test("a stub naming our item verifies, with a pointer and no content", async () => {
  web.set("https://other.example/blyg/items/s1.json", { body: item({ stub_of: { origin: O, id: ID, version: 2 } }) });
  const r = await verifyDoc("https://other.example/blyg/items/s1.json", ID, O);
  assert.equal(r.status, "verified"); assert.equal(r.relation, "stub"); assert.equal(r.author, "Ada");
  assert.equal(r.page, "https://other.example/blyg/t/aaaaaaaaaaaaaaaaaaaaaaaaaa/");
  assert.ok(!("content_md" in r));
});

test("an HTML page is followed to its item document via rel=alternate", async () => {
  web.set("https://other.example/blyg/t/x/", { type: "text/html", body: '<html><head><link rel="alternate" type="application/json" href="../../items/s2.json"></head></html>' });
  web.set("https://other.example/blyg/items/s2.json", { body: item({ transclusions: [{ origin: O, id: ID, version: 2 }] }) });
  const r = await verifyDoc("https://other.example/blyg/t/x/", ID, O);
  assert.equal(r.status, "verified"); assert.equal(r.relation, "transclusion");
});

test("a document claiming another host's origin does not verify", async () => {
  web.set("https://mirror.example/x.json", { body: item({ stub_of: { origin: O, id: ID, version: 2 } }) });
  assert.equal((await verifyDoc("https://mirror.example/x.json", ID, O)).status, "failed");
});

test("withdrawn sources are gone; unrelated documents fail", async () => {
  web.set("https://other.example/blyg/items/w.json", { body: item({ kind: "withdrawn" }) });
  web.set("https://other.example/blyg/items/u.json", { body: item({}) });
  assert.equal((await verifyDoc("https://other.example/blyg/items/w.json", ID, O)).status, "gone");
  assert.equal((await verifyDoc("https://other.example/blyg/items/u.json", ID, O)).status, "failed");
});

test("redirects are followed within bounds, and oversized bodies are refused", async () => {
  web.set("https://other.example/r1", { redirect: "https://other.example/blyg/items/s1.json" });
  assert.equal((await verifyDoc("https://other.example/r1", ID, O)).status, "verified");
  web.set("https://other.example/big.json", { body: "x".repeat(1_100_000) });
  assert.equal((await verifyDoc("https://other.example/big.json", ID, O)).status, "failed");
});

test("a fork verifies only against a pinned version", async () => {
  web.set("https://other.example/blyg/items/f.json", { body: item({ forked_from: { origin: O, id: ID, version: 1 } }) });
  assert.equal((await verifyDoc("https://other.example/blyg/items/f.json", ID, O, () => false)).status, "failed");
  assert.equal((await verifyDoc("https://other.example/blyg/items/f.json", ID, O, (v) => v === 1)).relation, "fork");
});
