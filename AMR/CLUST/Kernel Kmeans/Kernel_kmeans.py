import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_kernels

def visualize_clusters(clusters):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot and saves the plot as a PNG file.
    """
    plt.figure(figsize=(10, 8))
    for i, cluster in enumerate(clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i}')
    plt.title('Kernel K-means Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/KernelKmeans0.png")
    plt.show()

# Import the data
df = pd.read_csv('/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output_norm.tsv', sep='\t')

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
df['Condition_Label'] = df['Condition'].astype('category').cat.codes

# Drop rows with missing values
df = df.dropna()

# Prepare the data
X = df.drop(columns=['Genome', 'Condition', 'Condition_Label']).values

# Algorithm parameters
k = 2
verbose = False
max_iter = 100
epochs = 10

# Define a custom kernel (for example, radial basis function (RBF) kernel)
kernel = 'rbf'
kernel_matrix = pairwise_kernels(X, metric=kernel)

# Run K-means clustering on the kernel matrix
km = KMeans(n_clusters=k, max_iter=max_iter, random_state=42)
km.fit(kernel_matrix)

# Get cluster assignments and visualize the clustering results
labels = km.labels_
unique_labels = np.unique(labels)
clusters = [X[labels == i] for i in unique_labels]
visualize_clusters(clusters)
