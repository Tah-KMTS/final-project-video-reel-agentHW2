"""Critiques and revises each slide's description + narration, in parallel."""

import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent

from models import CritiqueReport, Slide, SlideCritique

load_dotenv()

MODEL_NAME = os.getenv("REEL_MODEL", "openai:gpt-5.6-luna")

SYSTEM_PROMPT = """
You will be given one slide's current description and narration, plus its
slide_index.

Act as a tough but constructive critic, specifically watching for:
- Too much text on screen - if the description is dense or hard to
  quickly read/see at a glance, call that out.
- Weak or generic visuals - the description should describe something
  clear and visually interesting (pictures/icons/layout), not just a
  wall of words with a small icon.
- Monotone or flat narration - narration that just states facts instead
  of sounding upbeat and exciting.

Write:
- critique: what's specifically weak about THIS slide's description and
  narration (reference the too-much-text / weak-visual / monotone
  issues above where they actually apply - don't invent problems that
  aren't there).
- suggestions: concrete, specific fixes - e.g. "cut the on-screen text
  to under N words and lead with one bold visual" or "open the narration
  with an exciting hook instead of a flat statement" - not just "make it
  better."

Then actually apply your own suggestions and write:
- revised_description: a clearer, less text-heavy, more visual version
  of the on-screen content.
- revised_narration: a more energetic, exciting version of the spoken
  narration, still about 15 seconds / 2-3 sentences.

Echo back the same slide_index you were given.
"""

agent = Agent(MODEL_NAME, output_type=SlideCritique, system_prompt=SYSTEM_PROMPT)


def critique_slide(slide: Slide, index: int) -> SlideCritique:
    prompt = (
        f"slide_index: {index}\n"
        f"description: {slide.description}\n"
        f"narration: {slide.narration}\n"
    )
    result = agent.run_sync(prompt)
    return result.output


async def critique_slide_async(slide: Slide, index: int) -> SlideCritique:
    prompt = (
        f"slide_index: {index}\n"
        f"description: {slide.description}\n"
        f"narration: {slide.narration}\n"
    )
    result = await agent.run(prompt)
    return result.output


async def critique_all_async(slides: list[Slide]) -> CritiqueReport:
    # asyncio.gather fires off all these agent calls at (roughly) the same
    # time and waits for all of them to finish, instead of waiting for
    # slide 1's critique to fully finish before even starting slide 2's -
    # this is the "parallelization" the HW2 spec asks for.
    tasks = [critique_slide_async(slide, i) for i, slide in enumerate(slides, start=1)]
    critiques = await asyncio.gather(*tasks)
    return CritiqueReport(critiques=list(critiques))


def critique_all(slides: list[Slide]) -> CritiqueReport:
    return asyncio.run(critique_all_async(slides))
