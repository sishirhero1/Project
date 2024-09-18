import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def visualize_clusters(points, labels, centroids):
    """
    Visualizes the clusters and centroids.
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='r', s=100, label='Centroids')
    plt.title('Elkan\'s K-means Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/ElkansKmeans7.png")
    plt.show()

# Import the data
df = pd.read_csv('/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7_norm.tsv', sep='\t')

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
df['Condition_Label'] = df['Condition'].astype('category').cat.codes

# Drop rows with missing values
df = df.dropna()

# Prepare the data
points = df.drop(columns=['Genome', 'Condition', 'Condition_Label']).values

# Algorithm parameters
k = 2
max_iter = 300  # Adjust as needed
tol = 1e-4  # Tolerance for convergence

# Run Elkan's K-means clustering algorithm
kmeans = KMeans(n_clusters=k, init='k-means++', algorithm='elkan', max_iter=max_iter, tol=tol, random_state=0)
kmeans.fit(points)

# Retrieve clustering results
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualize the clustering results
visualize_clusters(points, labels, centroids)
