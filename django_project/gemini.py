# from dotenv import load_dotenv
from google import genai
from google.genai import types

from django.conf import settings

prompt = """
Find the degrees of separation between {0} and {1}. Use famous people they may have met personally. Make sure to collapse long lines of succession such as US presidents, Popes of the Church, and children and parents. Try to keep it under six or seven degrees of separation if possible, but prioritize providing accurate information.
Output in the following JSON format:
[
{{
    "degree": 1,
    "person_a": "",
    "connection": "Explain how they met in a short sentence",
    "person_b": ""
}},
]
"""

def send_prompt(person_a : str, person_b : str):
    client = genai.Client(api_key=settings.GOOGLE_API_KEY)

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=5)  # 0 = disable thinking
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt.format(person_a, person_b),
        config=config
    )

    print(response.text)

if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")
        sys.exit(0)

