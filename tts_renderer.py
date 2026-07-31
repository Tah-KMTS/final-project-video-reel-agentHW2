"""Synthesizes narration audio for each slide using OpenAI TTS."""

import os

from dotenv import load_dotenv
from openai import OpenAI

from models import Slide

load_dotenv()

client = OpenAI()

TTS_MODEL = "tts-1"
TTS_VOICE = "alloy"


def synthesize_narration(text: str, out_path: str) -> None:
    with client.audio.speech.with_streaming_response.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text,
    ) as response:
        response.stream_to_file(out_path)


def render_audio(slides: list[Slide], out_dir: str = "slides") -> list[str]:
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, slide in enumerate(slides, start=1):
        path = os.path.join(out_dir, f"slide_{i}.mp3")
        synthesize_narration(slide.narration, path)
        paths.append(path)
    return paths
