"""Renders each Slide into a standalone HTML file under slides/."""

import os

from models import Slide

BASE_CSS = """
  body {
    margin: 0;
    width: 1280px;
    height: 720px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: 'Segoe UI', sans-serif;
    background: #0d1117;
    color: #f0f6fc;
    text-align: center;
    padding: 60px;
    box-sizing: border-box;
  }
  h1 { font-size: 40px; margin-bottom: 24px; }
  p { font-size: 24px; line-height: 1.4; max-width: 900px; }
"""


def slide_to_html(slide: Slide, index: int) -> str:
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide {index}</title>
<style>{BASE_CSS}</style>
</head>
<body>
  <h1>Slide {index}</h1>
  <p>{slide.description}</p>
</body>
</html>
"""


VISUAL_SLIDE_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 3 - AI Sentiment Flow</title>
<style>
  body {
    margin: 0;
    width: 1280px;
    height: 720px;
    background: #0d1117;
    color: #f0f6fc;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    padding: 40px;
  }
  h1 { font-size: 36px; margin-bottom: 10px; }
  .caption { font-size: 20px; max-width: 900px; text-align: center; margin-top: 20px; color: #c9d1d9; }
  .box-label { font-size: 18px; font-weight: bold; fill: #f0f6fc; }
</style>
</head>
<body>
  <h1>The Feed Moves the Market</h1>
  <svg width="1100" height="360" viewBox="0 0 1100 360">
    <defs>
      <linearGradient id="sentimentGradient" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#f85149"/>
        <stop offset="50%" stop-color="#d29922"/>
        <stop offset="100%" stop-color="#3fb950"/>
      </linearGradient>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>

    <!-- Box 1: AI social post -->
    <rect x="20" y="120" width="220" height="120" rx="16" fill="#161b22" stroke="#58a6ff" stroke-width="3"/>
    <text x="130" y="165" text-anchor="middle" class="box-label">AI-Generated</text>
    <text x="130" y="190" text-anchor="middle" class="box-label">Social Post</text>
    <text x="130" y="222" text-anchor="middle" font-size="28">&#128241;</text>

    <path d="M250 180 L340 180" stroke="#8b949e" stroke-width="4" marker-end="url(#arrow)"/>

    <!-- Box 2: Sentiment meter -->
    <rect x="350" y="120" width="260" height="120" rx="16" fill="#161b22" stroke="#f78166" stroke-width="3"/>
    <text x="480" y="150" text-anchor="middle" class="box-label">Sentiment Meter</text>
    <rect x="375" y="175" width="210" height="18" rx="9" fill="url(#sentimentGradient)"/>
    <circle cx="530" cy="184" r="9" fill="#f0f6fc" stroke="#0d1117" stroke-width="2"/>
    <text x="480" y="222" text-anchor="middle" font-size="14" fill="#c9d1d9">panic &#8594; hype</text>

    <path d="M620 180 L710 180" stroke="#8b949e" stroke-width="4" marker-end="url(#arrow)"/>

    <!-- Box 3: Stock price chart -->
    <rect x="720" y="120" width="360" height="180" rx="16" fill="#161b22" stroke="#3fb950" stroke-width="3"/>
    <text x="900" y="150" text-anchor="middle" class="box-label">Stock Price</text>
    <polyline points="740,240 780,220 820,255 860,190 900,210 940,160 980,180 1020,140 1060,150"
              fill="none" stroke="#3fb950" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""


def visual_slide_html(slide: Slide) -> str:
    return VISUAL_SLIDE_TEMPLATE.replace("__NARRATION__", slide.narration)


def render_slides(slides: list[Slide], out_dir: str = "slides") -> list[str]:
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, slide in enumerate(slides, start=1):
        path = os.path.join(out_dir, f"slide_{i}.html")
        html = visual_slide_html(slide) if i == 3 else slide_to_html(slide, i)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        paths.append(path)
    return paths
