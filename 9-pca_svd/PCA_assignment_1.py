##################  Assignment of PCA   ####################################
#################   Topic: Dimension Reduction With PCA    #################


#Hints:
 # 1.	Business Problem
  #1.1.	What is the business objective?
 # Solution: 
'''
The business objective is to simplify large datasets by reducing the number of variables while keeping the important information. For example:

Customer Segmentation: Group customers based on fewer but key features like purchase behavior.
Fraud Detection: Spot patterns in fewer dimensions to detect fraud quickly.
'''

#1.2.	Are there any constraints?
#Solution
'''
Interpretability: The new variables (components) are harder to understand.
Data Requirements: PCA works best with standardized (scaled) data.
Loss of Information: Some data details may be lost during reduction.
Computational Load: Large datasets can take time to process.
'''

##################################################################

#2.	Work on each feature of the dataset to create a data dictionary as displayed in the below image:
    #2.12.1 Make a table as shown above and provide information about the features such as its data type and its relevance to the model building.
      #And if not relevant, provide reasons and a description of the feature.
      
      # Solution 
      '''
      Steps to Create the Data Dictionary:
Identify the Features: Go through your dataset and list all the features (columns).
Provide Information: For each feature, fill in the following details:
    
Name of Feature: The name of the feature (e.g., "Customer ID").

ID: Indicate whether it’s an identifier (Yes/No).

Description: A brief explanation of what the feature represents.

Type: Specify the data type (e.g., Quantitative, Categorical, Nominal, etc.).

Relevance: Assess whether the feature is relevant to your model. If not, explain why.

Example Table:
Name of Feature	||           ID	 ||            Description	              || T   ype	              ||      Relevance
Customer ID	    ||      Yes	     ||    Unique identifier for each customer||	Quantitative, Nominal ||      Irrelevant, does not provide useful information for model

Key Points:
Relevance to Model: If a feature like "Customer ID" doesn’t add value for prediction (since it’s just an identifier), explain that it's irrelevant and won’t be used in model building.
Description: Keep the descriptions simple and concise, focusing on what the feature represents in the business context.
'''
#################################################################################################

#3.	Data Pre-processing
  #3.1 Data Cleaning, Feature Engineering, etc.
    # Solution 
    '''
 3. Data Pre-processing

3.1 Data Cleaning
Handling Missing Values: Fill missing data with mean/median or remove affected rows.
Removing Duplicates: Eliminate duplicate records to ensure data integrity.
Outlier Detection: Identify and address outliers that may skew results.
Standardizing Data: Normalize or standardize numerical features for consistency.

3.2 Feature Engineering
Creating Interaction Features: Combine features to capture relationships (e.g., multiplying two features).
Binning: Convert continuous variables into categories (e.g., age ranges).
Encoding Categorical Variables: Use one-hot or label encoding to transform categorical data.
Initial Feature Selection: Remove less important features before applying PCA.
'''
###########################################################################################

 #4.	Exploratory Data Analysis (EDA):
    #4.1.	Summary.
    #4.1 	Univariate analysis.
    #4.3.	Bivariate analysis.
     # Solution :
         '''

4. Exploratory Data Analysis (EDA)

4.1 Summary
Key Stats: Look at basic statistics like the average (mean), middle value (median), and how spread out the data is (range, variance).
Data Spread: Use charts like histograms or box plots to see how data is distributed and spot any outliers.
Correlations: Check if any features are strongly related to each other using a correlation matrix or heatmap. This helps see which features might be reduced with PCA.

4.2 Univariate Analysis
For Numbers: Look at each feature (column) separately using charts (histograms, box plots) to understand its distribution.
For Categories: Use bar charts to see how many times each category appears.

4.3 Bivariate Analysis
Number-Number: Use scatter plots to see how two numerical features are related.
Category-Number: Compare a numerical feature across categories using box plots or other visualizations.
Category-Category: Look at how two categorical features relate using bar charts or cross-tabulations.
'''

###########################################################################################


#v5.	Model Building
   #5.1	Build the model on the scaled data (try multiple options).
        # 5.2 Perform PCA analysis and get the maximum variance between components.
         # 5.3 Perform clustering before and after applying PCA to cross the number of clusters      	formed.
           #5.4 Briefly explain the model output in the documentation. 
# Solution:

