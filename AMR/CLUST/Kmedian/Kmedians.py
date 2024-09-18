import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist

def visualize_clusters(clusters):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot and saves the plot as a PNG file.
    """
    plt.figure(figsize=(10, 8))
    for i, cluster in enumerate(clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i}')
    plt.title('K-medians Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/Kmedians7.png")
    plt.show()

def kmedians(points, k=2, max_iter=100):
    """
    Clusters the list of points into `k` clusters using K-medians clustering algorithm.
    """
    points = np.array(points)
    n_points, n_features = points.shape
    assert n_points >= k, "Number of data points can't be less than k"

    # Initialize centroids randomly from data points
    np.random.shuffle(points)
    centroids = points[:k, :]

    for _ in range(max_iter):
        # Assign points to closest centroids based on L1 distance (median)
        distances = cdist(points, centroids, metric='cityblock')  # L1 distance
        labels = np.argmin(distances, axis=1)

        # Update centroids to the median of assigned points
        new_centroids = np.zeros_like(centroids)
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = np.median(cluster_points, axis=0)

        # Check for convergence
        if np.array_equal(centroids, new_centroids):
            break

        centroids = new_centroids

    # Group points into clusters based on final centroids
    clusters = [points[labels == i] for i in range(k)]
    return clusters

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
max_iter = 100

# Run K-medians clustering algorithm
clusters = kmedians(points=points, k=k, max_iter=max_iter)

# Visualize the clustering results
visualize_clusters(clusters)
