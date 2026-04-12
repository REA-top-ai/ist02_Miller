import requests


MISTRAL_API_KEY = "ZuJF2w6Hyepz7QtCqoQAPXof9qeZA26J"
NEWSAPI_KEY = "99aabb9cea4749fbbcd1b90919b2d5f4"


def get_news(topic):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 15,
        "apiKey": NEWSAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("articles", [])


def build_prompt(articles, topic):
    text = ""

    for i, a in enumerate(articles, 1):
        title = a.get("title", "")
        desc = a.get("description", "")
        source = a.get("source", {}).get("name", "")

        text += f"{i}. {title}\n{desc}\nИсточник: {source}\n\n"

    return f"""
Ты — профессиональный новостной аналитик.

Проанализируй статьи по теме: "{topic}".

Требования:
- объясни, что произошло за последние 24 часа
- выдели ключевые события
- дай анализ причин и последствий
- определи тенденции

ВАЖНО:
- язык: русский
- объем: 250–300 слов
- стиль: как Reuters / Bloomberg

СТАТЬИ:
{text}
"""


def ask_mistral(prompt):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]


def save_to_file(text):
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(text)


def main():
    topic = input("Введите тему новостей: ")

    print("Загружаю новости...")
    articles = get_news(topic)

    if not articles:
        print("Новости не найдены")
        return

    print("Создаю аналитический запрос...")
    prompt = build_prompt(articles, topic)

    print("Отправляю в Mistral...")
    result = ask_mistral(prompt)

    save_to_file(result)

    print("Готово! Результат в файле text.txt")


if __name__ == "__main__":
    main()