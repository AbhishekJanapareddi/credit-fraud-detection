# -*- coding: utf-8 -*-
"""
Created on Dec 30, 2023

@author: Abhishek
"""

from src.data.data_preproc import get_file_path, data_process
from src.models.models import model_train
from src.features.feature_engineering import feature_engineering


def main():
    file_path = get_file_path()
    data = data_process(file_path)
    data = feature_engineering(data)
    model_train(data)
    
    
if __name__ == "__main__":
    main()
