import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist
from pyclustering.cluster.kmedoids import kmedoids

def visualize_clusters(clusters, medoids):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot and saves the plot as a PNG file.
    """
    plt.figure(figsize=(10, 8))
    for i, cluster in enumerate(clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i}')
    plt.scatter(medoids[:, 0], medoids[:, 1], c='r', marker='o', s=100, label='Medoids')
    plt.title('K-medoids Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/Kmedoids7.png")
    plt.show()

def kmedoids_clustering(points, k=2, max_iter=100):
    """
    Clusters the list of points into `k` clusters using K-medoids clustering algorithm.
    """
    points = np.array(points)
    n_points, n_features = points.shape
    assert n_points >= k, "Number of data points can't be less than k"

    # Initialize medoids randomly from data points
    initial_medoids = np.random.choice(n_points, k, replace=False)
    kmedoids_instance = kmedoids(points, initial_medoids, data_type='points')

    # Run K-medoids algorithm
    kmedoids_instance.process()

    # Get clusters and medoids
    clusters = [[] for _ in range(k)]
    medoids = kmedoids_instance.get_medoids()
    labels = kmedoids_instance.get_clusters()

    for i, cluster in enumerate(labels):
        clusters[i] = points[cluster]

    return clusters, points[medoids]

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

# Run K-medoids clustering algorithm
clusters, medoids = kmedoids_clustering(points=points, k=k, max_iter=max_iter)

# Visualize the clustering results
visualize_clusters(clusters, medoids)
