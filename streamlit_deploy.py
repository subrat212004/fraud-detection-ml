import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fraud_data_prediction.pkl")

st.title("Real-Time Transaction Fraud Detection System")

st.markdown("""
### About This Project
This system detects fraudulent financial transactions using a Machine Learning model trained on large-scale transaction data.
""")

st.sidebar.title("Model Information")

st.sidebar.markdown("""
Model: XGBoost  
Dataset Size: 6.3 Million  
Threshold: 0.99  
Deployment: Streamlit  
""")

st.subheader("Transaction Details")

step = st.number_input("Step", min_value=0, value=1)

trans_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

amount = st.number_input("Amount", min_value=0.0, value=1000.0)

oldbalanceOrg = st.number_input("Old Balance Origin", 0.0, 60000000.0)

newbalanceOrig = st.number_input("New Balance Origin", 0.0, 50000000.0)

oldbalanceDest = st.number_input("Old Balance Destination", 0.0, 400000000.0)

newbalanceDest = st.number_input("New Balance Destination", 0.0, 400000000.0)

if st.button("Predict Fraud"):

    input_data = pd.DataFrame([{
        "step": step,
        "type": trans_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prob = model.predict_proba(input_data)[:,1][0]

    threshold = 0.99
    prediction = int(prob >= threshold)

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Legitimate Transaction")

    st.metric("Fraud Probability", f"{prob:.4f}")