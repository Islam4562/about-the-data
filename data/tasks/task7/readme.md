# Telecom Customer Churn Prediction Report

## Project Overview

The goal of this project is to predict customer churn using a dataset from a telecom company. Churn refers to customers who stop using the service. By identifying patterns in customer behavior, we can build a predictive model to support business decisions aimed at customer retention.

---

## Problem Statement

**Objective:**  
Develop a machine learning model that accurately predicts whether a customer will churn based on historical features such as tenure, billing information, internet service, and demographics.

---

## Dataset Description

- **Source:** Synthetic telecom customer dataset (1,000 samples)
- **Format:** CSV (`telecom_customers.csv`)
- **Target Variable:** `churn` (Yes = 1, No = 0)
- **Main Features:**
  - `tenure`: Number of months the customer has stayed
  - `monthly_charges`: Monthly billing amount
  - `internet_service`, `phone_service`, `multiple_lines`
  - `partner`, `dependents`, `senior_citizen`
  - `total_charges` (derived)

---

## Tools and Libraries

- Python 3.10
- `pandas`, `numpy` for data manipulation
- `scikit-learn` for ML modeling
- `matplotlib`, `seaborn` for visualization

---

## Data Preprocessing

- Removed missing values (if any)
- Encoded categorical features using `LabelEncoder`
- Split dataset into training (80%) and test (20%) sets
- Removed `customer_id` as it is not predictive

---

## Model Training

- Algorithm used: **Random Forest Classifier**
- Parameters: `n_estimators=100`, `random_state=42`
- Train/test split: 80/20

---

## Model Evaluation

- **Accuracy:** ~80%
- **Classification Report:**
  - Precision, Recall, F1-Score reported for both classes
- **Confusion Matrix:** Provided to visualize true/false positives and negatives

---

## Feature Importance

Top contributing features:
1. `tenure`
2. `monthly_charges`
3. `total_charges`
4. `internet_service`

Visualized using bar plot of feature importances from the Random Forest model.

---

## Key Insights

- Customers with low tenure and high monthly charges are more likely to churn.
- Fiber optic internet service showed a higher churn rate than DSL or No Internet.
- Partnered customers tend to churn less often.

---

## ✅ Conclusion

The model performs with good baseline accuracy and can be further improved using advanced techniques like hyperparameter tuning, ensemble models (e.g., XGBoost), or including temporal behavior (e.g., recent activity trends).

---

## Next Steps

- Implement a dashboard for churn monitoring.
- Deploy the model as a REST API for real-time scoring.
- Integrate with CRM to trigger retention actions.

---

## 👨‍💻 Author

*Islam Nashentaev*  
*AI/Data Engineer — April 2025*
