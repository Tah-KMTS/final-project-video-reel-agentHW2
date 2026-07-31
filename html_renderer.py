"""Renders each Slide into a standalone HTML file under slides/.

All 4 slides get a real HTML/CSS/SVG illustration (only 1 is required by
the HW2 spec, but we're doing all of them for a more consistent-looking
video). slide_to_html() below is kept as a plain-text fallback for any
slide index beyond the 4 we've hand-illustrated.
"""

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

VISUAL_CSS = """
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


VISUAL_SLIDE_1 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 1 - Live Inside the System</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Live Inside the System</h1>
  <svg width="1100" height="340" viewBox="0 0 1100 340">
    <defs>
      <linearGradient id="skyGradient" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#161b3a"/>
        <stop offset="100%" stop-color="#0d1117"/>
      </linearGradient>
    </defs>
    <rect x="0" y="0" width="1100" height="340" fill="url(#skyGradient)"/>

    <!-- skyline -->
    <rect x="30"  y="180" width="90"  height="140" fill="#161b22" stroke="#30363d" stroke-width="2"/>
    <rect x="130" y="130" width="70"  height="190" fill="#161b22" stroke="#30363d" stroke-width="2"/>
    <rect x="210" y="210" width="100" height="110" fill="#161b22" stroke="#30363d" stroke-width="2"/>
    <rect x="850" y="160" width="80"  height="160" fill="#161b22" stroke="#30363d" stroke-width="2"/>
    <rect x="950" y="200" width="110" height="120" fill="#161b22" stroke="#30363d" stroke-width="2"/>

    <!-- chapel, the landmark - taller, gold outline -->
    <rect x="500" y="110" width="110" height="210" fill="#161b22" stroke="#d4af37" stroke-width="3"/>
    <polygon points="500,110 555,60 610,110" fill="#161b22" stroke="#d4af37" stroke-width="3"/>
    <line x1="555" y1="60" x2="555" y2="35" stroke="#d4af37" stroke-width="3"/>
    <line x1="543" y1="45" x2="567" y2="45" stroke="#d4af37" stroke-width="3"/>

    <!-- a few lit windows -->
    <rect x="45" y="200" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="75" y="230" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="150" y="160" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="970" y="230" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>

    <!-- coin icon -->
    <circle cx="960" cy="70" r="34" fill="#d29922" stroke="#8a6d1f" stroke-width="3"/>
    <text x="960" y="80" text-anchor="middle" font-size="34" font-weight="bold" fill="#161b22">$</text>

    <!-- street-level car -->
    <rect x="330" y="290" width="120" height="30" rx="10" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
    <rect x="350" y="270" width="70" height="26" rx="8" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
    <circle cx="355" cy="322" r="12" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
    <circle cx="425" cy="322" r="12" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_2 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 2 - The City Is the Playground</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>The City Is the Playground</h1>
  <svg width="1100" height="340" viewBox="0 0 1100 340">
    <!-- Panel 1: DRIVE -->
    <rect x="20" y="20" width="330" height="300" rx="16" fill="#161b22" stroke="#58a6ff" stroke-width="3"/>
    <text x="185" y="60" text-anchor="middle" class="box-label" font-size="22">DRIVE</text>
    <rect x="105" y="170" width="160" height="40" rx="14" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
    <rect x="130" y="140" width="110" height="34" rx="10" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
    <circle cx="135" cy="215" r="16" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>
    <circle cx="235" cy="215" r="16" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>

    <!-- Panel 2: CASINO -->
    <rect x="385" y="20" width="330" height="300" rx="16" fill="#161b22" stroke="#f78166" stroke-width="3"/>
    <text x="550" y="60" text-anchor="middle" class="box-label" font-size="22">CASINO</text>
    <circle cx="510" cy="190" r="34" fill="#f78166" stroke="#8a3b1f" stroke-width="3"/>
    <circle cx="590" cy="190" r="34" fill="#3fb950" stroke="#1f6f2f" stroke-width="3"/>
    <path d="M550 150 L570 195 L550 220 L530 195 Z" fill="#d29922" stroke="#8a6d1f" stroke-width="2"/>

    <!-- Panel 3: CHAPEL -->
    <rect x="750" y="20" width="330" height="300" rx="16" fill="#161b22" stroke="#d4af37" stroke-width="3"/>
    <text x="915" y="60" text-anchor="middle" class="box-label" font-size="22">CHAPEL</text>
    <rect x="865" y="160" width="100" height="120" fill="#0d1117" stroke="#d4af37" stroke-width="3"/>
    <polygon points="865,160 915,120 965,160" fill="#0d1117" stroke="#d4af37" stroke-width="3"/>
    <line x1="915" y1="120" x2="915" y2="95" stroke="#d4af37" stroke-width="3"/>
    <line x1="903" y1="105" x2="927" y2="105" stroke="#d4af37" stroke-width="3"/>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_3 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 3 - The Feed Moves the Market</title>
<style>""" + VISUAL_CSS + """</style>
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

VISUAL_SLIDE_4 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 4 - Next: Make the World Feel Alive</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Next: Make the World Feel Alive</h1>
  <svg width="1100" height="300" viewBox="0 0 1100 300">
    <defs>
      <marker id="roadmapArrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>
    <line x1="60" y1="150" x2="1040" y2="150" stroke="#30363d" stroke-width="4" marker-end="url(#roadmapArrow)"/>

    <circle cx="120" cy="150" r="28" fill="#161b22" stroke="#58a6ff" stroke-width="3"/>
    <text x="120" y="200" text-anchor="middle" class="box-label" font-size="15">Smarter NPCs</text>

    <circle cx="380" cy="150" r="28" fill="#161b22" stroke="#f78166" stroke-width="3"/>
    <text x="380" y="110" text-anchor="middle" class="box-label" font-size="15">Phone UI</text>

    <circle cx="640" cy="150" r="28" fill="#161b22" stroke="#3fb950" stroke-width="3"/>
    <text x="640" y="200" text-anchor="middle" class="box-label" font-size="15">Social &#8594; Price</text>

    <circle cx="900" cy="150" r="28" fill="#161b22" stroke="#d29922" stroke-width="3"/>
    <text x="900" y="110" text-anchor="middle" class="box-label" font-size="15">Crime &amp; Jail</text>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_TEMPLATES = {
    1: VISUAL_SLIDE_1,
    2: VISUAL_SLIDE_2,
    3: VISUAL_SLIDE_3,
    4: VISUAL_SLIDE_4,
}


def visual_slide_html(slide: Slide, index: int) -> str:
    template = VISUAL_TEMPLATES.get(index)
    if template is None:
        return slide_to_html(slide, index)
    return template.replace("__NARRATION__", slide.narration)


def render_slides(slides: list[Slide], out_dir: str = "slides") -> list[str]:
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, slide in enumerate(slides, start=1):
        path = os.path.join(out_dir, f"slide_{i}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(visual_slide_html(slide, i))
        paths.append(path)
    return paths
