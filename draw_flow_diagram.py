"""Draws ai_grading/agent_flow.png - a diagram of the reel_agent pipeline."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, FancyBboxPatch

# (label, inputs -> outputs, x, y, width, is_blocked)
NODES = [
    ("load_proposal()\n(slide_planner.py)", "in: project_proposal.md\nout: proposal text", 0, 4),
    ("generate_slide_plan()\n(slide_planner.py)\nAgent: gpt-5.6-luna", "in: proposal text\nout: SlidePlan\n(4-6 slides)", 1, 4),
    ("critique_all()\n(critique.py)\nAgent: gpt-5.6-luna\n(parallel: asyncio.gather)", "in: list[Slide]\nout: CritiqueReport\n(per-slide critique\n+ revised text)", 2, 4),
    ("apply_critique()\n(reel_agent.py)", "in: SlidePlan + CritiqueReport\nout: final list[Slide]", 3, 4),
    ("render_slides()\n(html_renderer.py)", "in: list[Slide]\nout: slides/*.html", 4, 5.2),
    ("synthesize_narration()\n(tts_renderer.py)\n[BLOCKED - no TTS\nmodel access]", "in: narration text\nout: slides/*.mp3", 4, 2.8),
    ("screenshot_all()\n(screenshot.py)", "in: slides/*.html\nout: slides/*.png", 5, 5.2),
    ("build_video()\n(video_builder.py)", "in: slides/*.png\n(+ slides/*.mp3 once\nunblocked)\nout: reel.mp4", 6, 4),
]

EDGES = [
    (0, 1), (1, 2), (2, 3),
    (3, 4), (3, 5),
    (4, 6), (5, 7), (6, 7),
]

fig, ax = plt.subplots(figsize=(16, 8))
ax.set_xlim(-0.5, 6.8)
ax.set_ylim(1.5, 6.5)
ax.axis("off")

box_w, box_h = 0.9, 1.3
centers = {}

for i, (title, io, x, y) in enumerate(NODES):
    blocked = "BLOCKED" in title
    color = "#f8d7da" if blocked else "#d7e3fc"
    edge = "#dc3545" if blocked else "#4361ee"
    box = FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle="round,pad=0.05", linewidth=1.5,
        edgecolor=edge, facecolor=color,
    )
    ax.add_patch(box)
    ax.text(x, y + 0.25, title, ha="center", va="center", fontsize=8, fontweight="bold")
    ax.text(x, y - 0.35, io, ha="center", va="center", fontsize=6.5)
    centers[i] = (x, y)

for a, b in EDGES:
    x1, y1 = centers[a]
    x2, y2 = centers[b]
    ax.annotate(
        "", xy=(x2 - box_w / 2 + 0.05, y2), xytext=(x1 + box_w / 2 - 0.05, y1),
        arrowprops=dict(arrowstyle="->", color="#555555", lw=1.5,
                         connectionstyle="arc3,rad=0.1"),
    )

ax.set_title("reel_agent.py pipeline", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("ai_grading/agent_flow.png", dpi=150)
print("Wrote ai_grading/agent_flow.png")
