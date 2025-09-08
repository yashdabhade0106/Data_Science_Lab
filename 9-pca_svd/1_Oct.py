# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:34:11 2024

@author: yashd

"""

import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the csv File
file_path = "C:/9-pca_svd/game.csv.xls"
data = pd.read_csv(file_path)

#Step1 : Create a user item matrix (rows:user, columns: games, values: rating)
user_item_matrix = data.pivot_table(index='userId',columns='game',values='rating')

"""
pivot_table: This function reshapes the DataFrame into a matrix where:
    
    Each row represents a user (identified by userId),
    Each columns represents a game (identified by game )
    The values in the matrix represent the rating that
    user gave to the games.
    
"""
#Step 2 : Fill the Nan values with 0 (assuming no rating means the game has not )
user_item_matrix_filled = user_item_matrix.fillna(0)
'''
This line replaces the any missing values(NaNs)
in the user-item matrix with0,
indicating that the user did not rate that particular game.

'''
#Step 3 : Compute the cosine similarity betwwen users based on raw rating 
user_similarity = cosine_similarity(user_item_matrix_filled )

#Convert similarity matrix to a DataFrame for easy reference
user_similarity_df = pd.DataFrame(user_similarity, index = user_item_matrix.index,columns=user_item_matrix.index)

#Step 4 : Function to get game recommendation for a specific based o similarity
def get_collabrative_recommendation_for_user(user_id,num_recommendation=5):
    #Get the similarity scores for the input user with all other users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    #Get the most similar users (excluding the user themselves )
    similar_users = similar_users.drop(user_id)

    #Select the top N similar users to limit noise(e.g., top 50 users)
    top_similar_users = similar_users.head(50)
    #This selection the top 50 most similar users to list noise in the recommendation 
    #Get rating of these similar users, weigted by their similarity scored

    weighted_ratings = np.dot(top_similar_users.values,user_item_matrix_filled.loc[top_similar_users.index])

    #np.dot: this computes the dot products between the 
    # Similarity scores of the top similar user and 
    #their corresponding rating in the user-item matrix,
    #The resul is an array of weighted rating for each game.
    #Normalize by the sum of similarity 

    sum_of_similarity = top_similar_users.sum()


    if sum_of_similarity > 0:
          weighted_ratings /= sum_of_similarity
        
        #The weighted rating are normlized by dividing by the 
        #Sum of similarity to avoid baising toward user
        #higher rating
        
        
    #Recommend games that the user hasn't rated yet
    user_rating= user_item_matrix_filled.loc[user_id]
    unrated_games = user_rating[user_rating == 0]
    #Identifies game sthat the target user has not rated (i.e, rated 0.)

    #Get the weighted scores for unrated games 
    game_recommendations = pd.Series(weighted_ratings,index = user_item_matrix_filled.columns).loc[unrated_games.index
                                                                                                  ]
      #This creates a pandas Series from the weighted ratings
      #and filters it to include only unrated games.
      #Finally it sorts the recommendation in desecnding order
      #and return the top specified number of recommendation 
      
      #Return the top 'num_recommendation' game recommendation 
    return game_recommendations.sort_values(ascending = False).head(num_recommendation)



#Example usage: Get recommendation for a user with ID 3 
recommeded_games = get_collabrative_recommendation_for_user(user_id=3)

#Print the recommended games
print("Recommended games for user 3 : ")
print(recommeded_games)




