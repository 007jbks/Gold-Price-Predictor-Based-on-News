from gemini import gemini
from news import news1

sys = (
    "You will be provided with a list of news article headlines and summaries. "
    "Your task is to analyze these articles and identify which ones are likely to have an impact "
    "on the price of gold. Consider geopolitical events, central bank policies, inflation data, demand-supply shifts, "
    "currency movements, and other relevant financial or economic factors. "
    "Respond strictly in valid JSON format as: {\"articles\": [\"<headline1>\", \"<headline2>\", ...]}"
)

articles = news1()
def f():
    try:
        resp = gemini("".join(articles),sys)
        return resp
    except:
        print("Error")
        return None




