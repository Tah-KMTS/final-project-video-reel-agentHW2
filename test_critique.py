
import json

from critique import critique_slide
from models import Slide

with open("ai_grading/slide_plan.json", encoding="utf-8") as f:
    data = json.load(f)

slide1 = Slide(**data["slides"][0])
result = critique_slide(slide1, index=1)
print(result.model_dump_json(indent=2))