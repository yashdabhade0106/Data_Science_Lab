# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:13:14 2024

@author: yashd
"""

import pandas as pd 
import matplotlib.pylab as plt 
#Now impoprt file from data set and create dataframe
Univ1 = pd.read_excel("C:/DataScience/7-Clustering/University_Clustering.xlsx")
a=Univ1.describe()
#We have one cloumn 'State' which really not usefull we will drop it
Univ=Univ1.drop(['State'],axis=1)
#We know there is scale difference among the columns,
#which we have to remove
#either by using normalization  or standardization 
#whenever ther is mixed data apply normalization 
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#Now apply the normalization function to Univ dataframe 
# for all rows and clomnsn from 1 until end 
# sinces 0 th column has University name hences skipped 
df_norm=norm_func(Univ.iloc[:,1:])
#you can check the df_norm dataframe which is scaled 
#between values 0 to 1
#you can apply describe function to new data frame 
b=df_norm.describe()
#before yo u apply clustering, you need to plot dendrogram first
# Now to create dendrogram,we need to measure the distance
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or aglomerative clustering
#ref the help for linkage 
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hierarchical clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
#ref helpl of dendrogram
#sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#dendrogram()
#applying agglomerative clustering choosing 5 as clustering from dendrogram
#whatever has been displayed in dendrogram is not clusteering 
#it is just showing numbver of ppossible clusters
from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters = 3,linkage='complete',metric='euclidean').fit(df_norm)
#apply labels to the clusters 
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#Assign this series to Univ dataframe as column and name the cloumn as clust
Univ['clust']=cluster_labels
#we want to relocate the column 7 to 0th position 
Univ1 = Univ.iloc[:,[7,1,2,3,4,5,6]]
#Now check the Univ1 dataframe 
Univ1.iloc[:,2:].groupby(Univ.clust).mean()
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses 
#highest gradutes ratio 
Univ1.to_csv("University.csv",encoding='utf-8')











