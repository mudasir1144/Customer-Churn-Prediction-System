import numpy as np
import pandas as pd
import pickle

with open ('models/log_model.pkl','rb')as file:
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

    if prediction ==1:
        results = 'Customer is likely to churn'
    else:
        results= 'Customer is not likely to churn'
    
    return results , probability

result, probability = predict_customer_churn(
    age=35,
    monthly_spending=1.2,
    tenure=12,
    purchases=15,
    support_requests=6,
    satisfaction_score=3
)

print(result)
print(f"Churn Probability: {probability*100:.2f}%")