# -*- coding: utf-8 -*-
"""
Created on Jan 2, 2024

@author: Abhishek
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#Obs 1: Logistic Regression has a huge number of false positives (Lesser precision and Accuracy)
#Obs 2: Local Outlier Factor has higher percentage of false negatives
#Obs 3: Undersampling and Oversampling do not help
#Conclusion 1: We continue working with Isolation forest
    
    
def model_train(data):   
    columns = data.columns.tolist()
    features = [x for x in columns if x not in ["Class", "Amount"]]
    output = "Class"
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[output], test_size=0.3, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Isolation Forest
    model_if = IsolationForest(contamination=0.055, random_state=43)  # Adjust contamination based on your dataset
    model_if.fit(X_train, y_train)
    y_pred_if = model_if.predict(X_test)

    y_pred_if_binary = np.where(y_pred_if == -1, 1, 0)
    
    print("Isolation Forest Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred_if_binary))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_if_binary))
    
    print("Precision:", precision_score(y_test, y_pred_if_binary))
    print("Recall:", recall_score(y_test, y_pred_if_binary))
    print("F1 Score:", f1_score(y_test, y_pred_if_binary))
    print("Accuracy:", accuracy_score(y_test, y_pred_if_binary))
