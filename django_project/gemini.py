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

hardcoded_sample_response = """
```json
[
  {
    "degree": 1,
    "person_a": "John Lennon",
    "connection": "Met and collaborated with",
    "person_b": "Yoko Ono"
  },
  {
    "degree": 2,
    "person_a": "Yoko Ono",
    "connection": "Was photographed with and attended events with",
    "person_b": "Andy Warhol"
  },
  {
    "degree": 3,
    "person_a": "Andy Warhol",
    "connection": "Met and created art featuring",
    "person_b": "Steve Jobs"
  },
  {
    "degree": 4,
    "person_a": "Steve Jobs",
    "connection": "Regularly met with and collaborated with",
    "person_b": "Larry Page"
  },
  {
    "degree": 5,
    "person_a": "Larry Page",
    "connection": "Has had numerous public and private meetings with, often related to technology and future ventures, as co-founders of major tech companies",
    "person_b": "Elon Musk"
  }
]
```
"""

def send_prompt(person_a : str, person_b : str):
    return hardcoded_sample_response
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

