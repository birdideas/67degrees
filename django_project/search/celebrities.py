CELEBRITIES = [
    # Music
    {"name": "Taylor Swift", "category": "Music", "emoji": "🎵"},
    {"name": "Beyoncé", "category": "Music", "emoji": "🎵"},
    {"name": "Drake", "category": "Music", "emoji": "🎵"},
    {"name": "Rihanna", "category": "Music", "emoji": "🎵"},
    {"name": "Ed Sheeran", "category": "Music", "emoji": "🎵"},
    {"name": "Billie Eilish", "category": "Music", "emoji": "🎵"},
    {"name": "The Weeknd", "category": "Music", "emoji": "🎵"},
    {"name": "Adele", "category": "Music", "emoji": "🎵"},
    {"name": "Bruno Mars", "category": "Music", "emoji": "🎵"},
    {"name": "Lady Gaga", "category": "Music", "emoji": "🎵"},
    {"name": "Kendrick Lamar", "category": "Music", "emoji": "🎵"},
    {"name": "Ariana Grande", "category": "Music", "emoji": "🎵"},
    {"name": "Post Malone", "category": "Music", "emoji": "🎵"},
    {"name": "Dua Lipa", "category": "Music", "emoji": "🎵"},
    {"name": "Harry Styles", "category": "Music", "emoji": "🎵"},
    {"name": "Olivia Rodrigo", "category": "Music", "emoji": "🎵"},
    {"name": "Sabrina Carpenter", "category": "Music", "emoji": "🎵"},
    {"name": "Eminem", "category": "Music", "emoji": "🎵"},
    {"name": "Jay-Z", "category": "Music", "emoji": "🎵"},
    {"name": "Kanye West", "category": "Music", "emoji": "🎵"},
    # Film & TV
    {"name": "Leonardo DiCaprio", "category": "Film", "emoji": "🎬"},
    {"name": "Scarlett Johansson", "category": "Film", "emoji": "🎬"},
    {"name": "Tom Hanks", "category": "Film", "emoji": "🎬"},
    {"name": "Meryl Streep", "category": "Film", "emoji": "🎬"},
    {"name": "Brad Pitt", "category": "Film", "emoji": "🎬"},
    {"name": "Angelina Jolie", "category": "Film", "emoji": "🎬"},
    {"name": "Dwayne Johnson", "category": "Film", "emoji": "🎬"},
    {"name": "Jennifer Lawrence", "category": "Film", "emoji": "🎬"},
    {"name": "Ryan Reynolds", "category": "Film", "emoji": "🎬"},
    {"name": "Chris Evans", "category": "Film", "emoji": "🎬"},
    {"name": "Zendaya", "category": "Film", "emoji": "🎬"},
    {"name": "Tom Holland", "category": "Film", "emoji": "🎬"},
    {"name": "Timothée Chalamet", "category": "Film", "emoji": "🎬"},
    {"name": "Florence Pugh", "category": "Film", "emoji": "🎬"},
    {"name": "Margot Robbie", "category": "Film", "emoji": "🎬"},
    {"name": "Pedro Pascal", "category": "Film", "emoji": "🎬"},
    {"name": "Sydney Sweeney", "category": "Film", "emoji": "🎬"},
    {"name": "Ana de Armas", "category": "Film", "emoji": "🎬"},
    {"name": "Keanu Reeves", "category": "Film", "emoji": "🎬"},
    {"name": "Denzel Washington", "category": "Film", "emoji": "🎬"},
    # Sports
    {"name": "Cristiano Ronaldo", "category": "Sports", "emoji": "⚽"},
    {"name": "Lionel Messi", "category": "Sports", "emoji": "⚽"},
    {"name": "LeBron James", "category": "Sports", "emoji": "🏀"},
    {"name": "Serena Williams", "category": "Sports", "emoji": "🎾"},
    {"name": "Roger Federer", "category": "Sports", "emoji": "🎾"},
    {"name": "Naomi Osaka", "category": "Sports", "emoji": "🎾"},
    {"name": "Simone Biles", "category": "Sports", "emoji": "🤸"},
    {"name": "Michael Jordan", "category": "Sports", "emoji": "🏀"},
    {"name": "Tiger Woods", "category": "Sports", "emoji": "⛳"},
    {"name": "Usain Bolt", "category": "Sports", "emoji": "🏃"},
    {"name": "Stephen Curry", "category": "Sports", "emoji": "🏀"},
    {"name": "Patrick Mahomes", "category": "Sports", "emoji": "🏈"},
    {"name": "Caitlin Clark", "category": "Sports", "emoji": "🏀"},
    # Tech & Business
    {"name": "Elon Musk", "category": "Tech", "emoji": "🚀"},
    {"name": "Jeff Bezos", "category": "Tech", "emoji": "💼"},
    {"name": "Bill Gates", "category": "Tech", "emoji": "💻"},
    {"name": "Mark Zuckerberg", "category": "Tech", "emoji": "💻"},
    {"name": "Oprah Winfrey", "category": "TV", "emoji": "📺"},
    {"name": "Kim Kardashian", "category": "TV", "emoji": "📺"},
    {"name": "Ellen DeGeneres", "category": "TV", "emoji": "📺"},
    # Other
    {"name": "Prince Harry", "category": "Royals", "emoji": "👑"},
    {"name": "Meghan Markle", "category": "Royals", "emoji": "👑"},
    {"name": "David Beckham", "category": "Sports", "emoji": "⚽"},
    {"name": "Victoria Beckham", "category": "Fashion", "emoji": "👗"},
    {"name": "Kylie Jenner", "category": "TV", "emoji": "📺"},
    {"name": "Kendall Jenner", "category": "Fashion", "emoji": "👗"},
]

def search_celebrities(query, limit=8):
    if not query or len(query) < 1:
        return []
    query_lower = query.lower()
    results = []

    # Prioritize names starting with query
    for celeb in CELEBRITIES:
        name_lower = celeb["name"].lower()
        if name_lower.startswith(query_lower):
            results.append({**celeb, "score": 2})

    # Then names containing query
    for celeb in CELEBRITIES:
        name_lower = celeb["name"].lower()
        if not name_lower.startswith(query_lower) and query_lower in name_lower:
            results.append({**celeb, "score": 1})

    # Sort by score then alpha
    results.sort(key=lambda x: (-x["score"], x["name"]))
    return results[:limit]

