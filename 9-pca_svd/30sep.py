# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:09:42 2024

@author: om
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Load the CSV file
file_path="C:/10-recommandation engine/Entertainment.csv"
data = pd.read_csv(file_path)

#step 1: Preprocess the 'Category' column using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
#Remove common stop words
tfidf_matrix = tfidf.fit_transform(data['Category'])
#Fit and transform the category data

#step 2: Compute the cosine similarity betweeen titles
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#step 3: Create a function to recommend titles based on similarity

def get_recommendations(title, cosine_sim=cosine_sim):
    #get the index of the title that matches the input title
    idx = data[data['Title']==title].index[0]
    """
    data['Titles']==title 
    This creates a boolean mask (a series)
    
    
    
    
    """
    #get the pairwise similarity scores of all titles with that title
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    #Sort the titles based on the similarity scores in descending on
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    #Get the indices of the most similar titles
    sim_indices = [i[0] for i in sim_scores[1:6]]
    #Exclude the first as it's the title itself
    
    #return the top 5 most similar titles
    return data['Titles'].iloc[sim_indices]


#Test the recommendation system with an example title
example_title = ''