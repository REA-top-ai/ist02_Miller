import requests
import urllib.parse

EUROPEANA_API_KEY = "my_key"


# 🔹 Получение данных из Europeana
def get_europeana_data(query="painting art", rows=5):
    url = "https://api.europeana.eu/record/v2/search.json"

    params = {
        "wskey": EUROPEANA_API_KEY,
        "query": query,
        "rows": rows
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
        print("Используем fallback")

        return [
            {"title": "Impressionist Landscape with Soft Light"},
            {"title": "Abstract Geometric Composition"},
            {"title": "Classical Renaissance Portrait"}
        ]


# 🔹 Ввод пользователя (всё опционально)
def get_user_input():
    print("\nВведите пожелания (можно пропустить Enter):")

    mood = input("Настроение (dark, calm и т.д.): ").strip()
    colors = input("Цвета: ").strip()
    theme = input("Тема: ").strip()

    print("\n(Опционально) Художественный референс:")
    artist = input("Художник (можно пропустить): ").strip()
    artwork = input("Картина (можно пропустить): ").strip()

    return {
        "mood": mood,
        "colors": colors,
        "theme": theme,
        "artist": artist,
        "artwork": artwork
    }


# 🔹 Построение промпта (ключевая логика)
def build_prompt(items, user_data):
    prompt = "Create an original modern artwork inspired by classical art.\n\n"

    # 1. ОСНОВА
    prompt += "Primary references (MAIN INSPIRATION):\n"
    for item in items:
        prompt += f"- {item['title']}\n"

    # 2. МЯГКИЙ КОНТРОЛЬ
    if user_data["mood"] or user_data["colors"] or user_data["theme"]:
        prompt += "\nSecondary artistic guidance (SOFT CONTROL):\n"

        if user_data["mood"]:
            prompt += f"- mood hint: {user_data['mood']}\n"

        if user_data["colors"]:
            prompt += f"- color palette hint: {user_data['colors']}\n"

        if user_data["theme"]:
            prompt += f"- thematic hint: {user_data['theme']}\n"

    # 3. ОЧЕНЬ СЛАБЫЙ РЕФЕРЕНС
    if user_data["artist"] or user_data["artwork"]:
        prompt += "\nDirectional reference (VERY SUBTLE, DO NOT COPY):\n"

        ref_text = ""
        if user_data["artist"]:
            ref_text += user_data["artist"]

        if user_data["artwork"]:
            ref_text += f" - {user_data['artwork']}"

        prompt += f"- loosely inspired by {ref_text}\n"

    # 4. ПРАВИЛА (анти-копирование)
    prompt += (
        "\nInstructions:\n"
        "- The artwork MUST be original and not resemble any specific existing artwork\n"
        "- Primary influence must come from the provided art references\n"
        "- User guidance should only gently influence mood or color\n"
        "- Any artist or artwork reference must be interpreted loosely and abstractly\n"
        "- DO NOT replicate composition, brushwork, or identifiable elements\n"
        "- Blend all inputs into a unique museum-quality piece\n\n"

        "Important:\n"
        "- This is NOT a UI or app design\n"
        "- Do NOT include modern devices or screens\n\n"

        "Style:\n"
        "modern interpretation of classical art, high detail, soft lighting, gallery painting"
    )

    return prompt


# 🔹 Генерация изображения
def generate_image(prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024"

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


# 🔹 Сохранение
def save_image(image_bytes, filename="design.png"):
    if image_bytes:
        with open(filename, "wb") as f:
            f.write(image_bytes)
        print(f"Сохранено как {filename}")
    else:
        print("Нет изображения")


# 🔹 MAIN
if __name__ == "__main__":
    print("Запуск\n")

    # 1. Получаем данные
    items = get_europeana_data()

    # 2. Ввод пользователя
    user_data = get_user_input()

    # 3. Строим промпт
    print("\nСоздаём промпт")
    prompt = build_prompt(items, user_data)

    print("\nPROMPT:\n", prompt)

    # 4. Генерация
    print("\nГенерация")
    image = generate_image(prompt)

    # 5. Сохранение
    print("\nСохранение")
    save_image(image)

    print("\nГотово")
