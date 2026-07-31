"""Renders each Slide into a standalone HTML file under slides/.

All 6 slides get a real HTML/CSS/SVG illustration (only 1 is required by
the HW2 spec, but we're doing all of them for a more consistent-looking
video). slide_to_html() below is kept as a plain-text fallback for any
slide index beyond the 6 we've hand-illustrated.
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
    background: radial-gradient(circle at 50% 25%, #1a2036 0%, #0d1117 65%);
    color: #f0f6fc;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    padding: 40px;
  }
  h1 {
    font-size: 42px;
    margin-bottom: 8px;
    font-weight: 800;
    background: linear-gradient(90deg, #79c0ff, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.6));
  }
  .caption {
    font-size: 20px;
    max-width: 920px;
    text-align: center;
    margin-top: 26px;
    color: #c9d1d9;
    line-height: 1.5;
  }
  .box-label { font-size: 18px; font-weight: bold; fill: #f0f6fc; }
"""

# Shared <defs> reused by every illustrated slide: a soft glow filter for
# "highlight" elements and a drop-shadow filter for panels/buildings, both
# of which are what actually reads as "depth" once rendered.
SHARED_DEFS = """
      <linearGradient id="panelGradient" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#1c2333"/>
        <stop offset="100%" stop-color="#0d1117"/>
      </linearGradient>
      <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <filter id="dropshadow" x="-30%" y="-30%" width="160%" height="160%">
        <feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000000" flood-opacity="0.5"/>
      </filter>
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
    <defs>""" + SHARED_DEFS + """
      <linearGradient id="skyGradient" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#20264a"/>
        <stop offset="100%" stop-color="#0d1117"/>
      </linearGradient>
      <radialGradient id="spotlight" cx="50%" cy="55%" r="50%">
        <stop offset="0%" stop-color="#d4af37" stop-opacity="0.28"/>
        <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect x="0" y="0" width="1100" height="340" fill="url(#skyGradient)"/>
    <ellipse cx="555" cy="230" rx="270" ry="190" fill="url(#spotlight)"/>

    <!-- stars -->
    <circle cx="80" cy="40" r="2" fill="#f0f6fc" opacity="0.6"/>
    <circle cx="220" cy="25" r="1.5" fill="#f0f6fc" opacity="0.5"/>
    <circle cx="780" cy="35" r="2" fill="#f0f6fc" opacity="0.6"/>
    <circle cx="1000" cy="50" r="1.5" fill="#f0f6fc" opacity="0.5"/>
    <circle cx="650" cy="20" r="1.5" fill="#f0f6fc" opacity="0.4"/>

    <!-- skyline -->
    <rect x="30"  y="180" width="90"  height="140" fill="url(#panelGradient)" stroke="#30363d" stroke-width="2" filter="url(#dropshadow)"/>
    <rect x="130" y="130" width="70"  height="190" fill="url(#panelGradient)" stroke="#30363d" stroke-width="2" filter="url(#dropshadow)"/>
    <rect x="210" y="210" width="100" height="110" fill="url(#panelGradient)" stroke="#30363d" stroke-width="2" filter="url(#dropshadow)"/>
    <rect x="850" y="160" width="80"  height="160" fill="url(#panelGradient)" stroke="#30363d" stroke-width="2" filter="url(#dropshadow)"/>
    <rect x="950" y="200" width="110" height="120" fill="url(#panelGradient)" stroke="#30363d" stroke-width="2" filter="url(#dropshadow)"/>

    <!-- chapel, the landmark - taller, gold outline, glowing -->
    <g filter="url(#glow)">
      <rect x="500" y="110" width="110" height="210" fill="url(#panelGradient)" stroke="#d4af37" stroke-width="3"/>
      <polygon points="500,110 555,60 610,110" fill="url(#panelGradient)" stroke="#d4af37" stroke-width="3"/>
      <line x1="555" y1="60" x2="555" y2="35" stroke="#d4af37" stroke-width="3"/>
      <line x1="543" y1="45" x2="567" y2="45" stroke="#d4af37" stroke-width="3"/>
    </g>

    <!-- lit windows -->
    <rect x="45" y="200" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="75" y="230" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="150" y="160" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="970" y="230" width="14" height="14" fill="#f0f6fc" opacity="0.5"/>
    <rect x="540" y="150" width="14" height="14" fill="#ffd76b" opacity="0.85"/>
    <rect x="565" y="200" width="14" height="14" fill="#ffd76b" opacity="0.85"/>

    <!-- coin icon, glowing -->
    <g filter="url(#glow)">
      <circle cx="960" cy="70" r="34" fill="#d29922" stroke="#8a6d1f" stroke-width="3"/>
      <text x="960" y="80" text-anchor="middle" font-size="34" font-weight="bold" fill="#161b22">$</text>
    </g>

    <!-- street-level car -->
    <g filter="url(#dropshadow)">
      <rect x="330" y="290" width="120" height="30" rx="10" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
      <rect x="350" y="270" width="70" height="26" rx="8" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
      <circle cx="355" cy="322" r="12" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
      <circle cx="425" cy="322" r="12" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
    </g>
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
    <defs>""" + SHARED_DEFS + """</defs>

    <!-- Panel 1: DRIVE -->
    <rect x="20" y="20" width="330" height="300" rx="16" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="185" y="60" text-anchor="middle" class="box-label" font-size="22">DRIVE</text>
    <g filter="url(#glow)">
      <rect x="105" y="170" width="160" height="40" rx="14" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
      <rect x="130" y="140" width="110" height="34" rx="10" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
    </g>
    <circle cx="135" cy="215" r="16" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>
    <circle cx="235" cy="215" r="16" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>

    <!-- Panel 2: CASINO -->
    <rect x="385" y="20" width="330" height="300" rx="16" fill="url(#panelGradient)" stroke="#f78166" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="550" y="60" text-anchor="middle" class="box-label" font-size="22">CASINO</text>
    <g filter="url(#glow)">
      <circle cx="510" cy="190" r="34" fill="#f78166" stroke="#8a3b1f" stroke-width="3"/>
      <circle cx="590" cy="190" r="34" fill="#3fb950" stroke="#1f6f2f" stroke-width="3"/>
      <path d="M550 150 L570 195 L550 220 L530 195 Z" fill="#d29922" stroke="#8a6d1f" stroke-width="2"/>
    </g>

    <!-- Panel 3: CHAPEL -->
    <rect x="750" y="20" width="330" height="300" rx="16" fill="url(#panelGradient)" stroke="#d4af37" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="915" y="60" text-anchor="middle" class="box-label" font-size="22">CHAPEL</text>
    <g filter="url(#glow)">
      <rect x="865" y="160" width="100" height="120" fill="#0d1117" stroke="#d4af37" stroke-width="3"/>
      <polygon points="865,160 915,120 965,160" fill="#0d1117" stroke="#d4af37" stroke-width="3"/>
      <line x1="915" y1="120" x2="915" y2="95" stroke="#d4af37" stroke-width="3"/>
      <line x1="903" y1="105" x2="927" y2="105" stroke="#d4af37" stroke-width="3"/>
    </g>
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
    <defs>""" + SHARED_DEFS + """
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
    <rect x="20" y="120" width="220" height="120" rx="16" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="130" y="165" text-anchor="middle" class="box-label">AI-Generated</text>
    <text x="130" y="190" text-anchor="middle" class="box-label">Social Post</text>
    <g filter="url(#glow)">
      <text x="130" y="222" text-anchor="middle" font-size="28">&#128241;</text>
    </g>

    <path d="M250 180 L340 180" stroke="#8b949e" stroke-width="4" marker-end="url(#arrow)"/>

    <!-- Box 2: Sentiment meter -->
    <rect x="350" y="120" width="260" height="120" rx="16" fill="url(#panelGradient)" stroke="#f78166" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="480" y="150" text-anchor="middle" class="box-label">Sentiment Meter</text>
    <g filter="url(#glow)">
      <rect x="375" y="175" width="210" height="18" rx="9" fill="url(#sentimentGradient)"/>
      <circle cx="530" cy="184" r="9" fill="#f0f6fc" stroke="#0d1117" stroke-width="2"/>
    </g>
    <text x="480" y="222" text-anchor="middle" font-size="14" fill="#c9d1d9">panic &#8594; hype</text>

    <path d="M620 180 L710 180" stroke="#8b949e" stroke-width="4" marker-end="url(#arrow)"/>

    <!-- Box 3: Stock price chart -->
    <rect x="720" y="120" width="360" height="180" rx="16" fill="url(#panelGradient)" stroke="#3fb950" stroke-width="3" filter="url(#dropshadow)"/>
    <text x="900" y="150" text-anchor="middle" class="box-label">Stock Price</text>
    <g filter="url(#glow)">
      <polyline points="740,240 780,220 820,255 860,190 900,210 940,160 980,180 1020,140 1060,150"
                fill="none" stroke="#3fb950" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_4 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 4 - The Goal</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>The Goal</h1>
  <svg width="1100" height="340" viewBox="0 0 1100 340">
    <defs>""" + SHARED_DEFS + """</defs>

    <line x1="60" y1="300" x2="1040" y2="300" stroke="#30363d" stroke-width="3"/>

    <!-- 5-tier milestone ladder: the real win condition -->
    <rect x="90"  y="260" width="100" height="40"  rx="8" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
    <text x="140" y="245" text-anchor="middle" class="box-label" font-size="16">$50k</text>

    <rect x="230" y="220" width="100" height="80"  rx="8" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
    <text x="280" y="205" text-anchor="middle" class="box-label" font-size="16">$250k</text>

    <rect x="370" y="170" width="100" height="130" rx="8" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
    <text x="420" y="155" text-anchor="middle" class="box-label" font-size="16">$1M</text>

    <rect x="510" y="110" width="100" height="190" rx="8" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
    <text x="560" y="95" text-anchor="middle" class="box-label" font-size="16">$5M</text>

    <g filter="url(#glow)">
      <rect x="650" y="50" width="110" height="250" rx="8" fill="url(#panelGradient)" stroke="#d29922" stroke-width="3"/>
    </g>
    <text x="705" y="35" text-anchor="middle" class="box-label" font-size="20">$10M</text>
    <text x="705" y="150" text-anchor="middle" class="box-label" font-size="15" fill="#d29922">THE</text>
    <text x="705" y="172" text-anchor="middle" class="box-label" font-size="15" fill="#d29922">REAL</text>
    <text x="705" y="194" text-anchor="middle" class="box-label" font-size="15" fill="#d29922">WIN</text>

    <!-- flex goal beyond - deliberately faded/dashed, not the real target -->
    <line x1="820" y1="300" x2="820" y2="40" stroke="#30363d" stroke-width="2" stroke-dasharray="6,6"/>
    <rect x="860" y="70" width="150" height="230" rx="8" fill="none" stroke="#8b949e" stroke-width="2" stroke-dasharray="8,6" opacity="0.6"/>
    <text x="935" y="55" text-anchor="middle" class="box-label" font-size="16" fill="#8b949e" opacity="0.8">$1B</text>
    <text x="935" y="190" text-anchor="middle" font-size="14" fill="#8b949e" opacity="0.8">flex goal</text>
    <text x="935" y="210" text-anchor="middle" font-size="14" fill="#8b949e" opacity="0.8">(optional)</text>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_5 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 5 - How It's Built</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>How It's Built</h1>
  <svg width="1100" height="300" viewBox="0 0 1100 300">
    <defs>""" + SHARED_DEFS + """
      <marker id="buildArrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>

    <!-- 10 specialist agents, 2 rows of 5 -->
    <g class="box-label">
      <rect x="20"  y="60"  width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
      <text x="90" y="86" text-anchor="middle" font-size="12" fill="#f0f6fc">Producer</text>

      <rect x="172" y="60"  width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
      <text x="242" y="86" text-anchor="middle" font-size="12" fill="#f0f6fc">Game Designer</text>

      <rect x="324" y="60"  width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
      <text x="394" y="86" text-anchor="middle" font-size="12" fill="#f0f6fc">World-Builder</text>

      <rect x="476" y="60"  width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
      <text x="546" y="86" text-anchor="middle" font-size="12" fill="#f0f6fc">Gameplay Eng.</text>

      <rect x="628" y="60"  width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2"/>
      <text x="698" y="86" text-anchor="middle" font-size="12" fill="#f0f6fc">Art Director</text>

      <rect x="20"  y="120" width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
      <text x="90" y="146" text-anchor="middle" font-size="12" fill="#f0f6fc">Visual Polish</text>

      <rect x="172" y="120" width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
      <text x="242" y="146" text-anchor="middle" font-size="12" fill="#f0f6fc">Tech Artist</text>

      <rect x="324" y="120" width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
      <text x="394" y="146" text-anchor="middle" font-size="12" fill="#f0f6fc">Audio Director</text>

      <rect x="476" y="120" width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
      <text x="546" y="146" text-anchor="middle" font-size="12" fill="#f0f6fc">Writer</text>

      <rect x="628" y="120" width="140" height="42" rx="10" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2"/>
      <text x="698" y="146" text-anchor="middle" font-size="12" fill="#f0f6fc">QA Tester</text>
    </g>

    <path d="M780 120 L840 120" stroke="#8b949e" stroke-width="4" marker-end="url(#buildArrow)"/>

    <g filter="url(#glow)">
      <rect x="850" y="60" width="220" height="180" rx="16" fill="url(#panelGradient)" stroke="#3fb950" stroke-width="3"/>
    </g>
    <text x="960" y="140" text-anchor="middle" class="box-label" font-size="17">Capital</text>
    <text x="960" y="162" text-anchor="middle" class="box-label" font-size="17">Syndicate</text>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_6 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 6 - Next: Make the World Feel Alive</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Next: Make the World Feel Alive</h1>
  <svg width="1100" height="300" viewBox="0 0 1100 300">
    <defs>""" + SHARED_DEFS + """
      <linearGradient id="roadGradient" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#58a6ff"/>
        <stop offset="35%" stop-color="#f78166"/>
        <stop offset="70%" stop-color="#3fb950"/>
        <stop offset="100%" stop-color="#d29922"/>
      </linearGradient>
      <marker id="roadmapArrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>
    <line x1="60" y1="150" x2="1040" y2="150" stroke="url(#roadGradient)" stroke-width="5" marker-end="url(#roadmapArrow)"/>

    <g filter="url(#glow)">
      <circle cx="120" cy="150" r="28" fill="#161b22" stroke="#58a6ff" stroke-width="3"/>
    </g>
    <text x="120" y="200" text-anchor="middle" class="box-label" font-size="15">Smarter NPCs</text>

    <g filter="url(#glow)">
      <circle cx="380" cy="150" r="28" fill="#161b22" stroke="#f78166" stroke-width="3"/>
    </g>
    <text x="380" y="110" text-anchor="middle" class="box-label" font-size="15">Phone UI</text>

    <g filter="url(#glow)">
      <circle cx="640" cy="150" r="28" fill="#161b22" stroke="#3fb950" stroke-width="3"/>
    </g>
    <text x="640" y="200" text-anchor="middle" class="box-label" font-size="15">Social &#8594; Price</text>

    <g filter="url(#glow)">
      <circle cx="900" cy="150" r="28" fill="#161b22" stroke="#d29922" stroke-width="3"/>
    </g>
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
    5: VISUAL_SLIDE_5,
    6: VISUAL_SLIDE_6,
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
