# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:56:01 2024

@author: yashd
"""
import csv
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Sample transaction dataset (uncomment for example)
'''
transactions = [['milk', 'bread', 'butter'],
                ['bread', 'eggs'],
                ['milk', 'bread', 'eggs', 'butter'],
                ['bread', 'eggs', 'butter'],
                ['milk', 'bread', 'eggs']]
'''

# Initialize a list to hold the rows as strings from the CSV
csv_rows = []

# Open and read the CSV file containing the grocery transactions
with open("C:/9-pca_svd/groceries.csv.xls", mode='r') as file:
    reader = csv.reader(file)
    
    # Append each row to the list
    for row in reader:
        csv_rows.append(row)

# Output the CSV data as rows (optional)
print(csv_rows)

# Step 1: Convert the transaction data into a format usable by the Apriori algorithm
trans_encoder = TransactionEncoder()
transaction_array = trans_encoder.fit(csv_rows).transform(csv_rows)
transaction_df = pd.DataFrame(transaction_array, columns=trans_encoder.columns_)

# Step 2: Apply the Apriori algorithm to discover frequent itemsets with minimum support
frequent_itemsets = apriori(transaction_df, min_support=0.01, use_colnames=True)
print(frequent_itemsets)

# Step 3: Generate association rules from the frequent itemsets using a lift metric
assoc_rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.7)

# Step 4: Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(assoc_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

###################################################################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

transactions = pd.read_csv(r"C:/9-pca_svd/book.csv.xls")

# Step 1: Convert the dataset into a suitable format for Apriori
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df_transformed = pd.DataFrame(te_array, columns=te.columns_)

# Display the transformed dataframe
print(df_transformed)

# Step 2: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df_transformed, min_support=0.001, use_colnames=True)
print(frequent_itemsets)

# Step 3: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Step 4: Output the results
print("\nFrequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

##########################################################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Step 1: Load the dataset correctly (CSV or Excel based on the file type)
transactions = pd.read_csv(r"C:/9-pca_svd/my_movies.csv.xls")  # Corrected to CSV format

# Step 2: Convert the dataset into a suitable format for Apriori
transaction_list = transactions.values.tolist()

te = TransactionEncoder()
te_array = te.fit(transaction_list).transform(transaction_list)
df_transformed = pd.DataFrame(te_array, columns=te.columns_)

# Step 3: Apply the Apriori algorithm
frequent_itemsets = apriori(df_transformed, min_support=0.001, use_colnames=True)

# Step 4: Generate association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Output results
print("\nFrequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
############################################################

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

transactions = pd.read_csv(r"C:/9-pca_svd/myphonedata.csv.xls")

# Step 1: Check the structure of the dataset
print(transactions.head())  # This will show you the first few rows of your dataset
transaction_list = transactions.values.tolist()

# Step 2: Convert the dataset using TransactionEncoder
te = TransactionEncoder()
te_array = te.fit(transaction_list).transform(transaction_list)
df_transformed = pd.DataFrame(te_array, columns=te.columns_)

# Step 3: Display the transformed data
print(df_transformed)

# Step 4: Apply the Apriori algorithm to find frequent itemsets (set appropriate min_support)
frequent_itemsets = apriori(df_transformed, min_support=0.1, use_colnames=True)

# Step 5: Display the frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Step 6: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Step 7: Output the results
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
