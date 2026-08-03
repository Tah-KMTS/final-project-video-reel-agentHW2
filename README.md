# Final Project Video Reel Agent

Turns `project_proposal.md` into a short video reel: a Pydantic-structured slide
plan (via a `gpt-5.6-luna` PydanticAI agent), a parallel critique-and-revise
pass on every slide, HTML/CSS/SVG slides, and a stitched MP4.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m playwright install chromium   # one-time browser download, used to
                                         # screenshot the HTML slides
```

Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your-key-here
```

## Run

```bash
python reel_agent.py
```

This regenerates the slide plan, critiques and revises every slide, renders
each as HTML, screenshots them, synthesizes narration audio per slide, and
stitches everything into `reel.mp4`.

**TTS note:** the provided API key has no access to `tts-1` (403
model_not_found), but does have access to `tts-1-hd` (see
`client.models.list()`) — the model the assignment spec requires anyway.
`tts_renderer.py` is set to `tts-1-hd`. Each slide's `.mp3` is rendered to
`slides/`, and passing those paths as `audio_paths` to `build_video()` makes
each clip last exactly as long as its narration instead of the fixed-length
placeholder. Per the assignment spec, narration is kept under 15 seconds per
clip and the full reel under 60 seconds.

`ai_grading/agent_flow.png` is a static diagram of this pipeline, generated
by `draw_flow_diagram.py` (already included in the repo; re-run it if the
pipeline structure changes).

## Output

- `slides/` — HTML slide files (`slide_3.html` is the required real
  HTML/CSS/SVG visual) and their PNG screenshots
- `ai_grading/slide_plan.json` — slide descriptions + narration text
- `ai_grading/critique_feedback.json` — critique/improvement notes per slide
- `ai_grading/agent_flow.png` — agent flow diagram
- `reel.mp4` — final video (not committed; upload separately)
