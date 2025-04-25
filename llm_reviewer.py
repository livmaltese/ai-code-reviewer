import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(code: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior engineer reviewing pull requests."},
            {"role": "user", "content": f"Review this code:\n\n{code}"}
        ]
    )
    return response.choices[0].message["content"]
