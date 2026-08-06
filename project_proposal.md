# Final Project Proposal
## Capital Syndicate: Financial Reality Engine
*(originally prototyped as "Board of Realities")*

### One-line pitch
An AI-agent-built financial-simulation RPG in which a generative-AI social feed — not a scripted event table — is the thing that actually moves the market, so players learn how genAI-driven social content and financial risk feed each other by living inside that loop, not by reading about it.

---

### The Problem

Two gaps, and this project sits at their intersection. First, most financial education is passive: textbooks and case studies describe market cycles and risk, but don't let a learner *feel* the consequences of a leveraged bet or a reputational hit in real time. Second, most discussion of genAI's effect on social media and markets (meme-stock rallies, AI-generated hype, coordinated pump-and-dump content) is analytical rather than experiential — you can read about how a viral post moves a stock, but you can't *cause* it and watch the consequence land. Capital Syndicate is built around a single mechanic that closes both gaps at once: an in-game social feed, populated by both the player and LLM-driven NPCs, whose posts and sentiment are designed to feed directly into market prices and NPC behavior — a lived testbed for how generative AI and social content actually move a financial system.

### Target Audience

- **Primary:** early-career professionals and business/MBA students who want to build intuition for how social sentiment, generative content, and financial risk interact, through play rather than spreadsheets or case studies.
- **Secondary:** general simulation/RPG players drawn to a finance-and-power-themed sandbox (comparable audience to games like *Game Dev Tycoon* or *Yakuza*'s business sub-games).

### What It Is — Current State

Capital Syndicate is a top-down 2D simulation RPG (React + Phaser) set in a single, flattened city map built around one hand-authored landmark, the Whispering Temple Chapel, with 9 other hub buildings packed around it (Tokyo Stock Exchange, Capital Business Center, Bank & Realty Office, Real Estate Agency, Federal Government Building, Neon Dragon Casino, The Underworld, Industrial Zone, Central Train Station). The player builds net worth toward a tiered win condition ($50k / $250k / $1M / $5M / $10M, with an aspirational $1B "flex goal" past the real win) — and can take almost any route to get there: a day job, stock and crypto trading, casino games, real-estate flipping, fishing for quick low-risk cash, or crossing to the dark side through call-center scam work and black-market fencing. Every hub building carries its own short minigame or puzzle rather than a static menu, so each stop on the map is something to actually play, not just a shop screen. The player can also drive a car around the map; going openly criminal draws police attention, and getting caught leads to jail, from which the player can bribe their way out, talk their way out, or attempt an escape — a full crime/consequence loop, not a one-way trip to a game-over screen. The game also navigates a government/regulatory layer — elections, a Fed chairmanship, FTC investigations, SCOTUS, IRS, FBI, Congress.

Already shipped and playable today:
- A persistent **in-game smartphone** with 6 apps: **Social/X** (an in-game feed the player and NPCs post to), Banking & Portfolio, Startups & M&A, Dark Web & Underground, Contacts & Romance, and an **AI Assistant** app that answers any in-game question the player asks (via the OpenAI API) — the smartphone doubles as the "if you're lost" fallback.
- **LLM-narrated daily events** (via the OpenAI API, with a templated fallback when no key is present) that already move stock prices and crypto hype rather than being decorative text.
- **A 76-NPC roster, each built around a real historical figure's persona, plus 6 common NPC archetypes** that populate the world's background (vendors, guards, passersby, and the like) without a unique backstory of their own. Roster and common NPCs alike wander the open world rather than sitting behind a menu — the player has to physically walk up and make contact to trigger a conversation. Every roster NPC has generated voice-over, a live free-text chat backend (FastAPI + `gpt-4o-mini`) for open-ended conversation, and an in-game dating/romance path — the LLM API is what makes talking to and dating them feel like talking to a person rather than picking dialogue-tree options. Separate from these are the 4 tycoon-boss antagonists (Biffle, Vanderbilt, Rusk, Howard Marks).
- A full economic/behavioral loop: stock exchange with short-selling and a live risk meter, casino games (Blackjack, Poker, Slots, Russian Roulette) with a Luck stat wired into odds, non-lethal combat, and a full jail/bribe/escape system tied to the police-chase loop above.
- Three additional fully-built worlds (Hunter's Rift, Yu-Gi-Oh, Domino City) exist in the codebase but are intentionally unreachable from the overworld — a deliberate scope decision to keep the shipping game to one coherent world, not a bug.

This is a live, actively-developed codebase, not a static prototype or a plan on paper. That matters for how this proposal was written: rather than describing the game from an old planning document, the scope below was set after re-auditing the actual current repository (commit history, source files, and the project's own `production/backlog.md`) — which caught that several items an earlier internal planning note called "still to do" (the chapel landmark art, a tree-rendering bug, the smartphone UI itself) had already shipped, while NPC vehicle traffic had been built, found buggy, and deliberately rolled back rather than fixed. Grounding the proposal in the real repo state, not the last hand-off note, is itself part of the discipline this project is demonstrating.

### Why This Fits a GenAI + Social Media Course

Two layers, distinct from each other:

**The product's core mechanic is genAI-and-social-media, not just finance.** The Social/X app is designed so that posts — from the player or from LLM-driven NPCs — feed a sentiment signal that moves stock prices and crypto hype (FOMO rallies, panic-selling), and the daily-event narration is itself LLM-generated rather than templated. The game is, mechanically, a small closed-loop simulation of the exact phenomenon the course studies: generative AI content shaping social sentiment shaping real (in-world) financial outcomes. Wiring the Social app's posts through to actual price movement — currently scoped but not yet a fully distinct system — remains a tracked, deferred item (see Out of Scope below); this milestone's stock-exchange item audits and hardens the exchange itself rather than building that tie-in.

**The build process is a second, independent applied-AI story.** Rather than one generalist coding assistant, the game itself is developed with a coordinated fleet of 10 specialized Claude Code subagents, each with a narrow mandate and its own tool access: a **producer** that scopes and sequences backlog work, a **game-designer** for balance/mechanics, a **world-builder** for lore/layout consistency, a **gameplay-engineer** for state/store/scene implementation, an **art-director** and **visual-polish** agent for procedural visual consistency, a **technical-artist** who checks art direction against sprite/tile-generation feasibility, an **audio-director** for sound identity, a **writer** for NPC dialogue, and a **qa-tester** that verifies changes in a live browser rather than trusting self-reported success. I act as the human product owner: setting priorities, reviewing each agent's actual output, and deciding what ships. That orchestration pattern — a manager delegating scoped, verifiable work to specialist agents and treating their output as evidence to check rather than facts to trust — already caught real drift once during this proposal's own scoping (see above), which is the clearest demonstration of why the pattern matters.

### Scope of Work for This Milestone (revised — ~6 days remaining of the August 3–12 window)

The original plan for this milestone was a from-scratch prison-tutorial prologue world (opening scene + 3 in-prison minigames) plus a general polish pass. With roughly 6 days left of the original 9–10-day window, a brand-new hand-authored world is too much to responsibly finish, so the milestone is re-scoped: drop the new prologue world in favor of a much smaller narrative capstone, and redirect the freed-up time into a prioritized punch-list across the six systems the game's own pitch already leans on. Naming and re-scoping this in the open, rather than quietly letting the prison world slip, is the same discipline this proposal already argues for elsewhere.

**Narrative capstone — a win cutscene, not a new prologue world.** Replace the planned prison-tutorial prologue with a single scripted cutscene that plays when the player crosses the $10M win threshold. It closes the loop the Storyline item below sets up (why the player is chasing $10M at all) without the multi-day cost of building and testing an entirely new hand-authored area from zero.

**Six-item punch-list, in priority order:**

1. **Storyline** — tighten the throughline that gives the player a reason to chase $10M and pays it off in the new win cutscene, replacing the prison world's job of carrying the narrative.
2. **Stock exchange** — a further correctness/behavior audit of the existing exchange (pricing, short-selling, risk meter) beyond what's already shipped; fix whatever the audit turns up.
3. **Arcade/Casino** — add additional minigames to the casino/arcade hub, on top of the existing Blackjack/Poker/Slots/Russian Roulette set.
4. **Crime loop polish (car theft to police to jail to bribe/puzzle)** — this flow already exists end-to-end and is not being rebuilt; the work is straightening its sequencing/logic so the flee-or-bribe, then jail, then bribe-or-puzzle path plays correctly.
5. **Church (Whispering Temple Chapel)** — done; carried forward from prior work and verified complete, not new work for this milestone.
6. **Lisa romance path** — verify the existing dating/chat flow with this NPC actually works end-to-end; fix if it doesn't.

**New mechanic: a 30-day clock.** The game already tracks days and has an "End Day" action that resolves the current day and advances to the next, counting up indefinitely from Day 1. This milestone caps that: it becomes a 30-day countdown — an in-game "Day Left: 30" counter that starts at 30 and drops by one each time the player presses End Day. Reaching 0 days left ends the game (game over) regardless of net worth — real time pressure on a loop that was previously open-ended.

Items 5 and 6 are quick verification passes and unlikely to slip. If time runs short, item 3 (additional casino minigames) is the one to compress first — it's additive scope, not a fix to something already broken. Item 1 (storyline) and the 30-day clock are not cut candidates: together they're what turn the $10M goal into a game with stakes, rather than an open-ended sandbox.

### Explicitly Out of Scope for This Milestone

The prison-tutorial prologue world (opening scene + 3 in-prison minigames) originally planned for this milestone is now explicitly descoped in favor of the lighter win-cutscene capstone above — deferred as a possible future milestone if there's appetite for a full prologue world later, not abandoned as a concept. Ambient background music, the decision on how far to extend the free-text NPC chat backend, the Food Center energy-top-up hook, a full Dock/Pier hub building (fishing itself already works as a standalone activity; a dedicated hub around it does not), and reviving the built-but-dormant Hunter's Rift / Yu-Gi-Oh / Domino City worlds (unreachable by design, not by bug) remain real, tracked backlog items but are not attempted here. The Entertainment Complex remains deferred by existing design decision. The Social-feed-to-price sentiment-engine tie-in, NPC vehicle traffic restoration, and ambient-roster expansion are deferred to a future milestone, not abandoned. Naming and deferring these is itself part of the scoping discipline this proposal is demonstrating.

### Success Criteria

- `npm run build` and `npm run lint` (oxlint) stay clean (0 errors).
- The 30-day clock is live: the counter shows "Day Left: 30", pressing End Day drops it by one, and reaching 0 triggers game over — confirmed in a live playthrough.
- Reaching $10M net worth plays the new win cutscene — confirmed live, not just structurally.
- Each of the six punch-list items has a one-line record of what changed, verified live (screenshot or recorded), not claimed from a diff — including explicit confirmation that the church hub is complete and the Lisa romance path works end-to-end.
- A recorded demo exists showing the 30-day clock, the win cutscene, and at least one polished punch-list item, as raw material for the video-reel agent, and it matches what this proposal describes.
- Every item above has a one-line record of which specialist agent produced it, as evidence of real multi-agent orchestration rather than a single monolithic assistant.

### Risks

- **Re-scoping mid-milestone can look like scope failure instead of scope discipline.** Mitigated by naming the prison-world cut explicitly (see Out of Scope) rather than letting it quietly disappear.
- **The 30-day clock changes game balance** — 30 days may be too tight or too loose against the existing economy loop, since reaching $50k–$10M takes real in-game time. Mitigated by playtesting the full loop against the new clock before finalizing 30 as the number, per the game-designer agent role.
- **The "check and fix" items (stock exchange, crime-loop flow, Lisa romance) are diagnostic by nature** — each could turn out bigger once actually verified live. Mitigated by time-boxing the audit pass before committing to a fix scope, so a deep bug doesn't silently eat the whole milestone.
- **Additional casino minigames are the one genuinely open-ended, scope-creep-shaped item** in this list, the same way "polish" was in the prior milestone. Mitigated by pre-declaring it the first item to compress if time is short.
- **Visual/behavioral bugs are hard to verify without a human eye** (a documented failure mode from earlier in this project: passing structural or lint checks isn't the same as looking or working right) — mitigated by mandatory live-browser/screenshot confirmation before calling any item done, per the project's own QA-tester agent role.
