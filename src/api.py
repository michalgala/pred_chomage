import pandas as pd
from fastapi import FastAPI
import uvicorn
from model import create_dataframe

# Create the app
app = FastAPI()

@app.get('/')
def root():
    return {'Bonjour': 'Monde'}

@app.post('/return_df/{start_nb}')
def predict(start_nb: int):
    df = create_dataframe(start_nb)
    return {'prediction_df': df.to_json(orient="records")}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)