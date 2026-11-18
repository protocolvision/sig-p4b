# SIG-P4B 2026-11-16 — Session Notes

Participants:
  - Sebastián Aristizábal | UTC+1
  - Ben
  - Robert Peake | UTC+1
  - Dylan Fitzgerald — UTC-6
  - ComplexSy
  - Jose Leal
  - rafa (UTC+1)
  - Esther!
  - Mike Casey | UTC -5
  - daniel ospina - UTC+2
  - Nav Nouhi (UTC+1)
  - Matthew McDowell-Sweet (UTC)

---

## 📖 The Reading
Not clearly identified in the discussion. This session was a guest presentation rather than a discussion of a specific text. The week's assigned reading — described by Mike Casey as being "all around these agents being black boxes and nobody knowing what they're doing" — was explicitly deferred to the next session and is not named.

## 🧭 Overview
This was the second "Protocols for Business" session (theme: agents), featuring guest presenter Nav Nouhi, a marketing/growth practitioner and founder of a company called Credible. Nav walked through how discovery is shifting from traditional SEO toward Answer Engine Optimization (AEO)/Generative Engine Optimization (GEO) and the emerging layer of "agent readiness." The group then held an extended Q&A touching on creator-driven demand, whether AI optimization will repeat Google's "SEO slop" problem, content strategy, and the risk that well-capitalized AI labs will gatekeep and monetize agent traffic. The scheduled reading discussion was postponed to the next meeting.

## 💡 Key Points & Themes

- **Three shifts in how people find businesses (Nav):**
  - More than two-thirds of Google searches now end on Google itself (zero-click); the answer sits in the results page.
  - Asking an AI assistant is now mainstream — ~1.2B weekly ChatGPT users (cited Sept 2026 data), plus Claude and Perplexity. Between a quarter and half of consumers reportedly use AI to find local businesses.
  - People no longer type keywords; they use ~23-word prompts and expect a recommendation back.
  - Adobe data: AI referral visits to US retail up ~138% year-over-year, converting ~54% higher than regular traffic (though still a small share of overall traffic).

- **Three-layer stack (Nav):** SEO (crawl/understand/rank) → AEO/GEO (being named and trusted in AI answers) → **agent readiness** (sites offering facts and actions — booking, buying — usable by software acting for a human). No official agent-readiness standards yet; **Google WebMCP** is the framework Nav is focused on.

- **"Isn't this just SEO?" — three key differences (Nav):**
  - Ranking no longer earns a citation: ~38% of cited pages are *not* in the top 10; ~62% of citations come from pages ranked 10–100+.
  - **Query fan-out:** an assistant breaks one question into several background searches (effectively sub-agents), narrowing the answer.
  - Brand *mentions* across the web correlated with AI visibility ~3x more strongly than backlinks (Ahrefs study of ~75 brands; correlation, not proof).

