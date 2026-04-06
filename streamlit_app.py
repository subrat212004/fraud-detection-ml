import streamlit as st  
import requests

# Title
st.title("Real-Time Transaction Fraud Detection System")

# Project Description
st.markdown("""
### About This Project
This system detects fraudulent financial transactions using a Machine Learning model trained on large-scale transaction data.  
The model uses XGBoost with preprocessing pipeline including encoding, scaling, and imbalance handling.  
This application provides real-time fraud detection using FastAPI and Streamlit.
""")

# Sidebar Information
st.sidebar.title("Model Information")

st.sidebar.markdown("""
**Model:** XGBoost Classifier  
**Dataset Size:** 6.3 Million Transactions  
**Imbalance Handling:** SMOTE  
**Threshold:** 0.99  
**Deployment:** FastAPI + Streamlit  
**Prediction Type:** Real-Time  
""")

st.subheader("Transaction Details")

# Step 
step_input = st.radio(
    'Step Input Type',
    ['Manual','Slider'],
    horizontal=True,
    key="step_input"
)

if step_input == 'Manual':
    step = st.number_input('Step', min_value=0, value=1)
else:
    step = st.slider('Step', min_value=0, max_value=800, value=1, step=1)


# Transaction Type
trans_type = st.selectbox(
    'Transaction Type',
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)


st.subheader("Transaction Amount")

# Amount
amt_input = st.radio(
    'Amount Input Type',
    ['Manual','Slider'],
    horizontal=True,
    key="amount_input"
)

if amt_input == 'Manual':
    amount = st.number_input('Amount', min_value=0.0, value=1000.0)
else:
    amount = st.slider('Amount', 0.0, 100000000.0, value=1000.0, step=1000.0)


st.subheader("Origin Account Balance")

# Old Balance Origin
old_org_input = st.radio(
    "Old Balance Origin Input",
    ["Manual", "Slider"],
    horizontal=True,
    key="old_org"
)

if old_org_input == "Manual":
    oldbalanceOrg = st.number_input("Old Balance Origin", 0.0, 60000000.0, value=0.0)
else:
    oldbalanceOrg = st.slider("Old Balance Origin", 0.0, 60000000.0, value=0.0, step=1000.0)


# New Balance Origin
new_org_input = st.radio(
    "New Balance Origin Input",
    ["Manual", "Slider"],
    horizontal=True,
    key="new_org"
)

if new_org_input == "Manual":
    newbalanceOrig = st.number_input("New Balance Origin", 0.0, 50000000.0, value=0.0)
else:
    newbalanceOrig = st.slider("New Balance Origin", 0.0, 50000000.0, value=0.0, step=1000.0)


st.subheader("Destination Account Balance")

# Old Balance Destination
old_dest_input = st.radio(
    "Old Balance Dest Input",
    ["Manual", "Slider"],
    horizontal=True,
    key="old_dest"
)

if old_dest_input == "Manual":
    oldbalanceDest = st.number_input("Old Balance Destination", 0.0, 400000000.0, value=0.0)
else:
    oldbalanceDest = st.slider("Old Balance Destination", 0.0, 400000000.0, value=0.0, step=1000.0)


# New Balance Destination
new_dest_input = st.radio(
    "New Balance Dest Input",
    ["Manual", "Slider"],
    horizontal=True,
    key="new_dest"
)

if new_dest_input == "Manual":
    newbalanceDest = st.number_input("New Balance Destination", 0.0, 400000000.0, value=0.0)
else:
    newbalanceDest = st.slider("New Balance Destination", 0.0, 400000000.0, value=0.0, step=1000.0)


st.markdown("---")


# Predict Button
if st.button("Predict Fraud"):
    
    with st.spinner("Processing Transaction..."):
        
        url = "http://127.0.0.1:8000/predict"
        
        input_data = {
            "step": step,
            "type": trans_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }
        
        try:
            response = requests.post(url, json=input_data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                
                prediction = result["prediction"]
                probability = result["probability"]
                
                st.subheader("Prediction Result")
                
                if prediction == 1:
                    st.error("⚠️ Fraudulent Transaction Detected")
                else:
                    st.success("✅ Legitimate Transaction")
                
                st.metric("Fraud Probability", f"{probability:.4f}")
                
                # Risk Interpretation
                if probability > 0.9:
                    st.warning("High Risk Transaction")
                elif probability > 0.5:
                    st.info("Moderate Risk Transaction")
                else:
                    st.success("Low Risk Transaction")
                    
            else:
                st.error("API returned an unexpected response")
        
        except requests.exceptions.ConnectionError:
            st.error("FastAPI server not running. Start API first.")
        
        except requests.exceptions.Timeout:
            st.error("Request timed out. Try again.")
        
        except Exception as e:
            st.error(f"Unexpected error: {e}")