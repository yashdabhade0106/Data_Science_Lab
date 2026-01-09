# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:35:25 2024

@author: yashd
"""

# Import requried labraries
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

#Smple dataset

transaction=[
    ['Milk','Bread','Butter'],
    ['Bread','Eggs'],
    ['Milk','Bread','Eggs','Butter'],
    ['Bread','Eggs','Butter'],
    ['Milk','Bread','Eggs']
    ]

# Step 1: Convert the datasets into fromat suitable for apriori
te = TransactionEncoder()
te_ary = te.fit(transaction).transform(transaction)
df = pd.DataFrame(te_ary, columns=te.columns_)

#Step2: Apply the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

 #Step 3: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets,metric="lift",min_threshold=1)
# Step 4 : Output the result
print("Frequent Itemsets: ")
print(frequent_itemsets)

print("/nAssociation Rules ")
print(rules[['antecedents','consequents','support','confidence','lift']]) 
