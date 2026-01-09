# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:39:52 2024

@author: yashd
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TdidfTransformer
########Loading the daataset
email_data=pd.read_csv("C:/11-knn/sms_raw_NB.csv",encoding='ISO-8859-1')
#These sms are in text form open the dataframe and there are ham or spam 
#Clearning the data 
#The function tokenizes the text and removes words 
#with fever than 4 chracters.
import re
def cleaning_text(i):
    i=re.sub("[^A-Z a-z ""]+"," ",i ).lower()
    w=[]
    #Every thing else A to Z and a to z is going to convert to space and 
    #we will take each row and tokenize 
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
    return (" ".join(w))

#Testing above function with sample text
    cleaning_text("Hope you are having good week.just checking ")
    cleaning_text("Hope i can i understand your feeling12321.123.hi how are you ?  ")
    cleaning_text(" Hi how are you  ")

#Note the dataframe size is 5559 ,2  now removing empty spaces
#removing empty rows 
email_data = email_data.loc[email_data.text != " ",:]
email_data.shape
#You can use count vectorizer which directly converts a collection of documenation
#First we will splite data 
from sklearn.model_selection import train_test_split
email_train,email_test = train_test_split(email_data, test_size=0.2)

#Splits each email into a list of words 
#creating matrix of token count for entire dataframe

def split_into_words(i):
    return[word for word in i.split(" ")]

#defining the prepartion of mail text into word count martix format 
#countVector: Convert the emails into a matrix of token counts 
#fit(): learns the vocabulary from text data
#transform(): Converts text data into a token count matrix

email_bow = CountVectorizer(analyzer=split_into_words).fit(email_data.text)

#Defining BOW for all the dataFrames
all_emails_matrix=email_bow.transform(email_data.text)
train_emails_matrix=email_bow.transform(email_data.text)

#For testing messages 
test_email_matrix = email_bow.transform(email_data.text)

#Learning Term weight and normalization entire emails 
tfidf_transformer = TdidfTransformer().fit(all_emails_matrix)
#Prepraining TFIDF for train matrix
train_tfidf = tfidf_transformer.transform(train_emails_matrix)
train_tfidf.shape

test_tfidf = tfidf_transformer.transform(train_emails_matrix)
test_tfidf

#Now apply naive bayes 
from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()
classifier_mb.fit(train_tfidf,email_train.type)
#email_train.type: This is the column in the training dataset 
#(email_train) that containts the target labels 
#Which sepcify whether each message is spam or ham (non spam )
#The .type attribute refers to that specific column
#in the email_train dataframe 
#traing data prepraded in terms of tfidf and 
#labels of corresponding training 
#evaluation on test data 
test_pred_m = classifier_mb.predict(test_tfidf)

#Calculating accuracy 
accuracy_test_m = np.mean(test_pred_m==email_test.type)
accuracy_test_m 

# Evaluation on Test data 

#Traing data accuracy
train_pred_m = classifier_mb.predict(train_tfidf)
accuracy_train_m = np.mean(train_pred_m == email_train.type)
accuracy_train_m

#Test Data (with Laplace Smoothing ): This accuracy is
#computed after applying Laplace smoothing (with alpha= 3)
#To the Naive Bayes model
#interpretation: Sommthing helps avoid issues when encountering 
#words in the test data that were not seen in the trainig data
#(zero-frequency problem)
classifier_mb_lap=MB(alpha=3)
classifier_mb_lap.fit(train_tfidf,email_train.type)
#Accuracy after tuning
test_pred_lap = classifier_mb_lap.predict(test_tfidf)
accuracy_test_lap = np.mean(test_pred_lap == email_test.type)
accuracy_test_lap
accuracy_score(test_pred_lap, email_test.type)

from sklearn.metrics import accuracy_score
accuracy_score(test_pred_lap, email_test.type)
pd.crosstab(test_pred_lap,email_test.type)

#Traning data accuracy
train_pred_lap = classifier_mb_lap.predict(train_tfidf)
accuracy_train_lap = np.mean(train_pred_lap == email_train.type)
accuracy_train_lap








