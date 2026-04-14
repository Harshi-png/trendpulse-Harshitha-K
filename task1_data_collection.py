 Task 1: Fetch and categorize trending stories from HackerNews API

import requests

top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"  #top story id's
# Categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "show", "award", "streaming"]
}

# Function to assign category
def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return "others"

try:
    response = requests.get(top_stories_url)

    if response.status_code == 200:
        story_ids = response.json()

        print("Fetching top stories...\n")

        for story_id in story_ids[:20]: # Fetch first 20 stories 

            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_res = requests.get(story_url)

            if story_res.status_code == 200:
                story = story_res.json()
              
                if story and "title" in story:   # Some stories may not have title
                    title = story["title"]
                    category = get_category(title)

                    print("Title:", title)
                    print("Category:", category)
                    print("-" * 50)

    else:
        print("Failed to fetch story IDs")

except Exception as e:
    print("Error occurred:", e)
