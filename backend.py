from fastapi import FastAPI
from llm_based_prediction import impact


app = FastAPI()

@app.get("/gold")
def predict():
    return {"Prediction":impact}
