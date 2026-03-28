from dotenv import load_dotenv
from google import genai
from google.genai import types

prompt = """
Find the degrees of separation between LeBron and Jesus Christ. Use famous people they may have known. Make sure to collapse long lines of succession such as US presidents, Popes of the Church, and children and parents.
Output in the following JSON format:
[
{
    "degree": 1,
    "person_a": "",
    "connection": "Explain how they met",
    "person_b": ""
},
]
"""

def main():
    load_dotenv()

    # Client auto-reads GEMINI_API_KEY from environment
    client = genai.Client()

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)  # 0 = disable thinking
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config)


    print(response.text)

if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")
        sys.exit(0)

