# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:43:25 2024

@author: yashd
"""

'''
Problem Statement :-
This dataset contains information of users in a social networks.
This social network has several business clinets which can post ads
on it.
One of the clinets has a car company which has just 
Launched a luxury SUV for a ridiculus price.
Build a Bernoulli Naive Bayes model using this dataset and 
classify which of the users of the social networks are going to purchase
this luxury SUV. I implies that there was a purchase 
and 0 implies there wasn't a purchase.

1. Business Problem 
1.1. What is the business objective ?
    1.1.1. This will help you bring those audiences to your website 
    who are intrested in cars.
    And, there will be many of those who are planning to buy a car in the near futur.
    
    1.1.2 Communicating with your target audience over social media 
    is always a great way to build a good market reputatio.
    Try responsible to people's automobile related queries on Twitter and Facebook
    pages quickly t be their first choice when it comes to buying a car.
    
1.2. Are there anu constraints?
     Not having a clear marketing or social media strategy may 
     result in reduced benefits for your business 
     
     Additional resource may be needed to manage 
     your online presence
     
     Social media is immediate and needs daily monitoring 
     
     If you don't activetly manage your social media presences,
     you may not see any reak benefits 
     
     There is a risk of unwanted or
     inappropriate behavior on your site 
     including bullying and harassment
     
     Greater exposure online has the potential to attract risks.
     Risks can include negative feedback information,
     Leaks or hacking
     
'''
#2. Work on each feature of the dataset to create a data dictionary 
#User ID: Integer type which is not contributory 
#Gender: Object Type need to be label encoding
#Age : Integer 
#EstimateSalary: Integer 
#Purchased: Integer Type 
#############################################
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#Let us first import the dataset 
car = pd.read_csv("C:/11-knn/NB_Car_Ad.csv")

#Exploratory data analysis 
car.columns
car.dtype
car.describe()

#Min age of employee is 18 years 
#Max age of employee is 60 years 
#Average age is 37.65
#Min salary of user is 15000
#Max salary of user is 1,50,000
#Average salary is 69742
car.isna().sum()
car.drop(['User ID'],axis=1,implace=True)
car.dtypes
plt.hist (car.Age)
#Age is normal distributed
plt.hist(car.EstimatedSalary)
#Data is normally distributes but right skewed 
##############################################

#Data Pre-processing 

#3.1 Data Cleaning, feature Engineering,etc.
car.dtypes

#The column gender is of object type 
#Let us apply label encoder to input features 

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
#This is model of label_encoder which is applied to all the object type 
car['Gender']=label_encoder.fit_transform(car['Gender'])

#Now let us apply normalization function 
def norm_funct(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

car_norm = norm_funct(car)
car_norm.describe()

##########################################
#Now let us desinate train data amd Test data

from sklearn.model_selection import train_test_split
car_train,car_test = train_test_split(car_norm,test_size=0.2)

col_names1=list(car_train.columns)
train_X=car_train[col_names1[0:2]]
train_y=car_train[col_names1[3]]
col_names2=list(car_train.columns)
test_X=car_test[col_names2[0:2]]
test_y=car_test[col_names2[3]]

###############################################
#Model Bulding 
#Bulid the model on the scaled data (try multiple options )
#bulid a Naive Bayes model
#Like MultinomialMB, this classifier is sutiable for discrete for discrete data. The 
#BernoulliMB is designed for binary/boolean features 

from sklearn.naive_bayes import BernoulliNB as BB
classifier_bb=BB()

classifier_bb.fit(train_X,train_y)
#Let us now evaluate on test data 
test_pred_b=classifier_bb.predict(test_X)
#Accuracy of the prediction
accuracy_test_b=np.mean(test_pred_b==test_y)
accuracy_test_b
#Let us now ckeck confusion matrix
from sklearn.metrics import accuracy_score












