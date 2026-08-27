from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI(title="Customer Churn Prediction API")


# Load trained XGBoost model
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "xgboost_churn_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


# These are the EXACT features shown by your XGBoost model
FEATURE_NAMES = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "gender_Male",
    "Partner_Yes",
    "Dependents_Yes",
    "PhoneService_Yes",
    "MultipleLines_No phone service",
    "MultipleLines_Yes",
    "InternetService_Fiber optic",
    "InternetService_No",
    "OnlineSecurity_No internet service",
    "OnlineSecurity_Yes",
    "OnlineBackup_No internet service",
    "OnlineBackup_Yes",
    "DeviceProtection_No internet service",
    "DeviceProtection_Yes",
    "TechSupport_No internet service",
    "TechSupport_Yes",
    "StreamingTV_No internet service",
    "StreamingTV_Yes",
    "StreamingMovies_No internet service",
    "StreamingMovies_Yes",
    "Contract_One year",
    "Contract_Two year",
    "PaperlessBilling_Yes",
    "PaymentMethod_Credit card (automatic)",
    "PaymentMethod_Electronic check",
    "PaymentMethod_Mailed check"
]


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):

    # Convert Pydantic object to dictionary
    customer_data = customer.model_dump()

    # Convert to DataFrame
    input_data = pd.DataFrame([customer_data])

    # One-hot encode categorical variables
    input_data = pd.get_dummies(input_data, drop_first=True)

    # Make sure API dataframe has EXACTLY the same
    # columns and order as the XGBoost training data
    input_data = input_data.reindex(
        columns=FEATURE_NAMES,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Probability of churn
    probability = model.predict_proba(input_data)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }