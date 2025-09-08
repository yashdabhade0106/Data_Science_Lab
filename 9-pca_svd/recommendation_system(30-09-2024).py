# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:03:44 2024

@author: icon
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load csv file
data=pd.read_csv(r"C:\10-recommendation_system\Entertainment.csv.xls")

#step:1 Preprocess the 'category' columns using TF-IDF
tfidf=TfidfVectorizer(stop_words='english')#remove common stopwords
tfidf_matrix=tfidf.fit_transform(data['Category'])#fit and transform


#step 2: compute the cosine similarity between titles
cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)

#step 3: create a function to recommend titles based on similarity
def get_recommendations(title,cosine_sim=cosine_sim):
    #get the index of the title that matches the input
    idx=data[data['Titles']==title].index[0]
    ''' add the comments '''
    
    #get the pairwise similarity scores of all titiles with that title'
    sim_scores=list(enumerate(cosine_sim[idx]))
    
    #sort the titles based on the similarity scores in descending order
    sim_scores=sorted(sim_scores,key=lambda  x: x[1],reverse=True)
    
    #get the indices of the most siimilar titles
    sim_indices=[i[0] for i in sim_scores[1:6]]
    #exclude the first as its the title itself
    
    #return the top 5 similar titles
    return data['Titles'].iloc[sim_indices]
    
#TEST THE recommendations system with an example title
example_title='Toy Story (1995)'
example_titles=get_recommendations(example_title)

print(f"Recommendation for'{example_title}':")
for title in example_titles:
    print(title)