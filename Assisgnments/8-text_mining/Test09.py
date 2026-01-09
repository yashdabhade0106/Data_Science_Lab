# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:14:42 2024

@author: yashd
"""
"""
1. You are given a dataset with two numerical features Height and Weight. 
Your goal is to cluster these people into 3 groups using K-Means clustering. 
After clustering, you will visualize the clusters and their centroids. 
 Load the dataset (or generate random data for practice). 
 Apply K-Means clustering with k = 3. 
 Visualize the clusters and centroids. 
 Experiment with different values of k and see how the clustering changes.

"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/DataScience/TESTS/HeightWeight.csv")

features = ['Height', 'Weight']
X = df[features].values

X_normalized = (X - X.mean(axis=0)) / X.std(axis=0)

kmeans = KMeans(n_clusters=3, n_init=10, max_iter=300, random_state=42)
clusters = kmeans.fit_predict(X_normalized)

plt.figure(figsize=(10, 6))
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=clusters, cmap='viridis')

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='red', label='Centroids')

plt.xlabel('Normalized Height')
plt.ylabel('Normalized Weight')
plt.title('K-Means Clustering with 3 Groups')
plt.legend()
plt.show()

def plot_elbow_curve(X, range_k):
    inertias = []
    for k in range_k:
        kmeans = KMeans(n_clusters=k, n_init=10, max_iter=300, random_state=42)
        kmeans.fit(X_normalized)
        inertias.append(kmeans.inertia_)
    
    plt.figure(figsize=(12, 6))
    plt.plot(range_k, inertias, marker='o')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Curve')
    plt.show()

plot_elbow_curve(X_normalized, range(1, 11))  

#################################################
"""
2. You have a dataset of  customers with features Age, Annual Income, and 
Spending Score. You need to apply hierarchical clustering to segment these 
customers. Plot a dendrogram to decide the optimal number of clusters and 
compare it with K-Means clustering results. 
Steps: 
 Load the dataset. 
 Apply hierarchical clustering. 
 Plot a dendrogram and choose the number of clusters. 
 Apply K-Means clustering with the same number of clusters. 
 Compare the results.
 
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/DataScience/TESTS/HeightWeight.csv")

features = ['Height', 'Weight']
X = df[features].values

X_normalized = (X - X.mean(axis=0)) / X.std(axis=0)

kmeans = KMeans(n_clusters=3, n_init=10, max_iter=300, random_state=42)
clusters = kmeans.fit_predict(X_normalized)

plt.figure(figsize=(10, 6))
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=clusters, cmap='viridis')

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='red', label='Centroids')

plt.xlabel('Normalized Height')
plt.ylabel('Normalized Weight')
plt.title('K-Means Clustering with 3 Groups')
plt.legend()
plt.show()


#################################################
"""
3. Evaluate clustering performance using the Silhouette Score and Elbow 
Method on the Wine dataset. Determine the optimal number of clusters. 
Note : Load the wine dataset from sklearn

"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn import metrics

newsgroups = fetch_20newsgroups(subset='all')
documents = newsgroups.data
true_labels = newsgroups.target

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

num_clusters = 20  
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

clusters = kmeans.labels_

silhouette_score = metrics.silhouette_score(X, clusters, metric='euclidean')
print(f'Silhouette Score: {silhouette_score:.3f}')

terms = vectorizer.get_feature_names_out()
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    print(f"Cluster {i}:")
    for ind in order_centroids[i, :10]:  
        print(f' {terms[ind]}')
    print()

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X.toarray())

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=clusters, cmap='viridis', s=10)
plt.colorbar(scatter)
plt.title('K-Means Clustering of 20 Newsgroups Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()


#################################################
"""
4. You have a 2D dataset with some clusters and random noise. Your task is to 
apply DBSCAN clustering to identify the core samples, outliers, and clusters. 
Compare the DBSCAN results with K-Means on the same dataset. 
 Generate a dataset with clusters and noise. 
 Apply DBSCAN clustering and tune parameters (eps, min_samples). 
 Visualize the clusters and outliers. 
 Apply K-Means clustering and compare.
"""


#################################################
"""
5. Cluster text documents based on their TF-IDF vectors using K-Means 
clustering. Use the 20 Newsgroups dataset. 
Note : Load the 20 Newsgroup dataset(fetch_20newsgroups) from sklearn5. Cluster text documents based on their TF-IDF vectors using K-Means 
clustering. Use the 20 Newsgroups dataset. 
Note : Load the 20 Newsgroup dataset(fetch_20newsgroups) from sklearn

"""


#################################################

