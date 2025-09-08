# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:08:58 2024

@author: yashd
"""

import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

file_path = "C:/9-pca_svd/Entertainment.csv.xls"
data = pd.read_csv(file_path)

#Step1 : Normalization the review score
#We use MinMaxScxalar to scale the reviews between 0 to 1
scaler = MinMaxScaler()
data['Normalized_Reviews'] = scaler.fit_transform(data[['Reviews']])

#Step2 : Compute the cosine similarity between titles based on
#the normalized reviews

cosine_sin_reviews = cosine_similarity(data[['Normalized_Reviews']],data[['Normalized_Reviews']])

#Step3 :








