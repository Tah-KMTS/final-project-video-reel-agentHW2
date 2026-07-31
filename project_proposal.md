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

Capital Syndicate is a top-down 2D simulation RPG (React + Phaser) set in a single, flattened city map built around one hand-authored landmark, the Whispering Temple Chapel, with 9 other hub buildings packed around it (Tokyo Stock Exchange, Capital Business Center, Bank & Realty Office, Real Estate Agency, Federal Government Building, Neon Dragon Casino, The Underworld, Industrial Zone, Central Train Station). The player builds net worth toward a tiered win condition ($50k / $250k / $1M / $5M / $10M, with an aspirational $1B "flex goal" past the real win) through trading, running businesses, gambling, and crime (with a full jail/escape/bail system), while navigating a government/regulatory layer — elections, a Fed chairmanship, FTC investigations, SCOTUS, IRS, FBI, Congress.

Already shipped and playable today:
- A persistent **in-game smartphone** with 5 apps: **Social/X** (an in-game feed the player and NPCs post to), Banking & Portfolio, Startups & M&A, Dark Web & Underground, Contacts & Romance.
- **LLM-narrated daily events** (via the OpenAI API, with a templated fallback when no key is present) that already move stock prices and crypto hype rather than being decorative text.
- **20 finance-world NPCs with generated voice-over**, plus a live free-text NPC chat backend (FastAPI + `gpt-4o-mini`) for deeper conversational interaction, separate from the 4 tycoon-boss antagonists (Biffle, Vanderbilt, Rusk, Howard Marks).
- A full economic/behavioral loop: stock exchange with short-selling and a live risk meter, casino games (Blackjack, Poker, Slots, Russian Roulette) with a Luck stat wired into odds, non-lethal combat, and a jail/escape system.
- Three additional fully-built worlds (Hunter's Rift, Yu-Gi-Oh, Domino City) exist in the codebase but are intentionally unreachable from the overworld — a deliberate scope decision to keep the shipping game to one coherent world, not a bug.

This is a live, actively-developed codebase, not a static prototype or a plan on paper. That matters for how this proposal was written: rather than describing the game from an old planning document, the scope below was set after re-auditing the actual current repository (commit history, source files, and the project's own `production/backlog.md`) — which caught that several items an earlier internal planning note called "still to do" (the chapel landmark art, a tree-rendering bug, the smartphone UI itself) had already shipped, while NPC vehicle traffic had been built, found buggy, and deliberately rolled back rather than fixed. Grounding the proposal in the real repo state, not the last hand-off note, is itself part of the discipline this project is demonstrating.

### Why This Fits a GenAI + Social Media Course

Two layers, distinct from each other:

**The product's core mechanic is genAI-and-social-media, not just finance.** The Social/X app is designed so that posts — from the player or from LLM-driven NPCs — feed a sentiment signal that moves stock prices and crypto hype (FOMO rallies, panic-selling), and the daily-event narration is itself LLM-generated rather than templated. The game is, mechanically, a small closed-loop simulation of the exact phenomenon the course studies: generative AI content shaping social sentiment shaping real (in-world) financial outcomes. Wiring the Social app's posts through to actual price movement — currently scoped but not yet a fully distinct system — is the centerpiece of the next milestone below.

**The build process is a second, independent applied-AI story.** Rather than one generalist coding assistant, the game itself is developed with a coordinated fleet of 10 specialized Claude Code subagents, each with a narrow mandate and its own tool access: a **producer** that scopes and sequences backlog work, a **game-designer** for balance/mechanics, a **world-builder** for lore/layout consistency, a **gameplay-engineer** for state/store/scene implementation, an **art-director** and **visual-polish** agent for procedural visual consistency, a **technical-artist** who checks art direction against sprite/tile-generation feasibility, an **audio-director** for sound identity, a **writer** for NPC dialogue, and a **qa-tester** that verifies changes in a live browser rather than trusting self-reported success. I act as the human product owner: setting priorities, reviewing each agent's actual output, and deciding what ships. That orchestration pattern — a manager delegating scoped, verifiable work to specialist agents and treating their output as evidence to check rather than facts to trust — already caught real drift once during this proposal's own scoping (see above), which is the clearest demonstration of why the pattern matters.

### Scope of Work for This Milestone (12 days: July 31 – August 12)

The full vision above is already substantially built; the milestone below is the next bounded increment, not a restatement of the whole project. Four items, sequenced by risk so the highest-uncertainty piece runs first and there's runway left to descope if it runs long:

1. **Sentiment engine tie-in (~2 days) — the genAI/social-media centerpiece.** Wire the existing phone Social app's posts into actual market movement (a post triggers visible stock-price/hype swings). This completes, as a distinct system, the exact mechanic described above as the project's central genAI-and-social-media claim. Lower technical risk than it sounds because it reuses existing hooks (`tickFinanceMarket`, the LLM-narrated daily events already shipped) rather than building new market-simulation logic from scratch.
2. **Restore NPC vehicle traffic with real collision (~3–4 days).** NPC-owned cars currently sit parked and decorative — a working drive/yield system was built, proved buggy (shaking, teleporting, sprinting NPCs), and was explicitly rolled back in a prior session. The player's own car already collides correctly with buildings, pedestrians, and parked vehicles via the existing `isSingleTileObstacle` / `isBlockedTile` pattern in `OverworldScene.js`; this item extends that same, already-proven obstacle check to NPC-driven cars, deliberately without rebuilding the more ambitious yield-to-vehicle-ahead choreography that caused the last failure. Highest engineering risk item (it has failed once before), so it's sequenced early enough to leave recovery time.
3. **46-NPC ambient finance roster (~2–3 days).** Implement the ambient roster already specified in `production/finance-npc-roster-50.md` (currently only 4 tycoon bosses exist), giving the world's population more of the texture the Social/X sentiment loop needs to feel alive.
4. **Verification pass + demo capture (~2–3 days).** Build/lint clean, a full manual playtest walking every one of the 10 hub buildings (the top item on the project's own current backlog, never logged as done after the last map rework), and a recorded walkthrough showing a social post visibly moving a price/hype meter, NPC cars driving and yielding, and an ambient-roster NPC encounter — plus a one-line record of which specialist agent produced each piece, as raw material for this course's video-reel agent.

If any item runs over budget, item 2 (vehicle traffic) is the one to cut first — it has failed once before and is the least connected to this course's specific genAI/social-media framing — followed by item 3, never item 4.

### Explicitly Out of Scope for This Milestone

Ambient background music, the decision on how far to extend the free-text NPC chat backend, the Food Center energy-top-up hook, and reviving the built-but-dormant Hunter's Rift / Yu-Gi-Oh / Domino City worlds (unreachable by design, not by bug) are real, tracked backlog items but not attempted here. The four deliberately-unbuilt building categories (Court & Prison, Dock/Pier, Entertainment Complex, Food Center) remain deferred by existing design decision. Naming and deferring these is itself part of the scoping discipline this proposal is demonstrating.

### Success Criteria

- `npm run build` and `npm run lint` (oxlint) stay clean (0 errors).
- A social-app post visibly moves a stock price or hype meter in a live demo — the core genAI/social-media claim, verified live.
- NPC cars actually drive and respect collision with buildings, pedestrians, and each other — confirmed live, not just structurally verified.
- At least one ambient-roster NPC (beyond the existing 4 bosses) is encounterable and distinguishable in a live playthrough.
- A recorded demo exists that the video-reel agent can consume as raw material, and it matches what this proposal describes.
- Every item above has a one-line record of which specialist agent produced it, as evidence of real multi-agent orchestration rather than a single monolithic assistant.

### Risks

- **Vehicle traffic has already failed once** (the prior yield/drive system was buggy enough to be fully reverted) — mitigated by scoping this attempt smaller than the last one (reuse the proven player-side obstacle check; skip the yield-to-vehicle-ahead choreography that caused the rollback), and by making it the first item to cut if time runs short.
- **Visual/behavioral bugs are hard to verify without a human eye** (a documented failure mode from earlier in this project: passing structural or lint checks isn't the same as looking or working right) — mitigated by mandatory live-browser/screenshot confirmation before calling any item done, per the project's own QA-tester agent role.
- **Conflating "already built" with "built for this course"** is a real risk given how much of the game predates this milestone — mitigated by this document's explicit separation of "What It Is — Current State" from "Scope of Work for This Milestone," and by the per-item agent-attribution log required in the success criteria.
- **Four items in 12 days is tight**, especially if item 2 runs long — mitigated by risk-ordered sequencing, committing after each independently-verifiable step, and the pre-declared descope order (cut 2, then 3, never 4).
