# Gold-Price-Predictor-Based-on-News
A simple API that provides gold price prediction based on latest business news

It works by utilising the advanced NLP properties of Gemini 2.0 Flash and https://saurav.tech/NewsAPI/ news api (credit to developer).

## How to use?
1. Simply go to the gemini.py file and add your gemini api key.
2. Download all the required python libraries as listed in requirements.txt
3. Start the backend.py file using fastapi
4. Parse the API response in json and connect with your app

## How it works?
1. The application receives the business news from the news api.
2. Filter.py uses Gemini to filter out the news that are relevant to gold price.
3. llm_based_prediction.py again utilises Gemini to analyse the news and it's sentiment towards the gold price whether it's positive, negative or neutral.
4.  The backend.py file takes the output and then sends it via FastAPI get method.

## Contribution
Pull requests are welcome
