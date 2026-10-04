// protocolsforbusiness.com: serve the built site from ../dist, and send www to the bare domain.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "www.protocolsforbusiness.com") {
      url.hostname = "protocolsforbusiness.com";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
