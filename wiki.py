import wikipediaapi

# Synchronous client
wiki = wikipediaapi.Wikipedia(user_agent='SixSevenBot/6.7 (https://github.com/birdideas/HackUSF2026; birdideasblog@gmail.com) wikipediaapi/0.12.0', language='en')

page_py = wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())

