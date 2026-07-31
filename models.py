"""Pydantic schemas for the slide plan (ai_grading/slide_plan.json)."""

from pydantic import BaseModel, Field


class Slide(BaseModel):
    description: str
    narration: str


class SlidePlan(BaseModel):
    slides: list[Slide] = Field(min_length=4, max_length=6)


class SlideCritique(BaseModel):
    slide_index: int
    critique: str
    suggestions: str
    revised_description: str
    revised_narration: str


class CritiqueReport(BaseModel):
    critiques: list[SlideCritique]
