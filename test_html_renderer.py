import json

from html_renderer import render_slides
from models import Slide

with open("ai_grading/slide_plan.json", encoding="utf-8") as f:
    data = json.load(f)

slides = [Slide(**s) for s in data["slides"]]
paths = render_slides(slides)
print("Wrote:", paths)