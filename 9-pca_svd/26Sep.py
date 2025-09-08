# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:07:15 2024

@author: yashd
"""

import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 
from mlxtend.preprocessing import TransactionEncoder

#Step 1 : Simultaing healthcare transaction (symptoms/diseases/tratment)


healthcare_data =[
    ['Fever','Cough','COVID-19'],
    ['Cough','Sore Throat','Flu'],
    ['Cough','Sore Throat','Shortnessn of Breadth','COVID-19'],
    ['Cough','Sore Throat','Flu','Headache'],
    ['Fever','Body Ache','Flu'],
    ['Fever','Cough','COVID-19','Shortness of Breadth'],
    ['Sore Throat','Headache','Cough'],
    ['Body Ache','Fatigue','Flu']]

# Step 1: Convert the datasets into fromat suitable for apriori
te = TransactionEncoder()
te_ary = te.fit(healthcare_data).transform(healthcare_data)
df = pd.DataFrame(te_ary, columns=te.columns_)

#Step2: Apply the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

 #Step 3: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.7)
# Step 4 : Output the result
print("Frequent Itemsets: ")
print(frequent_itemsets)

print("/nAssociation Rules ")
print(rules[['antecedents','consequents','support','confidence','lift']]) 

"""

"""




















