# -*- coding: utf-8 -*-
"""
Description: To handle missing values, outliers, format data, categorical values, data imabalance (If req.) & scaling.

@author: Abhishek
"""
import pandas as pd
import os
from imblearn.over_sampling import SMOTE


def data_process(file_path):
    data = pd.read_csv(file_path)
    
    print(data.head())
    
    #Check for missing values
    data = treat_missing_values(data)
        
    #Treat outliers
    data = treat_outliers(data)
    
    #Format data
    data = format_data(data)
    
    #Categorical data
    data = treat_categorical_data(data)
    
    output_path = get_output_file_path("processeddata.csv")
    
    if os.path.exists(output_path):
        os.remove(output_path)
        data.to_csv(output_path, index = False)
    else:
        data.to_csv(get_output_file_path("processeddata.csv"), index = False)
    return data

def format_data(data):
    return data

def treat_categorical_data(data):
    return data

def treat_outliers(data):
    return data

def treat_missing_values(data):
    if data.isnull().sum().sum() != 0:
        pass
    else:
        return data
    
def get_file_path():
    script_path = os.path.abspath(__file__)
    relative_path = "../../data/raw/creditcardtxs.csv"
    file_path = os.path.join(os.path.dirname(script_path), relative_path)
    return file_path

def get_output_file_path(file_name):
    script_path = os.path.abspath(__file__)
    relative_path = "../../data/processed/" + file_name
    file_path = os.path.join(os.path.dirname(script_path), relative_path)
    return file_path

def imbalanced_data(X_train, y_train):
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    return X_train_resampled, y_train_resampled

def data_scaling(data, scaler, transform_type):
    if transform_type == 0:
        data_scaled = scaler.fit_transform(data)
    else:
        data_scaled = scaler.transform(data)
    return data_scaled
