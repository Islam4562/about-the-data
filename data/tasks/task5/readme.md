 Fraud Detection Report

Project Overview

This project focuses on detecting fraudulent transactions in a synthetic dataset using supervised machine learning. The dataset contains customer transaction data with a binary target variable is_fraud indicating whether the transaction was fraudulent.

Dataset Description

Filename: fraudulent_transactions.csv
Total Records: 1000

Columns:
Column Name	Description
transaction_id	Unique ID of the transaction
customer_id	Customer identifier
amount	Transaction amount (USD)
transaction_time	Timestamp of the transaction
merchant	Merchant where the transaction occurred
device_type	Type of device used
location	Location of transaction
is_fraud	Target variable (1 = Fraud, 0 = Not Fraud)
Data Processing Steps

Datetime Parsing: Extract hour and day_of_week from transaction_time
Categorical Encoding: Label encoding of merchant, device_type, location
Feature Selection:
Numerical: amount, hour, day_of_week
Categorical (encoded): merchant, device_type, location
Train/Test Split: 80% training, 20% testing
Model Used

RandomForestClassifier (100 estimators, default settings)
Model Evaluation

Classification Report:

              precision    recall  f1-score   support

           0       0.91      0.96      0.94       177
           1       0.50      0.30      0.38        23

    accuracy                           0.89       200
   macro avg       0.71      0.63      0.66       200
weighted avg       0.87      0.89      0.88       200

Confusion Matrix:
Predicted 0	Predicted 1
Actual 0	170	7
Actual 1	16	7
