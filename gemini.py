import requests
import json

API_KEY = "YOUR GEMINI API KEY"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def gemini(query, system_prompt, API_KEY=API_KEY, URL=URL):
    data = {
        "contents": [{
            "parts": [{"text": system_prompt + query}]
        }]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        try:
            result = response.json()
            response_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return response_text
        except (KeyError, IndexError) as e:
            print("❌ Error parsing response:", e)
            print("📦 Full response:", json.dumps(result, indent=2))
            return "Error"
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return "response not okay"


