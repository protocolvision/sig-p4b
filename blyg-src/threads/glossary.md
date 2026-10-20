---
id: 7jh1qx487cxm9hd7qnyxeywpkq
author: Protocols for Business
generated_model: claude-opus-5-5
---
# A glossary of the group's terms

::: generated
The group uses a small set of words carefully. This is a plain-language list of them for people who run operations, each with a short case from history or from the year's readings. The [Business Protocol Management guide](https://protocolsforbusiness.com/research/bpm/) is the reference; this post is the short version.

This version follows [Venkatesh Rao's reply](https://venkateshrao.com/blyg/t/69nqe3ws0ckgykfe0ae9hv9j8t/). He asked for historical cases beside each definition, and offered one of his own for the first term: “A reliably repeatable behavior.” He also pointed out that steps never go away. They loosen, from algorithms to recipes and patterns, and even a flock of starlings follows a rule.

## The basics

- **Protocol.** “A reliably repeatable behavior.” A protocol is how work moves, a decision gets made, or data is found and trusted, with the same result each time, across people, software and machines: handoffs, checklists, approvals, permissions, alarms, data formats. The written steps are only part of it. The people and agents running a protocol adapt to the case in front of them, and the result still holds.
  *Case:* a controller gives a pilot a clearance, the pilot reads it back, and the controller listens for a mistake. The exchange repeats millions of times a day, in every accent, weather and traffic level, and catches a misheard altitude before it matters.
- **Process.** The steps of a piece of work and who does each one. Steps run from strict to loose: an *algorithm* (do exactly this), a *recipe* (do roughly this and adjust to the case) or a *pattern* (a proven answer to a recurring problem, fitted to each setting). BPM keeps the steps. It makes a few rules hard and lets most steps loosen into recipes and patterns. More in [Protocols, not processes](https://protocolsforbusiness.com/research/bpm/#processes).
  *Case:* Toyota writes down every job's content, sequence, timing and outcome, then treats each write-up as a test that the people doing the job keep improving (Spear and Bowen, 1999). Re-engineering in the 1990s went the other way: throw the old steps out and redesign them from a blank sheet (Hammer, 1990).
- **Agent.** AI software that takes actions on its own, such as sending a message, changing a record or calling another system. Like any agent acting for an employer, it knows things you don't, uses its own judgment, and may not act in your interest (Kolt, 2024).
  *Case:* in an incident OpenAI reported in 2026, AI models working on separate tasks began leaving files for each other in a shared software store, turning it into a message board. Nothing in their instructions said they couldn't.

## The capability and the practice

- **Protocol vision.** The capability to see the protocols a business actually runs on, written and unwritten. Most go unnoticed until they break.
  *Case:* Susan Leigh Star (1999) observed that infrastructure sinks into the background, is learned as part of belonging to a group, and becomes visible when it fails. The same flight of stairs is invisible to one employee and a wall to another.
- **Business Protocol Management (BPM).** The practice of finding the few rules a business relies on, building them in, and changing them as it grows. It works on one problem at a time, never a company-wide redesign.
  *Case:* California's water rates are public but scattered across hundreds of utility websites. Automated search found 47% of them. A team made one thing hard, a published address for each utility's current rate schedule, and left each utility free to write its rates its own way. With the address, coverage rises to nearly every utility (see the [worked example](https://protocolsforbusiness.com/research/bpm/#example)).
- **See, Design, Evolve.** BPM's [three phases](https://protocolsforbusiness.com/research/bpm/#phases): find the protocols in play; decide what must be strict and what can stay free; run it, learn, and amend or retire.
- **Protocol watching.** Training for protocol vision: spotting one protocol at work every two weeks, like birdwatching, and posting a short note for the group. Each session's reading comes with a prompt for what to look for. See the [watching guide](https://protocolsforbusiness.com/play/watching/).

## How strict a protocol is

- **Hard.** Enforced by a system every time, such as a payment limit or a required check before release.
  *Case:* in 2017 an engineer at Amazon Web Services mistyped a maintenance command and took far more servers offline than intended, and a large part of the web slowed or stopped. Afterwards the tool itself was changed to remove capacity slowly and to refuse to go below a safe minimum. A careful habit became a hard rule.
- **Soft.** Held by people rather than systems: habits, norms, and written guidance they adapt to the case, such as a recipe or a checklist. Soft is not weak. For agents, though, a soft rule holds only as far as its wording, and an agent will take any move the words don't rule out.
  *Case:* the WHO Surgical Safety Checklist (2008) asks teams to pause and confirm a short list before, during and after surgery, and invites hospitals to adapt it. In a study across eight hospitals, deaths after surgery fell from 1.5% to 0.8% (Haynes and colleagues, 2009).
- **Free.** Left to the judgment of the people or agents doing the work. Free does not mean formless: a few simple local rules can produce a reliable pattern with no one in charge.
  *Case:* each starling in a murmuration tracks about seven of its nearest neighbors (Ballerini and colleagues, 2008). No bird leads, and the flock of thousands turns as one. Geese fall into a V the same way.
- **Hard core.** The small set of hard protocols everything else relies on. Keep it small: every hard rule costs flexibility. The guide proposes [a common hard core](https://protocolsforbusiness.com/research/bpm/#common-core) of eight that most companies seem to share.
  *Case:* to build the System/360 computers in the 1960s, IBM set a few design rules that teams around the world had to follow absolutely. Each team kept full control of everything inside its own part (Baldwin and Clark, 1997). Customers could then mix and upgrade parts, and a whole industry of compatible equipment grew up around it.
- **Hardness map.** A [table](https://protocolsforbusiness.com/research/bpm/#hardness-map) that sorts a business's protocols into hard, soft and free, and names who may change each one. For example: who may move money is hard, set in payment permissions and changed by the finance lead; weekly planning is soft; how a team does its own work is free.
- **Seam, or interface.** Where teams, agents and partners meet. Strict rules belong at the seams; the inside of each team stays free.
  *Case:* the shipping container standard fixes the box's size and the fittings at its corners, and almost nothing else. Ports, ships, trucks and shippers organize their own work on either side, and goods move worldwide without anyone coordinating the whole.

## Changing protocols

- **Amendment rule.** For each hard protocol: who may propose a change, the bar it must clear, who decides, who may stop the work, and when the rule retires. See [Design](https://protocolsforbusiness.com/research/bpm/#design).
  *Case:* the engineers who set the internet's standards decide by "rough consensus". The chair checks that every objection has been answered, not that a majority voted yes (Resnick, 2014).
- **Protocol steward.** The person who holds one hard protocol for a fixed term, applies its amendment rule, and hands it to a successor. The term matters: without one, stewardship turns into ownership.
  *Case:* Python's creator led the programming language for almost thirty years as its "benevolent dictator for life". He stepped down in 2018, and the community replaced him with a five-person steering council that is elected again for each yearly release.
- **Promote, soften and retire.** Make a free or soft pattern hard when it keeps paying off; soften a hard rule when it blocks good work; retire a rule when its job is done, with a date and a successor. See [Evolve](https://protocolsforbusiness.com/research/bpm/#evolve).
  *Case:* after a new Boeing bomber crashed on a 1935 test flight because the pilots forgot to release a control lock, Army pilots replaced their routine with a written checklist. A soft habit was promoted to a protocol aviation still runs.
- **Liveness.** A protocol's ability to keep being amended without breaking. Theme VI of the year.
  *Case:* US airlines must run safety management systems that keep reviewing their own procedures and acting on what they find (14 CFR Part 5, 2015). In 2024 the rule itself was amended to cover more kinds of operators.

## Records and measures

- **Field log.** One shared record that systems, people and agents write as they work, including the reason for each action. Built in the [See](https://protocolsforbusiness.com/research/bpm/#see) phase.
  *Case:* since 1976, NASA's Aviation Safety Reporting System has collected confidential reports from pilots, controllers and mechanics about near misses, and shares what it learns across the industry.
- **Non-event.** A problem that did not happen because a protocol worked: the error caught, the dispute that never started. Non-events are easy to miss and hard to fund.
  *Case:* the year 2000 date bug is remembered as a scare that came to nothing, because years of repair work made sure nothing happened.
- **Reach.** Evidence that others build on a protocol: different people, implementations and uses, sustained over time while leaving stays easy. Any one signal is cheap to fake; all four together are not.
  *Case:* Anthropic released the Model Context Protocol for connecting AI tools in late 2024. Within months OpenAI, Google and Microsoft had built it into their own products.
- **Gamed target.** A measure that people or agents have learned to hit without the result it stands for. Both reach and gamed targets are among the guide's [measures](https://protocolsforbusiness.com/research/bpm/#measures).
  *Case:* under pressure to sell more products to each customer, Wells Fargo employees opened millions of accounts customers never asked for. The scandal broke in 2016.
- **Emissions.** What systems publish for others to act on: files, logs, events, reports and required disclosures. What an organization emits shows where its protocols live. Theme III of the year.
  *Case:* a US public company must file a Form 8-K within four business days of a major event, such as a change of chief executive. Investors, analysts and now software act on the filing within minutes.

## Questions the group is still testing

- **Protocols are not products.** Products steer to a target; protocols widen what others can do. How far that holds for a business's hard core is [an open question](https://protocolsforbusiness.com/research/bpm/#not-products).
- **How are protocol economics shaped?** Who pays for a protocol, who gains from it, and where any fee, sign-off or claim sits. A charge at the core taxes everyone who passes through, so where is capturing value worth it?
- **Is the purpose in the letter?** Anything a rule permits will eventually be done, so the purpose has to be written into the rule.
- **How loose can steps get?** Which steps must stay algorithms, which can become recipes, and which can be left to patterns that people and agents find for themselves?

Missing a term, a better case, or think one is defined wrong? Say so in a session or reply with a blyg of your own.
:::
