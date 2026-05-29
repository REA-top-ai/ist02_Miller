import os
from dotenv import load_dotenv

load_dotenv()
import requests
import urllib.parse

EUROPEANA_API_KEY = os.getenv("EUROPEANA_API_KEY")


def get_europeana_data(user_prompt):
    url = "https://api.europeana.eu/record/v2/search.json"

    params = {
        "wskey": EUROPEANA_API_KEY,
        "query": user_prompt,   # 🔥 ВАЖНО
        "rows": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    items = []
    for item in data.get("items", []):
        title = item.get("title", ["Artwork"])[0]
        items.append(title)

    return items

def build_prompt(user_prompt, items):
    prompt = f"""
Create an artwork based on cultural references.

User idea: {user_prompt}

Historical references:
"""

    for item in items:
        prompt += f"- {item}\n"

    prompt += """
Combine historical meaning with modern style.
Museum-quality artistic rendering.
"""

    return prompt

def generate_image(prompt):
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}"

    response = requests.get(url, timeout=60)

    if response.status_code == 200:
        return response.content
    return None


def save_image(image, username="user"):
    if image:
        filename = f"images/{username}.png"

        with open(filename, "wb") as f:
            f.write(image)

        print("Saved:", filename)