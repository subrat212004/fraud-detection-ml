from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel

app=FastAPI()
# Load the trained model
model=joblib.load('fraud_data_prediction.pkl')
# Create a Schema
class FraudInput(BaseModel):
    step: float
    type: str
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
# Creating the Home Route
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}
# creating prediction route
@app.post('/predict')
def predict(data:FraudInput):
    input_dic=data.model_dump()
    input_df=pd.DataFrame([input_dic])
    prob=model.predict_proba(input_df)[:,1][0]
    threshold=0.99
    pred=int(prob>=threshold)
    return{
        'prediction':pred,
        'probability':float(prob)
    }