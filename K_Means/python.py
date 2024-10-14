import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#generate blobs
dataset = make_blobs(n_samples=200, centers=4, n_features=2, cluster_std=1.6, random_state=50)

#convert to Arrays
points = dataset[0]

#Create Kmeans Objects
kmeans = KMeans(n_clusters=4)

#fit the data object
kmeans.fit(points)


#plt point in scatterplot
plt.scatter(dataset[0][:,0], dataset[0][:,1])