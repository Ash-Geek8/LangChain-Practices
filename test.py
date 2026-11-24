from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"


client = OpenAI()

result = client.images.generate(
    model="gpt-image-1",
    prompt="A detailed technical diagram of a quantum computer"
)