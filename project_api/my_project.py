import requests
import urllib.parse


EUROPEANA_API_KEY = "my_key"

#Получение данных
def get_europeana_data():
    url = "https://api.europeana.eu/record/v2/search.json"

    params = {
        "wskey": EUROPEANA_API_KEY,
        "query": "painting art",
        "rows": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        items = []
        for item in data.get("items", []):
            title = item.get("title", ["Artwork"])[0]

            items.append({
                "title": title
            })

        print("Данные получены из Europeana")
        return items

    except Exception as e:
        print("Ошибка Europeana:", e)
        print("Используем fallback...")

        return [
            {"title": "Impressionist Landscape with Soft Light"},
            {"title": "Abstract Geometric Composition"},
            {"title": "Classical Renaissance Portrait"}
        ]

#ПРОМПТ
def build_prompt(items):
    prompt = "Create a modern visual artwork inspired by classical art.\n\n"

    prompt += "Art references:\n"
    for item in items:
        prompt += f"- {item['title']}\n"

    prompt += (
        "\nInterpret these artworks into a NEW original piece.\n"
        "Use their:\n"
        "- color palette\n"
        "- composition\n"
        "- mood and lighting\n"
        "- artistic style\n\n"

        "Important:\n"
        "- This is NOT a UI design\n"
        "- DO NOT draw phones, apps, or interfaces\n"
        "- Create it as a painting, canvas, or wall artwork\n"
        "- It should look like something hanging in a gallery\n\n"

        "Style:\n"
        "modern interpretation of classical art, high detail, "
        "soft lighting, artistic композиция, museum quality"
    )

    return prompt

#Генерация
def generate_image(prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:
        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            print("Изображение сгенерировано")
            return response.content
        else:
            print("Ошибка API:", response.status_code)
            return None

    except Exception as e:
        print("Ошибка:", e)
        return None

#Сохранение
def save_image(image_bytes):
    if image_bytes:
        with open("design.png", "wb") as f:
            f.write(image_bytes)
        print("Сохранено как design.png")
    else:
        print("Нет изображения")

#MAIN
if __name__ == "__main__":
    print("Запуск...\n")

    items = get_europeana_data()

    print("\nСоздаём промпт...")
    prompt = build_prompt(items)
    print("\nPROMPT:\n", prompt)

    print("\nГенерация...")
    image = generate_image(prompt)

    print("\nСохранение...")
    save_image(image)

    print("\nГотово!")