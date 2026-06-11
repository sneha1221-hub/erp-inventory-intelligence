from fastapi import FastAPI
from erp_engine import process_query

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "ERP NLP API Running"
    }


@app.get("/predict")
def predict(query: str):

    return process_query(query)