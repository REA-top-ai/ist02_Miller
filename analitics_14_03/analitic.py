import requests

final_result = []
payload = {"apiKey": "99aabb9cea4749fbbcd1b90919b2d5f4", "q": "phones"}
r = requests.get("https://newsapi.org/v2/everything", params=payload)
data = r.json()
count = 0
for article in data['articles']:
    if (article['title']!= None
            and article['title'].strip() != ""
            and article['url'] != None
            and article['description']!= None
            and len(article['description'])>=50
            and count < 50):
        count += 1
        res = {
            'title':article['title'],
            'source':article['source']['name'],
            'publishedAt':article['publishedAt'],
            'author':article['author'],
        }
        final_result.append(res)

    if count >= 50:
        break
print(final_result)