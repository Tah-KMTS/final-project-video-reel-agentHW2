from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

models = client.models.list()
for m in sorted(models, key=lambda m: m.id):
    print(m.id)