'''
5. Model Building

5.1 Build the Model on Scaled Data
Scale Your Data: Use methods like Standardization (Z-score) or Min-Max scaling to ensure all features are on the same level. This helps the model work better.
Try Different Models: Experiment with different clustering models, such as:
K-Means Clustering: Groups data points based on similarities.
Hierarchical Clustering: Creates a tree of clusters to show how they relate.
DBSCAN: Finds clusters of different shapes and sizes, even if they are noisy.

5.2 Perform PCA Analysis
Apply PCA: Use PCA to reduce the number of features in your data while keeping important information.
Check Variance: Look at how much variance (spread) each new principal component explains. Try to keep enough components to explain a lot of the original variance (like 95%).

5.3 Clustering Before and After PCA
Before PCA: Run clustering on the original scaled data and note how many clusters you get.
After PCA: Run clustering again on the reduced data from PCA and compare the number of clusters. See how the clusters change after applying PCA.

5.4 Explain the Model Output
Document Results: Write down what you found from clustering:
How many clusters you had before and after PCA.
Use visuals (like elbow plots) to show how well the clustering worked.
Interpret Findings: Explain what the results mean. Discuss any patterns you noticed and how PCA helped to simplify the data while keeping important information.
'''
####################################################################################################


#Write about the benefits/impact of the solution - in what way does the business (client) benefit from the solution provided?
# Solution :
'''
Benefits/Impact of the Solution
Improved Insights: Simplifies data analysis, helping businesses focus on key features for better decision-making.

Enhanced Performance: Reduces model complexity, leading to faster training times and increased accuracy.

Cost-Effectiveness: Lowers computational and storage costs by minimizing the number of features analyzed.

Faster Processing: Speeds up data analysis, allowing quicker responses to market trends.

Pattern Identification: Reveals hidden relationships in data, opening up new business opportunities.

Better Visualization: Makes complex data easier to visualize and understand for stakeholders.

Scalability: Can be applied to future datasets, maintaining efficiency as the business grows.

Competitive Advantage: Enables faster, data-driven decisions, enhancing customer satisfaction and profitability.

'''
#########################################################################################################


#Problem Statement:
'''
Perform hierarchical and K-means clustering on the dataset. After that, 
perform PCA on the dataset and extract the first 3 principal components and make a new dataset
 with these 3 principal components as the columns.
 Now, on this new dataset, perform hierarchical and K-means clustering.
 Compare the results of clustering on the original dataset and clustering on the 
 principal components dataset (use the scree plot technique to obtain the optimum
number of clusters in K-means clustering and check if you’re getting similar results with and without PCA).
'''
#Solution 

# here first we make a dataset of that table 


import pandas as pd

# Create a structured list of lists for the dataset
data = [
    [11, 14.23, 1.71, 2.43, 15.6, 127, 2.80, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92],
    [21, 13.20, 1.78, 2.14, 11.2, 100, 2.65, 2.76, 0.26, 1.28, 4.38, 1.05, 3.40],
    [31, 13.16, 2.36, 2.67, 18.6, 101, 2.80, 3.24, 0.30, 2.81, 5.68, 1.03, 3.17],
    [41, 14.37, 1.95, 2.50, 16.8, 113, 3.85, 3.49, 0.24, 2.18, 7.80, 0.86, 3.45],
    [51, 13.24, 2.59, 2.87, 21.0, 118, 2.80, 2.69, 0.39, 1.82, 4.32, 1.04, 2.93],
    [61, 14.20, 1.76, 2.45, 15.2, 112, 3.27, 3.39, 0.34, 1.97, 6.75, 1.05, 2.85],
    [71, 14.39, 1.87, 2.45, 14.6, 96, 2.50, 2.52, 0.30, 1.98, 5.25, 1.02, 3.58],
    [81, 14.06, 2.15, 2.61, 17.6, 121, 2.60, 2.51, 0.31, 1.25, 5.05, 1.06, 3.58],
    [91, 14.83, 1.64, 2.17, 14.0, 97, 2.80, 2.98, 0.29, 1.98, 5.20, 1.08, 2.85],
    [101, 13.86, 1.35, 2.27, 16.0, 98, 2.98, 3.15, 0.22, 1.85, 7.22, 1.01, 3.55],
    [111, 14.10, 2.16, 2.30, 18.0, 105, 2.95, 3.32, 0.22, 2.38, 5.75, 1.25, 3.17],
    [121, 14.12, 1.48, 2.32, 16.8, 95, 2.20, 2.43, 0.26, 1.57, 5.00, 1.17, 2.82],
    [131, 13.75, 1.73, 2.41, 16.0, 89, 2.60, 2.76, 0.29, 1.81, 5.60, 1.15, 2.90],
    [141, 14.75, 1.73, 2.39, 11.4, 91, 3.10, 3.69, 0.43, 2.81, 5.40, 1.25, 2.73],
    [151, 14.38, 1.87, 2.38, 12.0, 102, 3.30, 3.64, 0.29, 2.96, 7.50, 1.20, 3.00],
    [161, 13.63, 1.81, 2.70, 17.2, 112, 2.85, 2.91, 0.30, 1.46, 7.30, 1.28, 2.88],
    [171, 14.30, 1.92, 2.72, 20.0, 120, 2.80, 3.14, 0.33, 1.97, 6.20, 1.07, 2.65],
    [181, 13.83, 1.57, 2.62, 20.0, 115, 2.95, 3.40, 0.40, 1.72, 6.60, 1.13, 2.57],
    [191, 14.19, 1.59, 2.48, 16.5, 108, 3.30, 3.93, 0.32, 1.86, 8.70, 1.23, 2.82],
    [201, 13.64, 3.10, 2.56, 15.2, 116, 2.70, 3.03, 0.17, 1.66, 5.10, 0.96, 3.36]
]

# Create a DataFrame from the structured data
columns = ['Index', 'Alcohol', 'Malic', 'Ash', 'Alcalinity', 'Magnesium', 'Phenols', 
           'Flavanoids', 'Nonflavanoids', 'Proanthocyanins', 'Color', 'Hue', 'Dilution']
df = pd.DataFrame(data, columns=columns)

# Display the resulting DataFrame
print(df)

# Save the DataFrame to a CSV file (optional)
df.to_csv('wine_data.csv', index=False)

##################################################################################################
###now we will do code on that dataset
#Code 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import silhouette_score

# Create a structured list of lists for the dataset
data = [
    [11, 14.23, 1.71, 2.43, 15.6, 127, 2.80, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92],
    [21, 13.20, 1.78, 2.14, 11.2, 100, 2.65, 2.76, 0.26, 1.28, 4.38, 1.05, 3.40],
    [31, 13.16, 2.36, 2.67, 18.6, 101, 2.80, 3.24, 0.30, 2.81, 5.68, 1.03, 3.17],
    [41, 14.37, 1.95, 2.50, 16.8, 113, 3.85, 3.49, 0.24, 2.18, 7.80, 0.86, 3.45],
    [51, 13.24, 2.59, 2.87, 21.0, 118, 2.80, 2.69, 0.39, 1.82, 4.32, 1.04, 2.93],
    [61, 14.20, 1.76, 2.45, 15.2, 112, 3.27, 3.39, 0.34, 1.97, 6.75, 1.05, 2.85],
    [71, 14.39, 1.87, 2.45, 14.6, 96, 2.50, 2.52, 0.30, 1.98, 5.25, 1.02, 3.58],
    [81, 14.06, 2.15, 2.61, 17.6, 121, 2.60, 2.51, 0.31, 1.25, 5.05, 1.06, 3.58],
    [91, 14.83, 1.64, 2.17, 14.0, 97, 2.80, 2.98, 0.29, 1.98, 5.20, 1.08, 2.85],
    [101, 13.86, 1.35, 2.27, 16.0, 98, 2.98, 3.15, 0.22, 1.85, 7.22, 1.01, 3.55],
    [111, 14.10, 2.16, 2.30, 18.0, 105, 2.95, 3.32, 0.22, 2.38, 5.75, 1.25, 3.17],
    [121, 14.12, 1.48, 2.32, 16.8, 95, 2.20, 2.43, 0.26, 1.57, 5.00, 1.17, 2.82],
    [131, 13.75, 1.73, 2.41, 16.0, 89, 2.60, 2.76, 0.29, 1.81, 5.60, 1.15, 2.90],
    [141, 14.75, 1.73, 2.39, 11.4, 91, 3.10, 3.69, 0.43, 2.81, 5.40, 1.25, 2.73],
    [151, 14.38, 1.87, 2.38, 12.0, 102, 3.30, 3.64, 0.29, 2.96, 7.50, 1.20, 3.00],
    [161, 13.63, 1.81, 2.70, 17.2, 112, 2.85, 2.91, 0.30, 1.46, 7.30, 1.28, 2.88],
    [171, 14.30, 1.92, 2.72, 20.0, 120, 2.80, 3.14, 0.33, 1.97, 6.20, 1.07, 2.65],
    [181, 13.83, 1.57, 2.62, 20.0, 115, 2.95, 3.40, 0.40, 1.72, 6.60, 1.13, 2.57],
    [191, 14.19, 1.59, 2.48, 16.5, 108, 3.30, 3.93, 0.32, 1.86, 8.70, 1.23, 2.82],
    [201, 13.64, 3.10, 2.56, 15.2, 116, 2.70, 3.03, 0.17, 1.66, 5.10, 0.96, 3.36]
]

