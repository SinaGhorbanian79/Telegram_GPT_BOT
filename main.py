from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv("api_key.env")

# Access environment variable using os.getenv
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "please write a poem about racism",
        }
    ],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
