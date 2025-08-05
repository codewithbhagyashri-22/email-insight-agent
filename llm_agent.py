from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import re


load_dotenv(override=True)
api_key = os.getenv("GROQ_API_KEY")
base_url = "https://api.groq.com/openai/v1"

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

PROMPT_TEMPLATE = """
You are an assistant that summarizes emails and extracts tasks.

Email:
{email}

Respond in JSON like:
{{
  "summary": "...",
  "tasks": [
    {{"title": "...", "due": "..."}}
  ]
}}
"""

def process_email(email_text):
    prompt = PROMPT_TEMPLATE.format(email=email_text)

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # You can also use mixtral-8x7b or gemma-7b-it
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512
    )
    raw_response = response.choices[0].message.content.strip()

    # Try direct JSON parsing
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        # Try extracting JSON using regex
        json_match = re.search(r"\{[\s\S]+\}", raw_response)
        if json_match:
            try:
                cleaned = json_match.group(0)
                parsed = json.loads(cleaned)
                return parsed
            except json.JSONDecodeError:
                print("❌ JSON found but still not parsable")
                print(cleaned)
        else:
            print("❌ No JSON block found in response")

    print("Raw response:")
    print(raw_response)
    return None