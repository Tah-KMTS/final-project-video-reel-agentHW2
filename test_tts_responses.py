import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Say hello in one short upbeat sentence.",
    extra_body={
        "modalities": ["text", "audio"],
        "audio": {"voice": "alloy", "format": "mp3"},
    },
)

print(response)
