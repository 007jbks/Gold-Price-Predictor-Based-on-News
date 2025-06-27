

import requests


BASE_URL = "https://saurav.tech/NewsAPI/"
category = "business"
country_code = "in"

top_headlines_api = f"{BASE_URL}/top-headlines/category/{category}/{country_code}.json"

def news1():
    try:
        response = requests.get(top_headlines_api)
        response.raise_for_status()  
        data = response.json()
        titles = []
        for article in data.get("articles", [])[:20:1]:
            titles.append(article["title"])
        return titles
    except requests.exceptions.RequestException as e:
        return f"❌ Error fetching news:{e}"
