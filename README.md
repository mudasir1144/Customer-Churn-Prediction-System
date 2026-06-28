# 🚀 Customer Churn Prediction System

> A Machine Learning web application that predicts whether a customer is likely to churn using **Logistic Regression** and provides the probability of churn along with key contributing risk factors.

---

# 📌 Project Overview

Customer churn is one of the biggest challenges faced by businesses. Losing existing customers is often more expensive than acquiring new ones. This project aims to predict customer churn using Machine Learning so that businesses can identify high-risk customers and take proactive retention measures.

The project uses **Logistic Regression** for binary classification and is deployed through a **Streamlit** web application that allows users to make real-time predictions.

---

# 🎯 Objectives

* Predict customer churn using Machine Learning.
* Analyze customer behavior based on demographic and transactional features.
* Provide churn probability instead of only Yes/No predictions.
* Display major factors contributing to churn.
* Build an interactive Streamlit web application for easy use.

---

# 🛠️ Technologies Used

| Category             | Technology                     |
| -------------------- | ------------------------------ |
| Programming Language | Python 3.x                     |
| Machine Learning     | Scikit-learn                   |
| Data Processing      | Pandas, NumPy                  |
| Model Serialization  | Pickle                         |
| Web Application      | Streamlit                      |
| Visualization        | Matplotlib, Seaborn (optional) |
| IDE                  | VS Code / Jupyter Notebook     |

---

# 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── customer_dataset.csv
│   │
├── models/
│   └── log_model.pkl
|   └── feature_name.pkl
|   └── ann_model.pkl
|   └── xg_boost.pkl
│
├── index.ipynb
│  │
├── streamlit_test_app.py
│
├── analysis report.docx
│
├── README.md
│
└── Heatmap.png
```

---

# 📊 Dataset Description

The dataset contains customer demographic and behavioral information.

### Features

* Age
* Monthly Spending
* Tenure
* Number of Purchases
* Customer Support Requests
* Satisfaction Score

### Target Variable

| Value | Meaning                 |
| ----- | ----------------------- |
| 0     | Customer Will Not Churn |
| 1     | Customer Will Churn     |

---

# ⚙️ Machine Learning Workflow

```text
Customer Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Train-Test Split
        │
        ▼
Feature Scaling
        │
        ▼
Logistic Regression
        │
        ▼
Model Evaluation
        │
        ▼
Save Model (.pkl)
        │
        ▼
Streamlit Deployment
```

---

# 📈 Features of the Application

✅ Predict customer churn in real time

✅ Display churn probability

✅ User-friendly interface

✅ Detect important churn risk factors

✅ Fast prediction using a trained ML model

---

# 🖥️ Streamlit Interface

The application allows users to enter:

* Age
* Monthly Spending
* Tenure
* Number of Purchases
* Customer Support Requests
* Satisfaction Score

After clicking **Predict Churn**, the application displays:

* Prediction Result
* Churn Probability (%)
* Important Contributing Factors

---

# 🔍 Churn Risk Factors

The application identifies major risk indicators, including:

* Low Customer Satisfaction
* High Customer Support Requests
* Low Purchase Frequency
* Young Customer Segment

These insights help businesses understand *why* a customer may be at risk of leaving.

---

# 📈 Model Used

**Algorithm:** Logistic Regression

### Why Logistic Regression?

* Suitable for binary classification
* Fast training and prediction
* Easy to interpret
* Produces probability estimates
* Works well with structured numerical datasets

---

# 📊 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC Curve

*(Replace this section with your actual evaluation metrics if available.)*

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

Navigate to the project directory:

```bash
cd customer-churn-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run streamlit_test_app.py
```

The application will open automatically in your default web browser.

---

# 📦 Required Libraries

```text
streamlit
pandas
numpy
scikit-learn
pickle
matplotlib
seaborn
```


# 💼 Business Benefits

This project enables organizations to:

* Reduce customer churn
* Improve customer satisfaction
* Increase customer retention
* Support data-driven decision-making
* Identify high-risk customers before they leave

---

# 🔮 Future Improvements

Possible enhancements include:

* Random Forest implementation
* XGBoost model
* Deep Learning approach
* Feature importance visualization
* SHAP explainability
* Database integration
* Cloud deployment
* User authentication
* Dashboard analytics
* Batch prediction support

---


# 🤝 Contributing

Contributions are welcome!

If you have ideas for improvements, feel free to:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

# 📄 License

This project is developed for educational and academic purposes.

You may modify and use it for learning, research, and portfolio projects.

---

# 👨‍💻 Author

**Mudasir Raza**

Machine Learning Student | Python Developer | Data Science Enthusiast

---

# ⭐ Acknowledgements

Special thanks to:

* Scikit-learn
* Streamlit
* Pandas
* NumPy
* Open-source Machine Learning Community

---

> **If you found this project helpful, consider giving it a ⭐ on GitHub!**
