# Real-Time Transaction Fraud Detection System

## Project Overview

This project builds an End-to-End Real-Time Transaction Fraud Detection System using Machine Learning. The system detects fraudulent financial transactions based on transaction details such as transaction type, transaction amount, and account balance behavior.

The model is trained on a large-scale dataset containing over 6.3 million transactions and deployed using FastAPI and Streamlit for real-time predictions.

This project demonstrates the complete machine learning lifecycle, including:

- Data preprocessing  
- Class imbalance handling  
- Model comparison  
- Hyperparameter tuning  
- Threshold optimization  
- Model deployment  

---

## Key Features

- Real-time fraud detection  
- End-to-end machine learning pipeline  
- SMOTE for class imbalance handling  
- Optuna hyperparameter tuning  
- Threshold optimization (0.99)  
- FastAPI backend deployment  
- Interactive Streamlit UI  
- Risk-level interpretation  
- Production-ready architecture  

---

## Dataset Information

- Dataset Size: 6.3 Million Transactions  
- Highly imbalanced dataset  
- Fraud transactions are extremely rare  

Features used:

- Step  
- Transaction Type  
- Amount  
- Old Balance Origin  
- New Balance Origin  
- Old Balance Destination  
- New Balance Destination  

---

## Machine Learning Workflow

### 1. Data Preprocessing

- Handling categorical variables  
- Encoding transaction type  
- Feature scaling using StandardScaler  
- Pipeline creation for reproducibility  

---

### 2. Handling Class Imbalance

Fraud detection datasets are highly imbalanced. To handle this:

- Used SMOTE (Synthetic Minority Oversampling Technique)  
- Balanced dataset before training  

---

### 3. Model Comparison

Multiple models were evaluated:

- Logistic Regression  
- Voting Classifier  
- XGBoost  

After evaluation, XGBoost performed best.

---

### 4. Hyperparameter Tuning

Used Optuna for automated hyperparameter optimization.

Optuna helped find:

- Best learning rate  
- Best max depth  
- Best number of estimators  
- Best regularization parameters  

This significantly improved model performance.

---

### 5. Threshold Optimization

Since fraud detection requires high confidence, a custom threshold of 0.99 was selected.

Benefits:

- Reduced false positives  
- High confidence fraud detection  
- Real-world applicability  

---

## Final Model Performance

After threshold tuning (0.99):

Accuracy = 0.9998  
Precision = 0.9343  
Recall = 0.9136  
F1 Score = 0.9238  

These results demonstrate strong performance on highly imbalanced fraud detection data.

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Optuna  
- Imbalanced-learn (SMOTE)  
- FastAPI  
- Streamlit  
- Joblib  

---

## Project Structure

```
fraud_detection_ml/
│
├── app.py
├── streamlit_app.py
├── fraud_data_prediction.pkl
├── Fraud_detection.ipynb
├── requirements.txt
└── README.md
```

---

## Deployment Architecture

```
User → Streamlit UI → FastAPI → ML Pipeline → XGBoost → Prediction
```

---

## How to Run Locally

### Step 1: Clone Repository

```
git clone https://github.com/yourusername/fraud-detection-ml.git
cd fraud-detection-ml
```

### Step 2: Install Requirements

```
pip install -r requirements.txt
```

### Step 3: Run FastAPI

```
uvicorn app:app --reload
```

### Step 4: Run Streamlit

```
streamlit run streamlit_app.py
```

---

## Application Features

- Manual input support  
- Slider input support  
- Real-time fraud prediction  
- Risk-level interpretation  
- Probability display  
- Error handling  

---

## Use Cases

This system can be used for:

- Banking fraud detection  
- Payment gateway fraud detection  
- Credit card fraud detection  
- Financial transaction monitoring  
- Risk management systems  

---

## Future Improvements

- Deep learning-based fraud detection  
- Batch prediction support  
- Model monitoring  
- Cloud deployment  
- Auto retraining pipeline  

---

## Author

Subrat Shatapathy 
National Institute of Technology Raipur  
Electrical (2026)

---

## Project Status

Completed  
End-to-End Deployment Ready