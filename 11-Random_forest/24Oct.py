# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:11:22 2024

@author: yashd
"""

import pandas as pd 
df=pd.read_csv("C:/12-Random_forest/movies_classification.csv")
df.info()
#Movie_classifictaion dataset contains two columns which are object
#Hence convert into dummies 
df=pd.get_dummies(df,columns=["3D_available","Genre"],drop_first=True)
#Let us assign input and output variables
predictors = df.loc[:,df.columns!="Start_Tech_Oscar"]
#Except Start_Tech_Oscar ,result all columns are assigned as predictors
#predictor has got 20 columns
target=df["Start_Tech_Oscar"]
################################
#Let us pratition the dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(predictors, target,test_size=0.2, random_state = 0)
################################
#Model selection 
from sklearn.ensemble import RandomForestClassifier
rand_for = RandomForestClassifier(n_estimators=500,n_jobs=1,random_state=13)
#n_estimators: It is number of trees in the forest, always in range 500
# to 1000
#n_jobs=1 means number of jobs running parallel=1, if it is -1 then multiple 
#random_state = controls randomness in bootstrapping
#Bootstrapping is getting samples replaced 
rand_for.fit(X_train,y_train)
pred_X_train = rand_for.predict(X_train)
pred_X_test = rand_for.predict(X_test)
#######
#let us check the preformance of the model
from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(pred_X_test, y_test)
confusion_matrix(pred_X_test, y_test)


##################
#For training dataset
accuracy_score(pred_X_train,y_train)
confusion_matrix(pred_X_train,y_train)
###########################



