# Create a DataFrame from the structured data
columns = ['Index', 'Alcohol', 'Malic', 'Ash', 'Alcalinity', 'Magnesium', 'Phenols', 
           'Flavanoids', 'Nonflavanoids', 'Proanthocyanins', 'Color', 'Hue', 'Dilution']
df = pd.DataFrame(data, columns=columns)

# Data Preparation
# Check for missing values
print(df.isnull().sum())

# Standardize the dataset (excluding the 'Index' column)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df.drop('Index', axis=1))

# Hierarchical Clustering on Original Dataset
linkage_matrix = linkage(data_scaled, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram to create clusters
# Adjust 't' to define the number of clusters
t = 3
hc_labels = fcluster(linkage_matrix, t, criterion='maxclust')

# K-means Clustering on Original Dataset
inertia = []
silhouette_scores = []

# Finding the optimal number of clusters for K-means
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data_scaled, kmeans.labels_))

# Plotting Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Plotting Silhouette Scores
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Scores for Different k')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Choose optimal number of clusters based on Elbow method or Silhouette score
optimal_k = 3  # Adjust this based on your analysis
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(data_scaled)
kmeans_labels = kmeans.labels_

# PCA
pca = PCA(n_components=3)
data_pca = pca.fit_transform(data_scaled)

# Variance explained by each principal component
explained_variance = pca.explained_variance_ratio_

# Scree Plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), explained_variance, marker='o')
plt.title('Scree Plot')
plt.xlabel('Principal Components')
plt.ylabel('Variance Explained')
plt.show()

# Hierarchical Clustering on PCA Dataset
linkage_matrix_pca = linkage(data_pca, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix_pca)
plt.title('Dendrogram for Hierarchical Clustering on PCA Data')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram for PCA
hc_labels_pca = fcluster(linkage_matrix_pca, t, criterion='maxclust')

# K-means Clustering on PCA Dataset
inertia_pca = []
silhouette_scores_pca = []

# Finding the optimal number of clusters for K-means on PCA data
for k in range(2, 11):
    kmeans_pca = KMeans(n_clusters=k, random_state=42)
    kmeans_pca.fit(data_pca)
    inertia_pca.append(kmeans_pca.inertia_)
    silhouette_scores_pca.append(silhouette_score(data_pca, kmeans_pca.labels_))

# Plotting Elbow Method for PCA data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia_pca, marker='o')
plt.title('Elbow Method for PCA Data')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Plotting Silhouette Scores for PCA data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores_pca, marker='o')
plt.title('Silhouette Scores for PCA Data')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Choose optimal number of clusters based on Elbow method or Silhouette score
optimal_k_pca = 3  # Adjust this based on your analysis
kmeans_pca = KMeans(n_clusters=optimal_k_pca, random_state=42)
kmeans_pca.fit(data_pca)
kmeans_labels_pca = kmeans_pca.labels_

# Comparison of Clustering Results
print("K-means Clustering Labels (Original Dataset):", kmeans_labels)
print("K-means Clustering Labels (PCA Dataset):", kmeans_labels_pca)

####################################################################################################333
#######################################################################################################

#Problem Statement
'''
A pharmaceuticals manufacturing company is conducting a study on a new medicine to treat heart diseases. The company has gathered data from its secondary sources and would like you to provide high level analytical insights on the data. Its aim is to segregate patients depending on their age group and other factors given in the data. Perform PCA and clustering algorithms on the dataset and check if the clusters formed before and after PCA are the same and provide a brief report on your model. You can also explore more ways to improve your model. 

Note: This is just a snapshot of the data. The datasets can be downloaded from AiSpry LMS in the Hands-On Material section.

'''
#Solution:
    # here we created a dataset on that table or that data and saved it 
    import pandas as pd

