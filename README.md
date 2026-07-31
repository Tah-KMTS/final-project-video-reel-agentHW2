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
each as HTML, screenshots them, and stitches them into `reel.mp4`.

**Known limitation:** the provided API key has no working access to any
OpenAI TTS model (`tts-1` returns a 403; requesting audio output from
`gpt-5.6-luna` via both `/chat/completions` and `/responses` returns a 400
"unknown parameter" error; `client.models.list()` shows only `gpt-5.6-luna`
is available to this key at all). Until that's resolved, `reel.mp4` is
generated silent, with each slide shown for a fixed 5 seconds
(`video_builder.DEFAULT_SLIDE_SECONDS`). `tts_renderer.py` contains the
intended TTS call; once a working model/endpoint is available, passing its
output paths as `audio_paths` to `build_video()` will use each clip's real
duration and audio instead.

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
