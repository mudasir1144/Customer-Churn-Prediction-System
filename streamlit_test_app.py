import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('models/log_model.pkl', 'rb') as file:
    log_model = pickle.load(file)

def predict_customer_churn(
    age,
    monthly_spending,
    tenure,
    purchases,
    support_requests,
    satisfaction_score
):

    customer_data = pd.DataFrame({
        'Age':[age],
        'Monthly Spending':[monthly_spending],
        'Tenure':[tenure],
        'Number of Purchases':[purchases],
        'Customer Support Requests':[support_requests],
        'Satisfaction Score':[satisfaction_score]
    })

    prediction = log_model.predict(customer_data)[0]

    probability = log_model.predict_proba(customer_data)[0][1]

    if prediction == 1:
        result = "Likely To Churn"
    else:
        result = "Not Likely To Churn"

    return result, probability


st.title("Customer Churn Prediction System")

st.subheader("Enter Customer Information")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

monthly_spending = st.number_input(
    "Monthly Spending",
    min_value=0.0,
    value=5000.0
)

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

purchases = st.number_input(
    "Number of Purchases",
    min_value=0,
    value=10
)

support_requests = st.number_input(
    "Customer Support Requests",
    min_value=0,
    value=2
)

satisfaction_score = st.number_input(
    "Satisfaction Score",
    min_value=1,
    max_value=10,
    value=7
)

predict_button = st.button("Predict Churn")
if predict_button:

    result, probability = predict_customer_churn(
        age,
        monthly_spending,
        tenure,
        purchases,
        support_requests,
        satisfaction_score
    )

    st.subheader("Prediction Result")

    st.success(result)

    st.write(
        f"Churn Probability: {probability*100:.2f}%"
    )

st.subheader("Important Contributing feature")

factors = []

if satisfaction_score <=4:
    factors.append("Low Customer Satisfaction")
if support_requests >=5:
    factors.append('High Customer Support Request')
if purchases <=3:
    factors.append("Low number of purchases")
if age <25:
    factors.append("Young customer segment")
if len(factors)==0:
    st.write('No major churn risk factor detected')
else:
    for factor in factors:
        st.write(f"{factor}")