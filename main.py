# -*- coding: utf-8 -*-
"""
Created on Dec 2023

@author: Abhishek
"""

from src.data.data_preproc import get_file_path, data_process

def main():
    file_path = get_file_path()
    data_process(file_path)
    
if __name__ == "__main__":
    main()
