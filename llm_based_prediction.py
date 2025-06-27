import json
judge = '''
    "You will be given a list of news articles that may influence gold prices. "
    "For each article, respond with either 'positive', 'negative', or 'neutral' based on whether it is expected to drive gold prices up, down, or have no significant effect. "
    "Give total and final overall prediction as whether the price'll go up or down"
    "Give response in json like {"Prediction":"Up"/"Down"} Don't return anything else only the json response"
'''

from gemini import gemini
from filter import f

info = f()

impact = gemini(info,judge)


