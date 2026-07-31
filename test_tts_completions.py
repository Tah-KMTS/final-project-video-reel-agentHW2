from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-5.6-luna",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "mp3"},
    messages=[{"role": "user", "content": "Say hello in one short upbeat sentence."}],
)

print(completion)
