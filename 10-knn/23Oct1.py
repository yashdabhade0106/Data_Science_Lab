# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:30:39 2024

@author: yashd
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv("C:/11-knn/salaries.csv")
#Data prepration
#check for null values 
data.isnull().sum()
data.dropna()
data.columns