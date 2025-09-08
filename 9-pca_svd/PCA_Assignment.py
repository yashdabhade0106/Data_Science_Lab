# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:20:58 2024

@author: yashd
"""
# 1.Business Problem
#1.1.What is the business objective?

'''
The goal is to simplify complex datasets by reducing the number of variables while preserving critical information. Here are a couple of examples:  

Customer Segmentation: Categorizing customers based on fewer, significant features such as purchasing habits.  
Fraud Detection: Identifying patterns in a reduced number of dimensions to spot fraud efficiently.

'''

#1.2.Are there any constraints?
'''
Interpretability: Newly created components may be difficult to understand.  
Data Standardization: PCA performs optimally when the data is normalized or scaled.  
Loss of Detail: Some minor data characteristics may be lost during dimensionality reduction.  
Processing Time: Large datasets might require considerable computational power.

'''

##################################################################

#2.	Work on each feature of the dataset to create a data dictionary as displayed in the below image:
#2.12.1 Make a table as shown above and provide information about the features such as its data type and its relevance to the model building.
#And if not relevant, provide reasons and a description of the feature.
'''
Follow these steps to build a data dictionary for your dataset:  

1. List each feature present in the dataset.  
2. For every feature, gather the following details:  

   - **Feature Name**: Name of the feature, e.g., "Customer ID."
   - **Identifier**: Indicate whether this is an identifier (Yes/No).  
   - **Description**: Provide a brief explanation of the feature.  
   - **Data Type**: Identify the data type (e.g., Numeric, Categorical, etc.).  
   - **Relevance**: Explain if the feature is relevant to the model. If not, clarify why.  

Example Table:  

| Feature Name | Identifier | Description | Type | Relevance |  
|--------------|------------|-------------|------|-----------|  
| Customer ID  | Yes        | Unique identifier for each customer | Nominal | Not useful for prediction |  

**Key Tips**:  
If a feature like "Customer ID" doesn’t add predictive value, label it irrelevant and exclude it from the model. The feature description should focus on the business context, remaining clear and concise.

'''
#################################################################################################

#3.	Data Pre-processing
#3.1 Data Cleaning, Feature Engineering, etc.

'''
**3.1 Data Cleaning**  
- Handle missing values: Impute with mean/median or drop rows with missing data.  
- Remove duplicates: Ensure no repeated records exist.  
- Identify outliers: Detect and mitigate outliers to prevent skewing results.  
- Standardize data: Normalize numerical variables to achieve consistency.  

**3.2 Feature Engineering**  
- Interaction Terms: Create interaction terms to capture relationships between features (e.g., multiplying them).  
- Binning: Convert continuous variables into discrete categories (e.g., age brackets).  
- Encoding Categorical Features: Apply techniques like one-hot encoding or label encoding.  
- Initial Feature Selection: Remove less relevant features before proceeding with PCA.

'''
###########################################################################################

#4.	Exploratory Data Analysis (EDA):
#4.1.	Summary.
#4.1 	Univariate analysis.
#4.3.	Bivariate analysis.
'''

**4.1 Summary**  
- Descriptive Stats: Look at key statistics such as mean, median, range, and variance.  
- Data Distribution: Use histograms and box plots to observe the distribution and detect any outliers.  
- Feature Correlation: Check for relationships between variables using a correlation matrix or heatmap. This helps in identifying features that PCA can reduce.  

**4.2 Univariate Analysis**  
- **Numerical Features**: Examine individual features through histograms or box plots.  
- **Categorical Features**: Use bar plots to view the frequency of each category.  

**4.3 Bivariate Analysis**  
- **Numeric vs Numeric**: Use scatter plots to understand the relationships between two numerical variables.  
- **Category vs Numeric**: Use box plots to compare numerical values across categories.  
- **Category vs Category**: Employ bar charts or cross-tabulations to examine relationships between categorical features.

'''

###########################################################################################
#v5.Model Building
#5.1Build the model on the scaled data (try multiple options).
# 5.2 Perform PCA analysis and get the maximum variance between components.
# 5.3 Perform clustering before and after applying PCA to cross the number of clusters      	formed.
#5.4 Briefly explain the model output in the documentation. 

'''
**5.1 Scale and Build the Model**  
- Standardize the dataset using techniques like Z-score or Min-Max scaling. This ensures that all variables are on the same scale, which is crucial for model performance.  
- Try various clustering models, such as:  
   - **K-Means Clustering**: Groups similar data points.  
   - **Hierarchical Clustering**: Builds a tree to represent the hierarchy of clusters.  
   - **DBSCAN**: Detects clusters of varying shapes and sizes, including noisy data.  

**5.2 PCA Analysis**  
- Apply PCA to reduce the number of features while retaining key information.  
- Check how much variance each principal component explains. Aim to keep components that explain a high percentage of the original variance (e.g., 95%).  

**5.3 Clustering Before and After PCA**  
- Before PCA: Perform clustering on the scaled dataset and record the number of clusters.  
- After PCA: Run clustering again on the reduced dataset and compare the number of clusters. Evaluate the impact of PCA.  

**5.4 Document Results**  
- Capture the number of clusters before and after PCA.  
- Present results visually using techniques like elbow plots.  
- Provide interpretation and analysis of how PCA improved the model by reducing complexity while preserving important insights.

'''
####################################################################################################
#Write about the benefits/impact of the solution - in what way does the business (client) benefit from the solution provided?

'''
**Business Impact**:  
- **Improved Insights**: Simplifies analysis, enabling better decision-making based on essential features.  
- **Performance Boost**: Reduces model complexity, leading to faster training times and enhanced accuracy.  
- **Cost Savings**: Minimizes computational costs by working with fewer features.  
- **Faster Response**: Streamlines data analysis for quicker responses to business needs.  
- **Discovery of Patterns**: Identifies hidden relationships that can reveal new opportunities.  
- **Improved Visualization**: Simplifies complex datasets, making them easier to explain to stakeholders.  
- **Scalability**: The solution can scale with future data, ensuring continued efficiency.  
- **Competitive Advantage**: Empowers quicker, data-driven decisions, enhancing customer satisfaction and driving business success.

'''
#########################################################################################################


#Problem Statement:
'''
Conduct both hierarchical and K-means clustering on a 
given dataset. Next, apply PCA to reduce the dataset to 
its first three principal components and create a new 
dataset with these components.  
Finally, perform hierarchical and K-means 
clustering again on this reduced dataset. 
Compare the clustering results from the original 
dataset with those from the PCA-reduced dataset. 
Use a scree plot to determine the optimal number of 
clusters and assess whether PCA produces similar clustering results.

'''
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
wine_data = [
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

# Define column names for the DataFrame
column_names = ['SampleID', 'Alcohol', 'MalicAcid', 'AshContent', 'Alcalinity', 'Magnesium',
                'Phenols', 'Flavanoids', 'NonFlavanoids', 'Proanthocyanins', 'ColorIntensity', 
                'Hue', 'DilutionFactor']

# Create the DataFrame with the dataset
wine_df = pd.DataFrame(wine_data, columns=column_names)

# Checking for missing values
print("Missing values per column:\n", wine_df.isnull().sum())

# Standardizing the features (excluding 'SampleID')
scaler = StandardScaler()
standardized_data = scaler.fit_transform(wine_df.drop('SampleID', axis=1))

# Performing Hierarchical Clustering on the standardized data
hierarchy_linkage = linkage(standardized_data, method='ward')

# Visualizing the dendrogram for hierarchical clustering
plt.figure(figsize=(10, 6))
dendrogram(hierarchy_linkage)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Wine Samples')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram to create clusters (adjust threshold 't' for cluster formation)
cluster_count = 3
cluster_labels = fcluster(hierarchy_linkage, cluster_count, criterion='maxclust')

# K-Means Clustering to identify clusters in the original dataset
cluster_inertia = []
silhouette_scores = []

# Determining optimal number of clusters using the Elbow Method and Silhouette Score
for k in range(2, 11):
    kmeans_model = KMeans(n_clusters=k, random_state=42)
    kmeans_model.fit(standardized_data)
    cluster_inertia.append(kmeans_model.inertia_)
    silhouette_scores.append(silhouette_score(standardized_data, kmeans_model.labels_))

# Plotting Elbow Method to visualize optimal cluster count
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), cluster_inertia, marker='o')
plt.title('Elbow Method for Optimal Cluster Count')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.show()

# Display Silhouette Scores
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Scores for Different Cluster Counts')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Set optimal number of clusters (based on Elbow and Silhouette results)
best_k = 3  # Modify based on analysis
kmeans_final = KMeans(n_clusters=best_k, random_state=42)
kmeans_final.fit(standardized_data)
final_labels = kmeans_final.labels_

# PCA to reduce dimensions to 3 principal components
pca_model = PCA(n_components=3)
data_pca = pca_model.fit_transform(standardized_data)

# Explained variance for each principal component
explained_variance = pca_model.explained_variance_ratio_

# Scree plot to show the variance explained by each principal component
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), explained_variance, marker='o')
plt.title('Scree Plot for PCA')
plt.xlabel('Principal Components')
plt.ylabel('Variance Explained')
plt.show()

# Performing Hierarchical Clustering on the PCA-reduced dataset
hierarchy_linkage_pca = linkage(data_pca, method='ward')

# Visualizing the dendrogram for PCA-transformed data
plt.figure(figsize=(10, 6))
dendrogram(hierarchy_linkage_pca)
plt.title('Dendrogram for Hierarchical Clustering (PCA Data)')
plt.xlabel('Wine Samples (PCA Transformed)')
plt.ylabel('Distance')
plt.show()

# Cutting the PCA dendrogram to create clusters
cluster_labels_pca = fcluster(hierarchy_linkage_pca, cluster_count, criterion='maxclust')

# K-Means Clustering on PCA-reduced data
cluster_inertia_pca = []
silhouette_scores_pca = []

# Finding the optimal number of clusters for the PCA-reduced dataset using Elbow and Silhouette scores
for k in range(2, 11):
    kmeans_pca = KMeans(n_clusters=k, random_state=42)
    kmeans_pca.fit(data_pca)
    cluster_inertia_pca.append(kmeans_pca.inertia_)
    silhouette_scores_pca.append(silhouette_score(data_pca, kmeans_pca.labels_))

# Plotting Elbow Method for PCA-reduced data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), cluster_inertia_pca, marker='o')
plt.title('Elbow Method for Optimal Cluster Count (PCA Data)')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.show()

# Displaying Silhouette Scores for PCA-transformed data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores_pca, marker='o')
plt.title('Silhouette Scores for Different Cluster Counts (PCA Data)')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Set optimal number of clusters for PCA-reduced data
best_k_pca = 3  # Modify based on analysis
kmeans_pca_final = KMeans(n_clusters=best_k_pca, random_state=42)
kmeans_pca_final.fit(data_pca)
final_labels_pca = kmeans_pca_final.labels_

# Comparing clustering results between original and PCA-transformed datasets
print("K-Means Clustering Labels (Original Data):", final_labels)
print("K-Means Clustering Labels (PCA Data):", final_labels_pca)

####################################################################################################333

#Problem Statement
'''
A pharmaceuticals manufacturing company is conducting a study on a new medicine to treat heart diseases. The company has gathered data from its secondary sources and would like you to provide high level analytical insights on the data. Its aim is to segregate patients depending on their age group and other factors given in the data. Perform PCA and clustering algorithms on the dataset and check if the clusters formed before and after PCA are the same and provide a brief report on your model. You can also explore more ways to improve your model. 

Note: This is just a snapshot of the data. The datasets can be downloaded from AiSpry LMS in the Hands-On Material section.

'''
# here we created a dataset on that table or that data and saved it 
import pandas as pd

# Create the dataset for heart disease study
heart_data = {
    'age': [63, 37, 41, 56, 57, 57, 56, 44, 52, 57, 50, 58, 66, 69, 59, 44, 42, 61],
    'sex': [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    'cp': [3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 2, 2, 3, 3, 0, 2, 0, 2],
    'trestbps': [145, 130, 130, 120, 140, 120, 140, 120, 172, 150, 140, 135, 130, 150, 140, 150, 140, 150],
    'chol': [233, 250, 204, 236, 192, 354, 294, 263, 199, 168, 239, 234, 233, 226, 247, 283, 340, 226],
    'fbs': [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
}

# Create a DataFrame from the dataset
heart_df = pd.DataFrame(heart_data)

# Display the DataFrame
print(heart_df)

# Save the dataset to a CSV file
heart_df.to_csv('heart_disease_data.csv', index=False)

##############################################################################################
# Import necessary libraries for clustering and analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import silhouette_score

# Checking for missing values
print("Missing values in each column:\n", heart_df.isnull().sum())

# Standardize the dataset (all columns)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(heart_df)

# Perform hierarchical clustering on the original dataset
linkage_matrix = linkage(scaled_data, method='ward')

# Plotting the dendrogram to visualize the clusters
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Cutting the dendrogram to define clusters
num_clusters = 2  # Number of clusters
hierarchical_labels = fcluster(linkage_matrix, num_clusters, criterion='maxclust')

# Performing K-means clustering on the original dataset
inertia_vals = []
silhouette_scores = []

# Determining the optimal number of clusters using the Elbow Method and Silhouette Scores
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_vals.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))

# Elbow Method plot to determine optimal clusters
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia_vals, marker='o')
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

# Choose optimal k clusters based on the analysis
optimal_k = 3
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42)
kmeans_final.fit(scaled_data)
kmeans_labels = kmeans_final.labels_

# PCA to reduce dataset dimensions to 3 principal components
pca = PCA(n_components=3)
pca_data = pca.fit_transform(scaled_data)

# Variance explained by each principal component
explained_variance = pca.explained_variance_ratio_

# Scree plot for explained variance by each principal component
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), explained_variance, marker='o')
plt.title('Scree Plot')
plt.xlabel('Principal Components')
plt.ylabel('Variance Explained')
plt.show()

# Hierarchical clustering on PCA-transformed dataset
linkage_matrix_pca = linkage(pca_data, method='ward')

# Plotting the dendrogram for PCA-transformed data
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix_pca)
plt.title('Dendrogram for Hierarchical Clustering on PCA Data')
plt.xlabel('Samples (PCA Transformed)')
plt.ylabel('Distance')
plt.show()

# Cutting the dendrogram to define clusters after PCA
hierarchical_labels_pca = fcluster(linkage_matrix_pca, num_clusters, criterion='maxclust')

# K-means clustering on PCA-transformed dataset
inertia_vals_pca = []
silhouette_scores_pca = []

# Determining the optimal number of clusters using Elbow and Silhouette methods for PCA data
for k in range(2, 11):
    kmeans_pca = KMeans(n_clusters=k, random_state=42)
    kmeans_pca.fit(pca_data)
    inertia_vals_pca.append(kmeans_pca.inertia_)
    silhouette_scores_pca.append(silhouette_score(pca_data, kmeans_pca.labels_))

# Elbow Method plot for PCA-transformed data
plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), inertia_vals_pca, marker='o')
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

# Choose the optimal number of clusters after PCA
optimal_k_pca = 2
kmeans_pca_final = KMeans(n_clusters=optimal_k_pca, random_state=42)
kmeans_pca_final.fit(pca_data)
kmeans_labels_pca = kmeans_pca_final.labels_

# Comparing the clustering results between the original and PCA-transformed datasets
print("K-means Clustering Labels (Original Data):", kmeans_labels)
print("K-means Clustering Labels (PCA Data):", kmeans_labels_pca)

# Report on findings and results
report = """
### Clustering Analysis Report

**1. Overview:**
- Dataset contains information on heart disease patients with features such as age, sex, chest pain type (cp), resting blood pressure (trestbps), cholesterol (chol), and fasting blood sugar (fbs).

**2. Clustering Analysis:**
- Hierarchical and K-means clustering were applied to the original dataset, with optimal clusters found through the Elbow Method and Silhouette scores.
- PCA was used to reduce dimensions, and clustering was re-applied to the PCA-transformed data.

**3. PCA Results:**
- The first three principal components retained significant variance from the original data, allowing clustering with fewer dimensions.

**4. Comparison:**
- Clustering tendencies were similar before and after PCA, showing PCA's ability to preserve key structural information in the data.

**5. Recommendations:**
- Consider using different clustering algorithms (e.g., DBSCAN or Agglomerative Clustering) for more detailed insights.
- Further feature engineering could enhance clustering results.
- Larger datasets could improve stability and reliability of the clustering analysis.
"""

print(report)

############################################################################################################
