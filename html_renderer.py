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
    font-size: 48px;
    margin-bottom: 8px;
    font-weight: 800;
    background: linear-gradient(90deg, #79c0ff, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.6));
  }
  .caption {
    font-size: 24px;
    max-width: 960px;
    text-align: center;
    margin-top: 22px;
    color: #c9d1d9;
    line-height: 1.5;
  }
  .box-label { font-size: 22px; font-weight: bold; fill: #f0f6fc; }
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
<title>Slide 1 - Capital Syndicate: $0 to $10M</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Capital Syndicate</h1>
  <div class="caption" style="margin-top:-4px; margin-bottom:14px; font-size:22px; font-weight:700; color:#d4af37; letter-spacing:2px;">$0 &#8594; $10M</div>
  <svg width="1140" height="330" viewBox="0 0 1140 330">
    <defs>""" + SHARED_DEFS + """
      <linearGradient id="skyGradient" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#20264a"/>
        <stop offset="100%" stop-color="#0d1117"/>
      </linearGradient>
      <radialGradient id="spotlight" cx="50%" cy="55%" r="50%">
        <stop offset="0%" stop-color="#d4af37" stop-opacity="0.22"/>
        <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect x="0" y="0" width="1140" height="330" fill="url(#skyGradient)"/>
    <ellipse cx="570" cy="230" rx="320" ry="180" fill="url(#spotlight)"/>

    <!-- moon + stars -->
    <g filter="url(#glow)">
      <circle cx="570" cy="60" r="26" fill="#f0f6fc" opacity="0.9"/>
      <circle cx="580" cy="52" r="26" fill="#0d1117" opacity="0.5"/>
    </g>
    <circle cx="80" cy="30" r="2" fill="#f0f6fc" opacity="0.6"/>
    <circle cx="260" cy="18" r="1.5" fill="#f0f6fc" opacity="0.5"/>
    <circle cx="880" cy="25" r="2" fill="#f0f6fc" opacity="0.6"/>
    <circle cx="1060" cy="45" r="1.5" fill="#f0f6fc" opacity="0.5"/>
    <circle cx="380" cy="35" r="1.5" fill="#f0f6fc" opacity="0.4"/>
    <circle cx="760" cy="20" r="1.5" fill="#f0f6fc" opacity="0.4"/>

    <!-- distant skyline silhouette, low opacity for depth -->
    <g opacity="0.35" fill="#161b22">
      <rect x="0" y="230" width="55" height="70"/>
      <rect x="60" y="200" width="40" height="100"/>
      <rect x="620" y="215" width="45" height="85"/>
      <rect x="1090" y="210" width="50" height="90"/>
    </g>

    <!-- background hub: the Whispering Temple Chapel, distant silhouette -->
    <g opacity="0.35" fill="#161b22">
      <rect x="185" y="245" width="42" height="55" stroke="#8b949e" stroke-width="1"/>
      <path d="M185 245 L206 218 L227 245 Z" stroke="#8b949e" stroke-width="1"/>
      <line x1="206" y1="218" x2="206" y2="196" stroke="#8b949e" stroke-width="2"/>
      <line x1="199" y1="204" x2="213" y2="204" stroke="#8b949e" stroke-width="2"/>
    </g>

    <!-- background hub: Neon Dragon Casino / entertainment complex, distant silhouette -->
    <g opacity="0.35" fill="#161b22">
      <rect x="675" y="210" width="45" height="90" stroke="#8b949e" stroke-width="1"/>
      <ellipse cx="697" cy="210" rx="24" ry="16" stroke="#8b949e" stroke-width="1"/>
      <path d="M697 178 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3 z" opacity="0.7"/>
    </g>

    <!-- background hub: The Underworld, distant silhouette with a jagged roofline -->
    <g opacity="0.35" fill="#161b22">
      <path d="M800 300 L800 248 L813 236 L822 250 L833 238 L845 252 L860 240 L860 300 Z" stroke="#8b949e" stroke-width="1"/>
      <circle cx="822" cy="255" r="2.5" fill="#f85149" opacity="0.8"/>
    </g>

    <!-- dark-market alley hint: flickering red neon between INVEST and RISK -->
    <g filter="url(#glow)">
      <rect x="800" y="30" width="4" height="30" fill="#f85149" opacity="0.7"/>
      <text x="802" y="70" text-anchor="middle" font-size="14" fill="#f85149" opacity="0.85">?</text>
    </g>

    <!-- road -->
    <path d="M0 300 L1140 300" stroke="#30363d" stroke-width="26"/>
    <path d="M0 300 L1140 300" stroke="#f0f6fc" stroke-width="2" stroke-dasharray="20,18" opacity="0.4"/>

    <!-- WORK marker: office tower, blue -->
    <g>
      <rect x="60" y="140" width="90" height="160" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2" filter="url(#dropshadow)"/>
      <rect x="75" y="160" width="14" height="14" fill="#58a6ff" opacity="0.7"/>
      <rect x="100" y="160" width="14" height="14" fill="#58a6ff" opacity="0.5"/>
      <rect x="75" y="190" width="14" height="14" fill="#58a6ff" opacity="0.5"/>
      <rect x="100" y="190" width="14" height="14" fill="#58a6ff" opacity="0.7"/>
      <g filter="url(#glow)">
        <circle cx="105" cy="105" r="30" fill="#161b22" stroke="#58a6ff" stroke-width="3"/>
        <rect x="93" y="98" width="10" height="16" fill="#58a6ff"/>
        <rect x="107" y="92" width="10" height="22" fill="#58a6ff"/>
      </g>
      <text x="105" y="60" text-anchor="middle" class="box-label" font-size="21" fill="#58a6ff">WORK</text>
      <!-- pennant flag -->
      <line x1="105" y1="140" x2="105" y2="118" stroke="#8b949e" stroke-width="2"/>
      <path d="M105 118 L128 126 L105 134 Z" fill="#58a6ff"/>
    </g>

    <!-- INVEST marker: stock tower with ticker, green -->
    <g>
      <rect x="490" y="120" width="100" height="180" fill="url(#panelGradient)" stroke="#3fb950" stroke-width="2" filter="url(#dropshadow)"/>
      <g filter="url(#glow)">
        <polyline points="500,260 520,240 540,255 560,215 580,230" fill="none" stroke="#3fb950" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      </g>
      <g filter="url(#glow)">
        <circle cx="540" cy="80" r="30" fill="#161b22" stroke="#3fb950" stroke-width="3"/>
        <polyline points="527,88 535,75 543,82 553,68" fill="none" stroke="#3fb950" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      </g>
      <text x="540" y="40" text-anchor="middle" class="box-label" font-size="21" fill="#3fb950">INVEST</text>
      <!-- pennant flag -->
      <line x1="540" y1="120" x2="540" y2="98" stroke="#8b949e" stroke-width="2"/>
      <path d="M540 98 L563 106 L540 114 Z" fill="#3fb950"/>
    </g>

    <!-- RISK marker: casino tower with chip/die, gold/red -->
    <g>
      <rect x="960" y="130" width="110" height="170" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2" filter="url(#dropshadow)"/>
      <rect x="985" y="160" width="16" height="16" fill="#d29922" opacity="0.8"/>
      <rect x="1015" y="180" width="16" height="16" fill="#f78166" opacity="0.8"/>
      <rect x="985" y="200" width="16" height="16" fill="#3fb950" opacity="0.6"/>
      <g filter="url(#glow)">
        <circle cx="1015" cy="95" r="30" fill="#d29922" stroke="#8a6d1f" stroke-width="3"/>
        <circle cx="1008" cy="88" r="3" fill="#161b22"/>
        <circle cx="1022" cy="88" r="3" fill="#161b22"/>
        <circle cx="1015" cy="98" r="3" fill="#161b22"/>
        <circle cx="1008" cy="106" r="3" fill="#161b22"/>
        <circle cx="1022" cy="106" r="3" fill="#161b22"/>
      </g>
      <text x="1015" y="55" text-anchor="middle" class="box-label" font-size="21" fill="#f78166">RISK</text>
      <!-- pennant flag -->
      <line x1="1015" y1="130" x2="1015" y2="108" stroke="#8b949e" stroke-width="2"/>
      <path d="M1015 108 L1038 116 L1015 124 Z" fill="#d29922"/>
    </g>

    <!-- fishing dock hint, bottom left, with an angler figure -->
    <g filter="url(#dropshadow)">
      <rect x="230" y="290" width="70" height="8" fill="#8b5a2b"/>
      <circle cx="248" cy="278" r="7" fill="#c9d1d9"/>
      <path d="M240 285 L256 285 L254 300 L242 300 Z" fill="#c9d1d9"/>
      <line x1="255" y1="290" x2="255" y2="255" stroke="#c9d1d9" stroke-width="2"/>
      <line x1="255" y1="255" x2="285" y2="260" stroke="#c9d1d9" stroke-width="2"/>
      <line x1="285" y1="260" x2="285" y2="272" stroke="#8b949e" stroke-width="1.5"/>
      <path d="M700 305 q20 -10 40 0" stroke="#58a6ff" stroke-width="3" fill="none" opacity="0.7"/>
    </g>

    <!-- pedestrian walking toward the WORK tower -->
    <g filter="url(#dropshadow)">
      <circle cx="180" cy="279" r="6" fill="#58a6ff"/>
      <path d="M173 286 L187 286 L185 300 L175 300 Z" fill="#58a6ff"/>
    </g>

    <!-- investor crossing toward the INVEST tower -->
    <g filter="url(#dropshadow)">
      <circle cx="650" cy="279" r="6" fill="#3fb950"/>
      <path d="M643 286 L657 286 L655 300 L645 300 Z" fill="#3fb950"/>
    </g>

    <!-- gambler crossing toward the RISK tower -->
    <g filter="url(#dropshadow)">
      <circle cx="905" cy="279" r="6" fill="#d29922"/>
      <path d="M898 286 L912 286 L910 300 L900 300 Z" fill="#d29922"/>
    </g>

    <!-- hooded figure lurking under the dark-alley neon hint -->
    <g opacity="0.9">
      <path d="M793 279 Q800 267 807 279 L807 300 L793 300 Z" fill="#f85149"/>
    </g>

    <!-- player car cruising the road, headlight glow + speed streaks -->
    <g filter="url(#glow)">
      <ellipse cx="445" cy="284" rx="26" ry="10" fill="#ffe08a" opacity="0.5"/>
    </g>
    <g filter="url(#dropshadow)">
      <path d="M330 296 L336 274 Q344 262 362 262 L400 262 Q412 262 420 274 L432 274 L440 288 L440 296 Z" fill="#d4af37" stroke="#8a6d1f" stroke-width="2"/>
      <rect x="355" y="250" width="52" height="20" rx="7" fill="#1c2333" stroke="#8a6d1f" stroke-width="2"/>
      <circle cx="354" cy="298" r="11" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
      <circle cx="418" cy="298" r="11" fill="#0d1117" stroke="#8b949e" stroke-width="2"/>
      <circle cx="437" cy="285" r="4" fill="#ffe08a"/>
    </g>
    <line x1="290" y1="280" x2="322" y2="280" stroke="#f0f6fc" stroke-width="2" opacity="0.5"/>
    <line x1="280" y1="268" x2="318" y2="268" stroke="#f0f6fc" stroke-width="2" opacity="0.35"/>
    <line x1="270" y1="292" x2="310" y2="292" stroke="#f0f6fc" stroke-width="2" opacity="0.3"/>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_2 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 2 - Drive. Risk. Escape.</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Drive. Risk. Escape.</h1>
  <svg width="1140" height="330" viewBox="0 0 1140 330">
    <defs>""" + SHARED_DEFS + """
      <marker id="policeArrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>

    <!-- dashed film-reel path connecting the three tilted panels -->
    <path d="M192 315 Q 567 355 945 315" fill="none" stroke="#8b949e" stroke-width="2" stroke-dasharray="6,6" opacity="0.4"/>

    <!-- Panel 1: DRIVE (tilted -4deg) -->
    <g transform="rotate(-4 192.5 165)">
      <rect x="12" y="12" width="361" height="306" rx="14" fill="#f0f6fc" filter="url(#dropshadow)"/>
      <clipPath id="drivePanelClip"><rect x="20" y="20" width="345" height="290" rx="16"/></clipPath>
      <rect x="20" y="20" width="345" height="290" rx="16" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="3"/>
      <g clip-path="url(#drivePanelClip)" opacity="0.5">
        <line x1="0" y1="90" x2="200" y2="20" stroke="#58a6ff" stroke-width="10"/>
        <line x1="0" y1="150" x2="260" y2="20" stroke="#58a6ff" stroke-width="10"/>
        <line x1="0" y1="310" x2="365" y2="150" stroke="#58a6ff" stroke-width="10"/>
      </g>
      <text x="192" y="55" text-anchor="middle" class="box-label" font-size="25" fill="#58a6ff">DRIVE</text>
      <g filter="url(#glow)">
        <ellipse cx="255" cy="210" rx="24" ry="9" fill="#ffe08a" opacity="0.6"/>
        <rect x="110" y="175" width="165" height="38" rx="13" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
        <rect x="135" y="146" width="110" height="34" rx="10" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
      </g>
      <circle cx="140" cy="218" r="15" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>
      <circle cx="240" cy="218" r="15" fill="#0d1117" stroke="#8b949e" stroke-width="3"/>
      <!-- motion / smoke lines -->
      <line x1="60" y1="200" x2="100" y2="200" stroke="#f0f6fc" stroke-width="3" opacity="0.5"/>
      <line x1="55" y1="215" x2="95" y2="215" stroke="#f0f6fc" stroke-width="3" opacity="0.35"/>
      <line x1="65" y1="230" x2="100" y2="230" stroke="#f0f6fc" stroke-width="3" opacity="0.25"/>
      <text x="192" y="270" text-anchor="middle" font-size="17" fill="#c9d1d9">tear through the city</text>
      <circle cx="24" cy="24" r="15" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
      <text x="24" y="29" text-anchor="middle" font-size="17" font-weight="bold" fill="#58a6ff">1</text>
    </g>

    <!-- Panel 2: RISK (flat, popped forward) -->
    <g transform="translate(0 -14)">
      <rect x="387" y="12" width="361" height="306" rx="14" fill="#f0f6fc" filter="url(#dropshadow)"/>
      <rect x="395" y="20" width="345" height="290" rx="16" fill="url(#panelGradient)" stroke="#d29922" stroke-width="3"/>
      <text x="567" y="55" text-anchor="middle" class="box-label" font-size="25" fill="#d29922">RISK</text>
      <!-- slot reel peeking behind the table -->
      <g opacity="0.55">
        <rect x="530" y="70" width="26" height="34" rx="4" fill="#161b22" stroke="#d29922" stroke-width="2"/>
        <text x="543" y="94" text-anchor="middle" font-size="21" fill="#d29922">7</text>
        <rect x="560" y="70" width="26" height="34" rx="4" fill="#161b22" stroke="#d29922" stroke-width="2"/>
        <text x="573" y="94" text-anchor="middle" font-size="21" fill="#f78166">&#9733;</text>
        <rect x="590" y="70" width="26" height="34" rx="4" fill="#161b22" stroke="#d29922" stroke-width="2"/>
        <text x="603" y="94" text-anchor="middle" font-size="21" fill="#d29922">7</text>
      </g>
      <!-- casino table -->
      <ellipse cx="567" cy="215" rx="130" ry="55" fill="#0d3b26" stroke="#1f6f2f" stroke-width="3"/>
      <g filter="url(#glow)">
        <!-- cards fanned -->
        <rect x="500" y="150" width="40" height="58" rx="6" fill="#f0f6fc" stroke="#8b949e" stroke-width="2" transform="rotate(-12 520 179)"/>
        <rect x="545" y="145" width="40" height="58" rx="6" fill="#f0f6fc" stroke="#8b949e" stroke-width="2"/>
        <rect x="588" y="150" width="40" height="58" rx="6" fill="#f0f6fc" stroke="#8b949e" stroke-width="2" transform="rotate(12 608 179)"/>
        <!-- chips -->
        <circle cx="500" cy="235" r="16" fill="#f78166" stroke="#8a3b1f" stroke-width="2"/>
        <circle cx="535" cy="245" r="16" fill="#3fb950" stroke="#1f6f2f" stroke-width="2"/>
        <circle cx="600" cy="245" r="16" fill="#58a6ff" stroke="#1f6feb" stroke-width="2"/>
        <circle cx="635" cy="233" r="16" fill="#d29922" stroke="#8a6d1f" stroke-width="2"/>
      </g>
      <!-- sparkle accents -->
      <g fill="#ffe08a" opacity="0.8">
        <path d="M475 158 l2.5 7 l7 2.5 l-7 2.5 l-2.5 7 l-2.5 -7 l-7 -2.5 l7 -2.5 z"/>
        <path d="M665 178 l2.5 7 l7 2.5 l-7 2.5 l-2.5 7 l-2.5 -7 l-7 -2.5 l7 -2.5 z"/>
      </g>
      <!-- player seated at the table -->
      <g filter="url(#dropshadow)">
        <circle cx="567" cy="242" r="12" fill="#ffe08a"/>
        <path d="M552 254 Q567 236 582 254 L579 268 L555 268 Z" fill="#ffe08a"/>
      </g>
      <text x="567" y="285" text-anchor="middle" font-size="17" fill="#c9d1d9">blackjack &#183; poker &#183; slots</text>
      <circle cx="399" cy="24" r="15" fill="#161b22" stroke="#d29922" stroke-width="2"/>
      <text x="399" y="29" text-anchor="middle" font-size="17" font-weight="bold" fill="#d29922">2</text>
    </g>

    <!-- Panel 3: ESCAPE (tilted +4deg) -->
    <g transform="rotate(4 945 165)">
      <rect x="762" y="12" width="366" height="306" rx="14" fill="#f0f6fc" filter="url(#dropshadow)"/>
      <clipPath id="escapePanelClip"><rect x="770" y="20" width="350" height="290" rx="16"/></clipPath>
      <rect x="770" y="20" width="350" height="290" rx="16" fill="url(#panelGradient)" stroke="#f85149" stroke-width="3"/>
      <g clip-path="url(#escapePanelClip)">
        <circle cx="900" cy="110" r="34" fill="none" stroke="#f85149" stroke-width="2" opacity="0.35"/>
        <circle cx="900" cy="110" r="50" fill="none" stroke="#f85149" stroke-width="2" opacity="0.2"/>
        <circle cx="990" cy="110" r="34" fill="none" stroke="#58a6ff" stroke-width="2" opacity="0.35"/>
        <circle cx="990" cy="110" r="50" fill="none" stroke="#58a6ff" stroke-width="2" opacity="0.2"/>
      </g>
      <text x="945" y="55" text-anchor="middle" class="box-label" font-size="25" fill="#f85149">ESCAPE</text>
      <g filter="url(#glow)">
        <circle cx="900" cy="110" r="20" fill="#f85149"/>
        <circle cx="990" cy="110" r="20" fill="#58a6ff"/>
      </g>
      <!-- jail bars -->
      <rect x="850" y="140" width="190" height="70" fill="#161b22" stroke="#30363d" stroke-width="2"/>
      <!-- prisoner figure behind the bars -->
      <g>
        <circle cx="944" cy="163" r="8" fill="#8b949e"/>
        <path d="M933 172 L955 172 L953 200 L935 200 Z" fill="#8b949e"/>
      </g>
      <line x1="875" y1="140" x2="875" y2="210" stroke="#8b949e" stroke-width="4"/>
      <line x1="905" y1="140" x2="905" y2="210" stroke="#8b949e" stroke-width="4"/>
      <line x1="935" y1="140" x2="935" y2="210" stroke="#8b949e" stroke-width="4"/>
      <line x1="965" y1="140" x2="965" y2="210" stroke="#8b949e" stroke-width="4"/>
      <line x1="995" y1="140" x2="995" y2="210" stroke="#8b949e" stroke-width="4"/>
      <line x1="1020" y1="140" x2="1020" y2="210" stroke="#8b949e" stroke-width="4"/>
      <!-- three choice buttons -->
      <rect x="790" y="235" width="90" height="36" rx="10" fill="#161b22" stroke="#d29922" stroke-width="2"/>
      <text x="835" y="258" text-anchor="middle" font-size="17" fill="#d29922" font-weight="bold">BRIBE</text>
      <rect x="900" y="235" width="90" height="36" rx="10" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
      <text x="945" y="258" text-anchor="middle" font-size="17" fill="#58a6ff" font-weight="bold">TALK</text>
      <rect x="1010" y="235" width="90" height="36" rx="10" fill="#161b22" stroke="#f85149" stroke-width="2"/>
      <text x="1055" y="258" text-anchor="middle" font-size="17" fill="#f85149" font-weight="bold">ESCAPE</text>
      <circle cx="774" cy="24" r="15" fill="#161b22" stroke="#f85149" stroke-width="2"/>
      <text x="774" y="29" text-anchor="middle" font-size="17" font-weight="bold" fill="#f85149">3</text>
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
<title>Slide 3 - AI Is Part of the Game Loop</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>AI Is Part of the Game Loop</h1>
  <svg width="1000" height="360" viewBox="0 0 1000 360">
    <defs>""" + SHARED_DEFS + """
      <marker id="feedArrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#8b949e"/>
      </marker>
    </defs>

    <!-- faint city skyline behind the phone, for depth -->
    <g opacity="0.18" fill="#58a6ff">
      <rect x="60" y="180" width="50" height="150"/>
      <rect x="120" y="140" width="40" height="190"/>
      <rect x="850" y="160" width="45" height="170"/>
      <rect x="905" y="200" width="55" height="130"/>
    </g>

    <!-- faint ambient particles drifting near the phone -->
    <g opacity="0.18" stroke="#8b949e" fill="none" stroke-width="2">
      <path d="M270 40 c-6,-8 -18,-2 -18,7 c0,8 9,12 18,20 c9,-8 18,-12 18,-20 c0,-9 -12,-15 -18,-7 z"/>
      <circle cx="735" cy="45" r="14"/>
      <path d="M730 42 l10 6 l-10 6 z" fill="#8b949e"/>
      <text x="750" y="335" font-size="23" fill="#8b949e" stroke="none">$</text>
    </g>

    <!-- phone body, centered -->
    <g filter="url(#dropshadow)">
      <rect x="360" y="15" width="280" height="330" rx="30" fill="#161b22" stroke="#30363d" stroke-width="4"/>
      <rect x="378" y="40" width="244" height="280" rx="10" fill="url(#panelGradient)"/>
      <rect x="455" y="24" width="90" height="8" rx="4" fill="#30363d"/>
    </g>

    <!-- row 1: social post -> rising chart -->
    <rect x="392" y="54" width="216" height="78" rx="10" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
    <g filter="url(#glow)">
      <circle cx="416" cy="80" r="12" fill="#58a6ff"/>
      <polyline points="560,110 578,95 592,105 608,78" fill="none" stroke="#3fb950" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="440" y="76" font-size="14" fill="#c9d1d9">"$NOVA to the moon"</text>
    <text x="500" y="122" text-anchor="middle" font-size="15" fill="#3fb950" font-weight="bold">MOVE MARKETS</text>

    <!-- row 2: NPC portrait + heart chat -->
    <rect x="392" y="142" width="216" height="78" rx="10" fill="#161b22" stroke="#f78166" stroke-width="2"/>
    <g filter="url(#glow)">
      <!-- historical-figure NPC bust silhouette -->
      <circle cx="418" cy="162" r="12" fill="#d29922" stroke="#8a6d1f" stroke-width="2"/>
      <path d="M400 186 q18 -16 36 0 l0 8 l-36 0 z" fill="#d29922" stroke="#8a6d1f" stroke-width="2"/>
      <path d="M572 158 c-8,-10 -24,-3 -24,9 c0,10 12,16 24,26 c12,-10 24,-16 24,-26 c0,-12 -16,-19 -24,-9 z" fill="#f78166"/>
    </g>
    <text x="500" y="214" text-anchor="middle" font-size="15" fill="#f78166" font-weight="bold">BUILD RELATIONSHIPS</text>

    <!-- row 3: AI assistant Q&A -->
    <rect x="392" y="230" width="216" height="78" rx="10" fill="#161b22" stroke="#d29922" stroke-width="2"/>
    <g filter="url(#glow)">
      <circle cx="418" cy="255" r="14" fill="#0d1117" stroke="#d29922" stroke-width="2"/>
      <text x="418" y="260" text-anchor="middle" font-size="17" fill="#d29922">?</text>
    </g>
    <text x="440" y="252" font-size="13" fill="#c9d1d9">"How does short-selling work?"</text>
    <text x="440" y="270" font-size="13" fill="#3fb950">assistant is typing&#8230;</text>
    <text x="500" y="298" text-anchor="middle" font-size="15" fill="#d29922" font-weight="bold">GET ANSWERS</text>

    <!-- side callouts -->
    <text x="180" y="90" text-anchor="middle" class="box-label" font-size="19" fill="#58a6ff">AI-generated posts</text>
    <text x="180" y="115" text-anchor="middle" font-size="16" fill="#8b949e">move real prices</text>
    <path d="M280 100 L370 90" stroke="#8b949e" stroke-width="3" marker-end="url(#feedArrow)"/>

    <text x="820" y="180" text-anchor="middle" class="box-label" font-size="19" fill="#f78166">76 historical NPCs</text>
    <text x="820" y="205" text-anchor="middle" font-size="16" fill="#8b949e">chat &#183; date &#183; remember</text>
    <path d="M720 181 L630 181" stroke="#8b949e" stroke-width="3" marker-end="url(#feedArrow)"/>

    <text x="180" y="270" text-anchor="middle" class="box-label" font-size="19" fill="#d29922">Ask anything</text>
    <text x="180" y="295" text-anchor="middle" font-size="16" fill="#8b949e">no more guessing</text>
    <path d="M280 268 L370 260" stroke="#8b949e" stroke-width="3" marker-end="url(#feedArrow)"/>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_4 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 4 - The Real Win: $10M</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>The Real Win: $10M</h1>
  <svg width="1120" height="360" viewBox="0 0 1120 360">
    <defs>""" + SHARED_DEFS + """
      <linearGradient id="mountainGradient" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#2d3548"/>
        <stop offset="100%" stop-color="#0d1117"/>
      </linearGradient>
    </defs>

    <!-- faint rising bar-chart pattern in the background -->
    <g opacity="0.12" fill="#3fb950">
      <rect x="40" y="270" width="18" height="30"/>
      <rect x="65" y="250" width="18" height="50"/>
      <rect x="90" y="230" width="18" height="70"/>
      <rect x="1000" y="260" width="18" height="40"/>
      <rect x="1025" y="235" width="18" height="65"/>
      <rect x="1050" y="210" width="18" height="90"/>
    </g>

    <line x1="60" y1="300" x2="1060" y2="300" stroke="#30363d" stroke-width="3"/>

    <!-- ascending staircase-mountain silhouette: one continuous climb, not separate bars -->
    <path d="M60,300 L90,300 L90,260 L190,260 L230,220 L330,220 L370,170 L470,170 L510,110 L610,110 L650,40 L770,40 L800,90 L860,300 Z"
          fill="url(#mountainGradient)" stroke="#30363d" stroke-width="2"/>

    <!-- route path to the summit -->
    <path d="M110,298 Q 250,250 300,225 Q 420,190 460,150 Q 560,100 640,60"
          fill="none" stroke="#8b949e" stroke-width="2" stroke-dasharray="5,6" opacity="0.55"/>

    <text x="140" y="285" text-anchor="middle" class="box-label" font-size="19">$50K</text>
    <text x="280" y="245" text-anchor="middle" class="box-label" font-size="19">$250K</text>
    <text x="420" y="197" text-anchor="middle" class="box-label" font-size="19">$1M</text>
    <text x="560" y="135" text-anchor="middle" class="box-label" font-size="19">$5M</text>

    <!-- flag poles at each plateau -->
    <line x1="140" y1="260" x2="140" y2="235" stroke="#8b949e" stroke-width="2"/>
    <path d="M140 235 L162 242 L140 249 Z" fill="#58a6ff"/>
    <line x1="280" y1="220" x2="280" y2="195" stroke="#8b949e" stroke-width="2"/>
    <path d="M280 195 L302 202 L280 209 Z" fill="#58a6ff"/>
    <line x1="420" y1="170" x2="420" y2="145" stroke="#8b949e" stroke-width="2"/>
    <path d="M420 145 L442 152 L420 159 Z" fill="#f78166"/>
    <line x1="560" y1="110" x2="560" y2="85" stroke="#8b949e" stroke-width="2"/>
    <path d="M560 85 L582 92 L560 99 Z" fill="#f78166"/>

    <!-- $10M peak: bigger, glowing gold flag + WIN CONDITION -->
    <g filter="url(#glow)">
      <line x1="710" y1="40" x2="710" y2="8" stroke="#d29922" stroke-width="3"/>
      <path d="M710 8 L742 18 L710 28 Z" fill="#d29922"/>
    </g>
    <text x="710" y="60" text-anchor="middle" class="box-label" font-size="23" fill="#d29922">$10M</text>
    <text x="725" y="130" text-anchor="middle" class="box-label" font-size="18" fill="#d29922">WIN</text>
    <text x="725" y="150" text-anchor="middle" class="box-label" font-size="18" fill="#d29922">CONDITION</text>
    <!-- coin sparkle accents hugging the peak -->
    <g fill="#ffe08a" opacity="0.85">
      <path d="M655 55 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3 z"/>
      <path d="M790 70 l2.5 6 l6 2.5 l-6 2.5 l-2.5 6 l-2.5 -6 l-6 -2.5 l6 -2.5 z"/>
    </g>

    <!-- "Ways to earn" strip beneath the ladder -->
    <g filter="url(#glow)">
      <circle cx="230" cy="345" r="0" opacity="0"/>
    </g>
    <circle cx="330" cy="340" r="22" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
    <rect x="321" y="331" width="8" height="10" fill="#58a6ff"/>
    <rect x="335" y="327" width="8" height="14" fill="#58a6ff"/>
    <circle cx="470" cy="340" r="22" fill="#161b22" stroke="#f78166" stroke-width="2"/>
    <path d="M457 348 L470 325 L483 348 Z" fill="#f78166"/>
    <circle cx="610" cy="340" r="22" fill="#161b22" stroke="#3fb950" stroke-width="2"/>
    <polyline points="598,346 606,336 614,340 622,328" fill="none" stroke="#3fb950" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="470" y="325" text-anchor="middle" font-size="0"></text>
    <text x="230" y="345" text-anchor="middle" font-size="16" fill="#8b949e">Ways to earn:</text>
    <text x="330" y="378" text-anchor="middle" font-size="14" fill="#8b949e">work</text>
    <text x="470" y="378" text-anchor="middle" font-size="14" fill="#8b949e">risk it</text>
    <text x="610" y="378" text-anchor="middle" font-size="14" fill="#8b949e">invest</text>
  </svg>
  <p class="caption">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_5 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 5 - Built by a Fleet, Not a Generalist</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>Built by a Fleet, Not a Generalist</h1>
  <svg width="1000" height="440" viewBox="0 0 1000 480">
    <defs>""" + SHARED_DEFS + """</defs>

    <!-- spokes: hub to each phase panel -->
    <line x1="500" y1="162" x2="500" y2="125" stroke="#58a6ff" stroke-width="3" opacity="0.6"/>
    <line x1="578" y1="240" x2="690" y2="240" stroke="#f78166" stroke-width="3" opacity="0.6"/>
    <line x1="500" y1="318" x2="500" y2="330" stroke="#bc8cff" stroke-width="3" opacity="0.6"/>
    <line x1="422" y1="240" x2="310" y2="240" stroke="#3fb950" stroke-width="3" opacity="0.6"/>

    <!-- center hub: the shipped build -->
    <g filter="url(#glow)">
      <circle cx="500" cy="240" r="78" fill="url(#panelGradient)" stroke="#d4af37" stroke-width="3"/>
    </g>
    <text x="500" y="234" text-anchor="middle" font-size="20" font-weight="bold" fill="#f0f6fc">Capital</text>
    <text x="500" y="259" text-anchor="middle" font-size="20" font-weight="bold" fill="#f0f6fc">Syndicate</text>

    <!-- PLAN panel (top, blue) -->
    <rect x="330" y="10" width="340" height="115" rx="16" fill="url(#panelGradient)" stroke="#58a6ff" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="500" y="42" text-anchor="middle" font-size="22" font-weight="bold" fill="#58a6ff">PLAN</text>
    <text x="500" y="70" text-anchor="middle" font-size="17" fill="#f0f6fc">Producer</text>
    <text x="500" y="93" text-anchor="middle" font-size="17" fill="#f0f6fc">Game Designer</text>
    <text x="500" y="116" text-anchor="middle" font-size="17" fill="#f0f6fc">World-Builder</text>

    <!-- BUILD panel (right, orange) -->
    <rect x="690" y="183" width="300" height="115" rx="16" fill="url(#panelGradient)" stroke="#f78166" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="840" y="216" text-anchor="middle" font-size="22" font-weight="bold" fill="#f78166">BUILD</text>
    <text x="840" y="248" text-anchor="middle" font-size="17" fill="#f0f6fc">Gameplay Engineer</text>
    <text x="840" y="271" text-anchor="middle" font-size="17" fill="#f0f6fc">Art Director</text>

    <!-- POLISH panel (bottom, purple) -->
    <rect x="320" y="330" width="360" height="140" rx="16" fill="url(#panelGradient)" stroke="#bc8cff" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="500" y="362" text-anchor="middle" font-size="22" font-weight="bold" fill="#bc8cff">POLISH</text>
    <text x="500" y="388" text-anchor="middle" font-size="17" fill="#f0f6fc">Visual Polish</text>
    <text x="500" y="410" text-anchor="middle" font-size="17" fill="#f0f6fc">Tech Artist</text>
    <text x="500" y="432" text-anchor="middle" font-size="17" fill="#f0f6fc">Audio Director</text>
    <text x="500" y="454" text-anchor="middle" font-size="17" fill="#f0f6fc">Writer</text>

    <!-- VERIFY panel (left, green) -->
    <rect x="10" y="183" width="300" height="115" rx="16" fill="url(#panelGradient)" stroke="#3fb950" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="160" y="216" text-anchor="middle" font-size="22" font-weight="bold" fill="#3fb950">VERIFY</text>
    <text x="160" y="250" text-anchor="middle" font-size="17" fill="#f0f6fc">QA Tester</text>
  </svg>
  <p class="caption" style="margin-top:2px; margin-bottom:0;">Narrow roles. Coordinated output. Human product owner.</p>
  <p class="caption" style="margin-top:6px;">__NARRATION__</p>
</body>
</html>
"""

VISUAL_SLIDE_6 = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Slide 6 - What's Next: Fixes, a Clock, an Ending</title>
<style>""" + VISUAL_CSS + """</style>
</head>
<body>
  <h1>What's Next: Fixes, a Clock, an Ending</h1>
  <svg width="1140" height="400" viewBox="0 0 1140 400">
    <defs>""" + SHARED_DEFS + """</defs>

    <!-- countdown badge: real project days remaining -->
    <g filter="url(#glow)">
      <rect x="900" y="15" width="220" height="42" rx="21" fill="#161b22" stroke="#d29922" stroke-width="2"/>
    </g>
    <text x="1010" y="42" text-anchor="middle" font-size="19" font-weight="bold" fill="#d29922">~6 DAYS LEFT</text>

    <!-- LEFT PANEL: the new 30-day in-game clock -->
    <rect x="30" y="72" width="520" height="190" rx="16" fill="url(#panelGradient)" stroke="#d29922" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="290" y="102" text-anchor="middle" class="box-label" font-size="21" fill="#d29922">NEW: 30-DAY CLOCK</text>

    <g filter="url(#dropshadow)">
      <rect x="60" y="120" width="92" height="128" rx="14" fill="#161b22" stroke="#30363d" stroke-width="3"/>
      <rect x="70" y="134" width="72" height="88" rx="6" fill="#0d1117"/>
    </g>
    <text x="106" y="172" text-anchor="middle" font-size="30" font-weight="800" fill="#f0f6fc">30</text>
    <text x="106" y="192" text-anchor="middle" font-size="11" fill="#8b949e">DAY LEFT</text>
    <rect x="79" y="203" width="54" height="6" rx="3" fill="#30363d"/>
    <rect x="79" y="203" width="17" height="6" rx="3" fill="#f85149"/>

    <!-- pressing the existing End Day button, now docked from 30 instead of counting up forever -->
    <g filter="url(#glow)">
      <rect x="182" y="148" width="116" height="44" rx="10" fill="#161b22" stroke="#d29922" stroke-width="2.5"/>
      <text x="240" y="176" text-anchor="middle" font-size="17" font-weight="bold" fill="#d29922">END DAY</text>
    </g>
    <!-- fingertip tapping the button -->
    <path d="M312 132 L294 160" stroke="#c9d1d9" stroke-width="6" stroke-linecap="round"/>
    <circle cx="312" cy="128" r="6" fill="#c9d1d9"/>
    <!-- arrow from the button back to the counter -->
    <path d="M178 170 L162 170" stroke="#f85149" stroke-width="2.5"/>
    <path d="M162 170 L170 165 L170 175 Z" fill="#f85149"/>
    <text x="170" y="145" text-anchor="middle" font-size="13" font-weight="bold" fill="#f85149">-1</text>
    <text x="290" y="228" text-anchor="middle" font-size="14" fill="#c9d1d9">pressing End Day now costs a day off the clock</text>
    <text x="290" y="250" text-anchor="middle" font-size="15" font-weight="bold" fill="#f85149">0 LEFT = GAME OVER</text>

    <!-- RIGHT PANEL: win cutscene replacing the old prison tutorial -->
    <rect x="590" y="72" width="520" height="190" rx="16" fill="url(#panelGradient)" stroke="#d4af37" stroke-width="2.5" filter="url(#dropshadow)"/>
    <text x="850" y="102" text-anchor="middle" class="box-label" font-size="21" fill="#d4af37">NEW: WIN CUTSCENE</text>

    <g filter="url(#glow)" transform="translate(636 120)">
      <rect x="0" y="16" width="78" height="58" rx="6" fill="#161b22" stroke="#d4af37" stroke-width="2.5"/>
      <path d="M0 16 L18 2 L96 2 L78 16 Z" fill="#161b22" stroke="#d4af37" stroke-width="2.5"/>
      <path d="M15 16 L31 2" stroke="#d4af37" stroke-width="3"/>
      <path d="M45 16 L61 2" stroke="#d4af37" stroke-width="3"/>
      <path d="M75 16 L91 2" stroke="#d4af37" stroke-width="3"/>
    </g>

    <!-- triumphant figure at the win line -->
    <g filter="url(#glow)">
      <circle cx="800" cy="155" r="10" fill="#ffe08a"/>
      <path d="M786 170 Q800 150 814 170 L810 205 L790 205 Z" fill="#ffe08a"/>
      <line x1="787" y1="173" x2="772" y2="153" stroke="#ffe08a" stroke-width="3" stroke-linecap="round"/>
      <line x1="813" y1="173" x2="828" y2="153" stroke="#ffe08a" stroke-width="3" stroke-linecap="round"/>
    </g>

    <text x="945" y="155" text-anchor="middle" font-size="26" font-weight="800" fill="#d4af37">$10M</text>
    <text x="945" y="182" text-anchor="middle" font-size="14" fill="#c9d1d9">crossing the line plays the ending</text>
    <text x="850" y="240" text-anchor="middle" font-size="13" fill="#8b949e">a scripted finale for every winning run</text>
    <g fill="#ffe08a" opacity="0.85">
      <path d="M700 92 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3 z"/>
      <path d="M1000 96 l2.5 6 l6 2.5 l-6 2.5 l-2.5 6 l-2.5 -6 l-6 -2.5 l6 -2.5 z"/>
    </g>

    <!-- BOTTOM: the six-item punch list -->
    <text x="30" y="288" font-size="16" fill="#8b949e" font-weight="bold">SIX-ITEM PUNCH LIST</text>
    <line x1="30" y1="298" x2="1110" y2="298" stroke="#30363d" stroke-width="2" stroke-dasharray="8,6"/>

    <!-- 1: Storyline -->
    <circle cx="120" cy="345" r="28" fill="#161b22" stroke="#bc8cff" stroke-width="2.5"/>
    <circle cx="120" cy="333" r="4.5" fill="#bc8cff"/>
    <path d="M114 340 L126 340 L125 353 L115 353 Z" fill="#bc8cff"/>
    <path d="M107 356 L120 351 L133 356" stroke="#bc8cff" stroke-width="2" fill="none"/>
    <circle cx="98" cy="323" r="12" fill="#161b22" stroke="#bc8cff" stroke-width="2"/>
    <text x="98" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#bc8cff">1</text>
    <text x="120" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Storyline</text>

    <!-- 2: Stock Exchange -->
    <circle cx="300" cy="345" r="28" fill="#161b22" stroke="#3fb950" stroke-width="2.5"/>
    <circle cx="300" cy="333" r="4.5" fill="#3fb950"/>
    <path d="M294 340 L306 340 L305 353 L295 353 Z" fill="#3fb950"/>
    <polyline points="286,357 293,349 300,353 309,341" fill="none" stroke="#3fb950" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="278" cy="323" r="12" fill="#161b22" stroke="#3fb950" stroke-width="2"/>
    <text x="278" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#3fb950">2</text>
    <text x="300" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Stock Exchange</text>

    <!-- 3: Casino / Arcade -->
    <circle cx="480" cy="345" r="28" fill="#161b22" stroke="#d29922" stroke-width="2.5"/>
    <circle cx="480" cy="333" r="4.5" fill="#d29922"/>
    <path d="M474 340 L486 340 L485 353 L475 353 Z" fill="#d29922"/>
    <rect x="472" y="349" width="10" height="10" rx="2" fill="#161b22" stroke="#d29922" stroke-width="1.5"/>
    <circle cx="477" cy="354" r="1.2" fill="#d29922"/>
    <circle cx="483" cy="356" r="1.5" fill="none"/>
    <circle cx="480" cy="323" r="12" fill="#161b22" stroke="#d29922" stroke-width="2"/>
    <text x="480" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#d29922">3</text>
    <text x="480" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Casino / Arcade</text>

    <!-- 4: Crime loop (car theft to police to jail to bribe/puzzle) -->
    <circle cx="660" cy="345" r="28" fill="#161b22" stroke="#f85149" stroke-width="2.5"/>
    <circle cx="660" cy="333" r="4.5" fill="#f85149"/>
    <path d="M654 340 L666 340 L665 353 L655 353 Z" fill="#f85149"/>
    <circle cx="649" cy="350" r="4" fill="none" stroke="#f85149" stroke-width="2"/>
    <circle cx="659" cy="350" r="4" fill="none" stroke="#f85149" stroke-width="2"/>
    <line x1="653" y1="350" x2="655" y2="350" stroke="#f85149" stroke-width="2"/>
    <circle cx="638" cy="323" r="12" fill="#161b22" stroke="#f85149" stroke-width="2"/>
    <text x="638" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#f85149">4</text>
    <text x="660" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Crime Loop</text>

    <!-- 5: Church - done -->
    <circle cx="840" cy="345" r="28" fill="#161b22" stroke="#58a6ff" stroke-width="2.5"/>
    <circle cx="840" cy="333" r="4.5" fill="#58a6ff"/>
    <path d="M828 356 Q840 336 852 356 Z" fill="#58a6ff"/>
    <rect x="837" y="326" width="6" height="8" fill="#58a6ff"/>
    <circle cx="818" cy="323" r="12" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
    <text x="818" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#58a6ff">5</text>
    <g filter="url(#glow)">
      <circle cx="862" cy="325" r="12" fill="#0d3b26" stroke="#3fb950" stroke-width="2"/>
      <path d="M856 325 L860 330 L868 320" stroke="#3fb950" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="840" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Church — Done</text>

    <!-- 6: Lisa romance path -->
    <circle cx="1020" cy="345" r="28" fill="#161b22" stroke="#f78166" stroke-width="2.5"/>
    <circle cx="1012" cy="333" r="4" fill="#f78166"/>
    <path d="M1007 339 L1017 339 L1016 351 L1008 351 Z" fill="#f78166"/>
    <circle cx="1028" cy="333" r="4" fill="#f78166"/>
    <path d="M1023 339 L1033 339 L1032 351 L1024 351 Z" fill="#f78166"/>
    <path d="M1020 358 c-5,-6 -15,-2 -15,6 c0,6 8,10 15,16 c7,-6 15,-10 15,-16 c0,-8 -10,-12 -15,-6 z" fill="#f78166"/>
    <circle cx="998" cy="323" r="12" fill="#161b22" stroke="#f78166" stroke-width="2"/>
    <text x="998" y="327" text-anchor="middle" font-size="14" font-weight="bold" fill="#f78166">6</text>
    <text x="1020" y="392" text-anchor="middle" font-size="14" fill="#c9d1d9">Lisa Romance</text>
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
