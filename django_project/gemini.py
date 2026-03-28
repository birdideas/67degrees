from google import genai
from google.genai import types
import json

prompt = """
Find the degrees of separation between {0} and {1}. Use famous people they may have met personally. Make sure to collapse long lines of succession such as US presidents, Popes of the Church, and children and parents. Try to keep it under six or seven degrees of separation if possible, but prioritize providing accurate information.

Output ONLY valid JSON in this format:
[
{{
    "degree": 1,
    "person_a": "",
    "connection": "",
    "person_b": ""
}}
]
"""

def send_prompt(person_a: str, person_b: str):
    if not person_a or not person_b:
        return []

    client = genai.Client(api_key="YOUR_KEY")

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=5)
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt.format(person_a, person_b),
        config=config
    )

    text = response.text.strip()

    # 🔥 Handle cases where Gemini wraps JSON in ```json blocks
    if text.startswith("```"):
        text = text.split("```")[1]
        text = text.replace("json", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("❌ Bad JSON from Gemini:\n", text)
        return []