// protocolsforbusiness.com: serve the built site from ../dist, send www and http to the bare https domain,
// and run the blyg's Webmention endpoint (Blygger 0.3 §15) at /blyg/webmention.
import { receive, listFor } from "./mentions.js";

const ORIGIN = "https://protocolsforbusiness.com/blyg/";
const ENDPOINT = ORIGIN + "webmention";

async function ownItem(env, req, id) {
  const r = await env.ASSETS.fetch(new Request(new URL(`/blyg/items/${id}.json`, req.url)));
  return r.ok ? r.json() : null;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.hostname === "www.protocolsforbusiness.com" || url.protocol === "http:") {
      url.hostname = "protocolsforbusiness.com";
      url.protocol = "https:";
      return Response.redirect(url.toString(), 301);
    }
    if (url.pathname === "/blyg/webmention") {
      if (request.method === "POST") {
        return receive(request, env, ctx, ORIGIN, async (id) => !!(await ownItem(env, request, id)),
          async (id) => ((await ownItem(env, request, id))?.changelog || []).filter((c) => c.pinned).map((c) => c.version));
      }
      return new Response("Webmention endpoint for this blyg (Blygger 0.3 §15). POST source and target, form-encoded.\n",
        { headers: { "Content-Type": "text/plain; charset=utf-8", "Link": `<${ENDPOINT}>; rel="webmention"` } });
    }
    if (url.pathname === "/blyg/webmention/responses") {   // verified mentions of one item, for its page
      const id = url.searchParams.get("id") || "";
      if (!/^[0-9a-z]{26}$/.test(id)) return new Response("[]", { headers: { "Content-Type": "application/json" } });
      return new Response(JSON.stringify(await listFor(env, id)), {
        headers: { "Content-Type": "application/json", "Cache-Control": "max-age=300" } });
    }
    const res = await env.ASSETS.fetch(request);
    if (url.pathname.startsWith("/blyg/")) {   // W3C discovery: announce the endpoint on every blyg response
      const out = new Response(res.body, res);
      out.headers.append("Link", `<${ENDPOINT}>; rel="webmention"`);
      return out;
    }
    return res;
  },
};