- **How AI "sees" a site (Nav):** two modes — frozen training "memory" vs. live retrieval. Vendors use distinct bots (e.g., OpenAI's GPTBot for training, OAI-SearchBot for its index, GPT-user for live user queries); don't block the ones you want. Content must be **text-first** — assistants can't read JavaScript, so content should load as plain HTML.

- **Technical SEO as the floor (Nav):** sitemaps, clean links, indexable pages. Counterintuitively, *un*-blocking pages like T&Cs and privacy policy can build trust and increase traffic (he saw this in an audit). Consistency of info (address, phone, pricing) across your site and third-party profiles matters — inconsistencies incur a trust penalty. Page speed still matters because agents currently browse via virtual machines.

- **Trust and E-E-A-T (Nav):** AI rewards what can't be faked — firsthand experience, proprietary data, a named expert's view. Google's E-E-A-T (experience, expertise, authoritativeness, trust) applies; trust is most important. Analogy to the earlier era of SEO-spam listicles that made Google's results irrelevant.

- **Agent readiness and the near future (Nav):** personal agents (MetaMuse, Dot, Claude, Instinct, etc., many launched ~Sept) will be ubiquitous within 18–24 months — "the next iPhone app marketplace." Cited Cloudflare data: over half of internet traffic was non-human; ~1700% growth in daily agents year-over-year. Stripe is extending saved-card (Link) functionality to agents.

- **Transparency beats gaming (Ben + Nav):** Ben argued agents can do more cognitive work per query, making one-size-fits-all ranking easier to out-compete and harder to game; this pushes toward simply publishing genuinely useful, transparent information. Nav agreed, noting B2B SaaS "book a meeting / hidden pricing" tactics actively *hurt* you in the AI era — be fully transparent about strengths and weaknesses.

- **Content strategy (Nav, responding to rafa):** drive content from what customers actually ask (meeting notes, FAQs), since those questions become the prompts people type. Quality and citable/verifiable data matter more than format; open-sourcing a digital "book" could work but he hasn't tested it.

- **Positioning vs. capital (Daniel):** even well-capitalized players have finite capital and must choose where to compete; niches from product architecture/positioning trade-offs remain viable, and organic results are more capital-efficient (cheaper than ads) over the medium-to-long term — similar dynamics to the Google era.

## 🔀 Questions & Disagreements

- **Matthew McDowell-Sweet** asked how human-centric, creator-driven demand generation (referencing a Lenny's Podcast episode with WhisperFlow's Hector Serrano) interoperates with an agentic future. Nav distinguished that as a *paid acquisition* channel vs. the *organic* approaches he covers, but said creators (esp. YouTube, whose transcripts are indexable) are a beneficial citation channel — though he hasn't quantified the impact.

- **rafa** asked whether AI optimization will repeat Google's "SEO slop" problem. Nav: unique, high-quality, authoritative content will keep working because agents are built by/for humans; PR newswire releases are often no-index/no-follow and pass no SEO value.

- **Mike Casey** raised the central tension/disagreement: being legible/transparent to agents may amount to giving away IP to well-capitalized labs, and competing claims (e.g., an `agents.txt` file) may simply be adjudicated in favor of the biggest ad spenders. He connected this to the week's reading on agents as black boxes — how do business owners build confidence that agentic tools aren't just funneling to the best-paying ChatGPT advertisers? Nav was candid that he doesn't know how ChatGPT ads will balance paid vs. organic, noted Sam Altman has stated there won't be undue influence ("but time will tell… you gotta pay for those GPUs"), and argued you can be transparent while withholding your "secret sauce" (recipe analogy). Mike pushed back that someone could just ask ChatGPT to reverse-engineer the recipe's exact ratios.

- **Open question (unresolved):** will the dominant assistant monetization model be ads, subscriptions, or a hybrid? Nav leaned toward subscription/agent fees near-term, and singled out Google as best positioned due to decades of Gmail/search data, GCP, and its own chips (vertical integration).

- **Selling to people vs. agents:** rafa asked whether it's still a "people business" or whether one should "build for clankers [agents]." Nav: ultimately a people business, but agents increasingly feed people their options — so "build for the agents" now.

## 🔗 References Mentioned

- **Google WebMCP** — agent-readiness framework Nav is focused on.
- **E-E-A-T** (Google's experience, expertise, authoritativeness, trust guidance).
- **Query fan-out** / sub-agents concept.
- **Adobe** retail AI-referral data; **Cloudflare** bot/agent traffic data; **Ahrefs** brand-mention vs. backlink study.
- **OpenAI/ChatGPT, Anthropic/Claude, Perplexity, Google/Gemini**; personal agents **MetaMuse, Dot, Instinct**.
- **Stripe / Stripe Link** for agents.
- **Lenny's Podcast** episode with **Hector Serrano** (WhisperFlow) on creators as a paid acquisition channel.
- **HubSpot** (example of search-volume-driven generic content).
- **ModelML** (financial agentic AI; cited re: `agents.txt`).
- **Sam Altman** (comments on ads not unduly influencing answers).
- **Credible** — Nav's company; free website audit offered (link shared in the thread).
- **Subset** — safe search app Matthew is building; the Met Office (Matthew's day job).

## ✅ Action Items & Next Time

- **Nav** to share the Credible link in the channel thread (rafa posted it); free audit available for interested members.
- **Members** to drop questions in the Protocols for Business thread and recommend future guest speakers — litmus test: are they actually building AI-native businesses.
- The assigned **reading on agents as black boxes was deferred** and the discussion will resume in ~two weeks.
- After the session, a short optional segment ("Sachin"/a demo) was offered to those who stayed.

## ⭐ Memorable Quotes

- **Nav Nouhi:** "It's better when someone authoritative on LinkedIn is mentioning your site… the more you have out there that is verifiable, the better off you are."
- **Mike Casey:** "Your incentive is to be fully transparent, but at the end of the day, it's just cash that wins. So what's the move in that game?"
- **rafa / Nav:** "Build for the clankers." — "Yeah. Build for clankers."
