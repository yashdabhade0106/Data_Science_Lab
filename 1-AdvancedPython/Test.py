# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:33:01 2024

@author: yash
"""

#DATA pre-processing
import pandas as pd
#let us import dataset
df=pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv.xls") 
#let us check data type of column 
df.dtypes
#salaries data type is float ,let us convert into int 
df.Salaries=df.Salaries.astype(int)
df.dtypes

df.age=df.age.astype(int)
df.dtypes
###################################
#Identify the duplicate 
df_new = pd.read_csv("C:/5-Data_Prep/education.csv.xls") 
duplicate = df_new.duplicated()
#output of this column is single column 
#If there is duplicate record output - True
#If there is no duplicate record output - False
#Series will be created 

duplicate
sum(duplicate)
#output will be 0 
#Now let us import another sataset 
df_new1=pd.read_csv("C:/5-Data_Prep/mtcars_dup.csv.xls")
duplicate=df_new1.duplicated()
duplicate
sum(duplicate)
#There are 3 duplicate records 
#There is function called drop_duplicate 
#which will drop duplicate records
df_new2=df_new1.drop_duplicates()
duplicate2 = df_new2.duplicated()
duplicate2
sum(duplicate2)
###################################################
#Outliers Treatment
import pandas as pd 
import seaborn as sns 
df=pd.read_csv("C:/5-Data_Prep/ethnic diversity.csv.xls")
#Now let us find outliers in Salaries 
sns.boxplot(df.Salaries)
#There are outliers
#Let us check outliers in age cloumn
sns.boxplot(df.age)
#there are no outliers 
#Let us calculate IQR
IOR = df.Salaries.quantile(0.75).df.Salaries.quantile(0.25)
IOR


#############################################
#Trimming
import numpy as 

































