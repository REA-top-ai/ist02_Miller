import os
from datetime import datetime
import requests
import urllib.parse

from auth import verify_token

def generate_image(token, prompt):

    username = verify_token(token)

    if not username:
        print("Unauthorized")
        return None

    print(f"User '{username}' authorized")

    encoded_prompt = urllib.parse.quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:
        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            print("Image generated")
            return response.content

        else:
            print("API Error")
            return None

    except Exception as e:
        print("Error:", e)
        return None


def save_image(image_bytes, username):

    if not os.path.exists("images"):
        os.makedirs("images")

    filename = f"{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    filepath = os.path.join("images", filename)

    with open(filepath, "wb") as f:
        f.write(image_bytes)

    print("Image saved:", filepath)

    return filepath