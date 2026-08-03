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

**The product's core mechanic is genAI-and-social-media, not just finance.** The Social/X app is designed so that posts — from the player or from LLM-driven NPCs — feed a sentiment signal that moves stock prices and crypto hype (FOMO rallies, panic-selling), and the daily-event narration is itself LLM-generated rather than templated. The game is, mechanically, a small closed-loop simulation of the exact phenomenon the course studies: generative AI content shaping social sentiment shaping real (in-world) financial outcomes. Wiring the Social app's posts through to actual price movement — currently scoped but not yet a fully distinct system — is the centerpiece of the next milestone below.

**The build process is a second, independent applied-AI story.** Rather than one generalist coding assistant, the game itself is developed with a coordinated fleet of 10 specialized Claude Code subagents, each with a narrow mandate and its own tool access: a **producer** that scopes and sequences backlog work, a **game-designer** for balance/mechanics, a **world-builder** for lore/layout consistency, a **gameplay-engineer** for state/store/scene implementation, an **art-director** and **visual-polish** agent for procedural visual consistency, a **technical-artist** who checks art direction against sprite/tile-generation feasibility, an **audio-director** for sound identity, a **writer** for NPC dialogue, and a **qa-tester** that verifies changes in a live browser rather than trusting self-reported success. I act as the human product owner: setting priorities, reviewing each agent's actual output, and deciding what ships. That orchestration pattern — a manager delegating scoped, verifiable work to specialist agents and treating their output as evidence to check rather than facts to trust — already caught real drift once during this proposal's own scoping (see above), which is the clearest demonstration of why the pattern matters.

### Scope of Work for This Milestone (9–10 days: August 3 – August 12)

The full vision above is already substantially built and playable; the milestone below is the next bounded increment, not a restatement of the whole project. Two items, sequenced so the headline addition ships first and the safety-net item flexes to whatever time is left:

1. **A prison tutorial world (~5–6 days) — the new onboarding and narrative hook.** Build a self-contained prologue world set in a prison: an opening scene and story that establishes why the player is locked up and plants the revenge motivation that reframes the main world's goal from "get rich" to "get rich and get even." Inside the prison, the player plays through roughly 3 short minigames/puzzles; solving them yields clues that combine into an escape route back into the main city map. This gives the game both a tutorial (a low-stakes space to learn the minigame-and-puzzle pattern before the open world) and a narrative spine (why the player cares about the $10M goal at all), in one build.
2. **General polish pass (~3–4 days) — tightening what's already shipped.** Rather than new features, this is a prioritized punch-list pass across the existing economy loop, minigames, NPC interactions, and UI — smoothing rough edges a first-time player would actually notice, verified live rather than assumed from a changelog.

If time runs short, item 2 is the one to compress first — it's an open-ended punch-list by nature, so it can absorb a smaller time box without leaving anything half-finished. Item 1 is what this milestone is actually judged on and is not a cut candidate; if it's at risk, the fallback is descoping to 2 prison minigames instead of 3, not dropping the prison world itself.

### Explicitly Out of Scope for This Milestone

Ambient background music, the decision on how far to extend the free-text NPC chat backend, the Food Center energy-top-up hook, a full Dock/Pier hub building (fishing itself already works as a standalone activity; a dedicated hub around it does not), and reviving the built-but-dormant Hunter's Rift / Yu-Gi-Oh / Domino City worlds (unreachable by design, not by bug) are real, tracked backlog items but not attempted here. The Entertainment Complex remains deferred by existing design decision. The previous milestone's sentiment-engine tie-in, NPC vehicle traffic restoration, and ambient-roster expansion are deferred to a future milestone, not abandoned. Naming and deferring these is itself part of the scoping discipline this proposal is demonstrating.

### Success Criteria

- `npm run build` and `npm run lint` (oxlint) stay clean (0 errors).
- A new player can enter the prison tutorial, experience the opening scene, solve all 3 (or the descoped 2) minigames, and use the resulting clues to escape into the main world — confirmed in a live playthrough, not just structurally.
- The prison tutorial's story visibly sets up the revenge motivation that carries into the main world's $10M goal.
- The general polish pass has a short, named punch-list with each item verified live (screenshot or recorded), not claimed from a diff.
- A recorded demo exists showing the full prison-to-main-world arc, as raw material for the video-reel agent, and it matches what this proposal describes.
- Every item above has a one-line record of which specialist agent produced it, as evidence of real multi-agent orchestration rather than a single monolithic assistant.

### Risks

- **A brand-new narrative/puzzle space is unproven** — three original minigames plus a story scene is a different kind of work than the mostly-systems work in prior milestones. Mitigated by playtesting each prison minigame in isolation as soon as it's built, rather than waiting to test the full sequence at the end, and by the pre-declared 3-to-2 descope.
- **Tone mismatch risk:** a prison/revenge framing has to land as motivating, not tonally jarring next to the game's existing GTA-meets-finance sandbox voice. Mitigated by routing the opening scene through the same writer/world-builder agents that keep the rest of the world's voice consistent.
- **"Polish" is scope-creep-shaped by nature** — an open-ended punch-list can expand indefinitely. Mitigated by writing the punch-list itself before starting work and time-boxing it, rather than polishing opportunistically as issues are noticed.
- **Visual/behavioral bugs are hard to verify without a human eye** (a documented failure mode from earlier in this project: passing structural or lint checks isn't the same as looking or working right) — mitigated by mandatory live-browser/screenshot confirmation before calling any item done, per the project's own QA-tester agent role.
- **Two items in 9–10 days is still tight** if the prison world's writing or puzzle design takes longer than expected — mitigated by risk-ordered sequencing (headline item first, flexible item second) and the pre-declared descope order (fewer prison minigames, then a smaller polish scope, never dropping the prison world entirely).
