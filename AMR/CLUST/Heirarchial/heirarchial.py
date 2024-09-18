import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

def visualize_dendrogram(Z):
    """
    Visualizes the hierarchical clustering as a dendrogram.
    """
    plt.figure(figsize=(10, 8))
    dendrogram(Z, leaf_rotation=90, leaf_font_size=10)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/HierarchicalClusteringDendrogram7.png")
    plt.show()

def visualize_clusters(points, labels):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot.
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.title('Hierarchical Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/HierarchicalClustering7.png")
    plt.show()

# Import the data
df = pd.read_csv('/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7_norm.tsv', sep='\t')

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
df['Condition_Label'] = df['Condition'].astype('category').cat.codes

# Drop rows with missing values
df = df.dropna()

# Prepare the data
points = df.drop(columns=['Genome', 'Condition', 'Condition_Label']).values

# Perform hierarchical clustering
Z = linkage(points, method='ward')

# Visualize the dendrogram
visualize_dendrogram(Z)

# Determine clusters
max_clusters = 2
labels = fcluster(Z, max_clusters, criterion='maxclust')

# Visualize the clustering results
visualize_clusters(points, labels)

