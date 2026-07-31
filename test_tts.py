import json

from tts_renderer import synthesize_narration
from models import Slide

with open("ai_grading/slide_plan.json", encoding="utf-8") as f:
    data = json.load(f)

slide1 = Slide(**data["slides"][0])
synthesize_narration(slide1.narration, "slides/slide_1.mp3")
print("Wrote slides/slide_1.mp3")