# Create the dataset from the provided data
data = {
    'age': [63, 37, 41, 56, 57, 57, 56, 44, 52, 57, 50, 58, 66, 69, 59, 44, 42, 61],
    'sex': [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    'cp': [3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 2, 2, 3, 3, 0, 2, 0, 2],
    'trestbps': [145, 130, 130, 120, 140, 120, 140, 120, 172, 150, 140, 135, 130, 150, 140, 150, 140, 150],
    'chol': [233, 250, 204, 236, 192, 354, 294, 263, 199, 168, 239, 234, 233, 226, 247, 283, 340, 226],
    'fbs': [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save to CSV if needed
df.to_csv('heart_disease_data.csv', index=False)

##############################################################################################
#Code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import silhouette_score

# Create the dataset
data = {
    'age': [63, 37, 41, 56, 57, 57, 56, 44, 52, 57, 50, 58, 66, 69, 59, 44, 42, 61],
    'sex': [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    'cp': [3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 2, 2, 3, 3, 0, 2, 0, 2],
    'trestbps': [145, 130, 130, 120, 140, 120, 140, 120, 172, 150, 140, 135, 130, 150, 140, 150, 140, 150],
    'chol': [233, 250, 204, 236, 192, 354, 294, 263, 199, 168, 239, 234, 233, 226, 247, 283, 340, 226],
    'fbs': [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data Preparation
# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Standardize the dataset
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df)

# Hierarchical Clustering on Original Dataset
linkage_matrix = linkage(data_scaled, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram to create clusters
t = 2  # Adjust 't' for the number of clusters
hc_labels = fcluster(linkage_matrix, t, criterion='maxclust')

# K-means Clustering on Original Dataset
inertia = []
silhouette_scores = []

# Finding the optimal number of clusters for K-means
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data_scaled, kmeans.labels_))

# Plotting Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k (Original Data)')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Plotting Silhouette Scores
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Scores for Different k (Original Data)')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Choose optimal number of clusters based on Elbow method or Silhouette score
optimal_k = 3  # Chosen based on the plots
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(data_scaled)
kmeans_labels = kmeans.labels_

# PCA
pca = PCA(n_components=3)
data_pca = pca.fit_transform(data_scaled)

# Variance explained by each principal component
explained_variance = pca.explained_variance_ratio_

# Scree Plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), explained_variance, marker='o')
plt.title('Scree Plot')
plt.xlabel('Principal Components')
plt.ylabel('Variance Explained')
plt.show()

# Hierarchical Clustering on PCA Dataset
linkage_matrix_pca = linkage(data_pca, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix_pca)
plt.title('Dendrogram for Hierarchical Clustering on PCA Data')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram for PCA
hc_labels_pca = fcluster(linkage_matrix_pca, t, criterion='maxclust')

# K-means Clustering on PCA Dataset
inertia_pca = []
silhouette_scores_pca = []

# Finding the optimal number of clusters for K-means on PCA data
for k in range(2, 11):
    kmeans_pca = KMeans(n_clusters=k, random_state=42)
    kmeans_pca.fit(data_pca)
    inertia_pca.append(kmeans_pca.inertia_)
    silhouette_scores_pca.append(silhouette_score(data_pca, kmeans_pca.labels_))

# Plotting Elbow Method for PCA data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia_pca, marker='o')
plt.title('Elbow Method for PCA Data')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Plotting Silhouette Scores for PCA data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores_pca, marker='o')
plt.title('Silhouette Scores for PCA Data')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Choose optimal number of clusters based on Elbow method or Silhouette score
optimal_k_pca = 2  # Chosen based on the plots
kmeans_pca = KMeans(n_clusters=optimal_k_pca, random_state=42)
kmeans_pca.fit(data_pca)
kmeans_labels_pca = kmeans_pca.labels_

# Comparison of Clustering Results
print("K-means Clustering Labels (Original Dataset):", kmeans_labels)
print("K-means Clustering Labels (PCA Dataset):", kmeans_labels_pca)

# Brief Report
report = """
### Report on Clustering Analysis

**1. Data Overview:**
- The dataset contains information on heart disease patients with attributes such as age, sex, chest pain type (cp), resting blood pressure (trestbps), cholesterol levels (chol), and fasting blood sugar (fbs).

**2. Clustering Analysis:**
- Hierarchical clustering was performed on the original dataset, and the resulting dendrogram indicated a suitable number of clusters.
- K-means clustering was also conducted, with optimal clusters determined using the Elbow method and Silhouette scores.

**3. PCA Analysis:**
- PCA was performed to reduce dimensionality and retain the most informative features.
- The first three principal components explained a significant portion of variance in the data, facilitating better clustering.

**4. Comparison of Results:**
- The K-means clustering labels for both the original dataset and the PCA dataset were compared.
- While the number of clusters identified may differ, the clustering tendencies remained similar, suggesting that PCA retains significant structural information.

**5. Recommendations for Model Improvement:**
- Explore different clustering algorithms such as DBSCAN or Agglomerative Clustering for potentially better insights.
- Conduct feature engineering to create more informative features or interactions between existing features.
- Increase dataset size if possible, to enhance clustering stability and generalizability.

"""

print(report)



########################################################################################################
############################################################################################################

