from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

models = list(client.models.list())
models.sort(key=lambda m: m.name)

print(f"{'NAME':<45} {'DISPLAY NAME':<30} {'IN TOKENS':>12} {'OUT TOKENS':>11}")
print("-" * 102)

for m in models:
    print(
        f"{m.name:<45} "
        f"{(m.display_name or ''):<30} "
        f"{(m.input_token_limit or 0):>12,} "
        f"{(m.output_token_limit or 0):>11,}"
    )

print(f"\n{len(models)} models total.")

# Show which models support generateContent (i.e. can be used for chat/generation)
print("\nModels supporting generateContent:")
for m in models:
    if m.supported_actions and "generateContent" in m.supported_actions:
        print(f"  {m.name}")

client.close()

