"""
Final Project Video Reel Agent — entry point.

Run: python reel_agent.py

Pipeline:
  1. Load project_proposal.md                                      [DONE]
  2. Ask the agent for a structured 4-6 slide plan (Pydantic model) [DONE]
  3. Critique + revise each slide/narration pair, in parallel       [DONE]
  4. Render each (revised) slide as HTML, screenshot to PNG         [DONE]
  5. Synthesize TTS narration per slide (gpt-4o-mini-tts)           [DONE]
  6. Stitch slide images + audio into reel.mp4, each clip's         [DONE]
     duration matching its narration
  7. Write ai_grading/slide_plan.json          [DONE]
     ai_grading/critique_feedback.json         [DONE]
     ai_grading/agent_flow.png
"""

import os

from critique import critique_all
from html_renderer import render_slides
from models import CritiqueReport, Slide, SlidePlan
from screenshot import screenshot_all
from slide_planner import generate_slide_plan, load_proposal
from tts_renderer import render_audio
from video_builder import build_video


def write_json(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def apply_critique(plan: SlidePlan, report: CritiqueReport) -> list[Slide]:
    """Builds the final slide list using each slide's revised description
    and narration instead of the first draft."""
    revised_by_index = {c.slide_index: c for c in report.critiques}
    finalized = []
    for i, slide in enumerate(plan.slides, start=1):
        c = revised_by_index.get(i)
        if c:
            finalized.append(
                Slide(description=c.revised_description, narration=c.revised_narration)
            )
        else:
            finalized.append(slide)
    return finalized


def main() -> None:
    proposal = load_proposal()
    plan = generate_slide_plan(proposal)
    write_json(
        os.path.join("ai_grading", "slide_plan.json"),
        plan.model_dump_json(indent=2),
    )
    print(f"Wrote {len(plan.slides)} slides to ai_grading/slide_plan.json")

    report = critique_all(plan.slides)
    write_json(
        os.path.join("ai_grading", "critique_feedback.json"),
        report.model_dump_json(indent=2),
    )
    print(f"Wrote {len(report.critiques)} critiques to ai_grading/critique_feedback.json")

    final_slides = apply_critique(plan, report)
    html_paths = render_slides(final_slides)
    print(f"Wrote {len(html_paths)} HTML slides to slides/")

    png_paths = screenshot_all(html_paths)
    print(f"Wrote {len(png_paths)} slide screenshots")

    audio_paths = render_audio(final_slides)
    print(f"Wrote {len(audio_paths)} narration clips")

    build_video(png_paths, audio_paths=audio_paths, out_path="reel.mp4")
    print("Wrote reel.mp4")


if __name__ == "__main__":
    main()
