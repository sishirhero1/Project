import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

def convert_to_2d_array(points):
    """
    Converts `points` to a 2-D numpy array.
    """
    points = np.array(points)
    if len(points.shape) == 1:
        points = np.expand_dims(points, -1)
    return points

def visualize_clusters(clusters, labels):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot.
    """
    plt.figure(figsize=(10, 8))
    for i, cluster in enumerate(clusters):
        points = convert_to_2d_array(cluster)
        if points.shape[1] < 2:
            points = np.hstack([points, np.zeros_like(points)])
        plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i}')
    plt.title('Bisecting K-means Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/BisectingKmeans7_100epochs_100maxiter.png")
    plt.show()

def SSE(points):
    """
    Calculates the sum of squared errors for the given list of data points.
    """
    points = convert_to_2d_array(points)
    centroid = np.mean(points, 0)
    errors = np.linalg.norm(points - centroid, ord=2, axis=1)
    return np.sum(errors)

def kmeans(points, k=2, epochs=10, max_iter=100, verbose=False):
    """
    Clusters the list of points into `k` clusters using k-means clustering algorithm.
    """
    points = convert_to_2d_array(points)
    assert len(points) >= k, "Number of data points can't be less than k"
    best_sse = np.inf
    for ep in range(epochs):
        # Randomly initialize k centroids
        np.random.shuffle(points)
        centroids = points[0:k, :]
        last_sse = np.inf
        for it in range(max_iter):
            # Cluster assignment
            clusters = [None] * k
            for p in points:
                index = np.argmin(np.linalg.norm(centroids - p, 2, 1))
                if clusters[index] is None:
                    clusters[index] = np.expand_dims(p, 0)
                else:
                    clusters[index] = np.vstack((clusters[index], p))
            # Centroid update
            centroids = [np.mean(c, 0) for c in clusters]
            # SSE calculation
            sse = np.sum([SSE(c) for c in clusters])
            gain = last_sse - sse
            if verbose:
                print((f'Epoch: {ep:3d}, Iter: {it:4d}, '
                       f'SSE: {sse:12.4f}, Gain: {gain:12.4f}'))
            # Check for improvement
            if sse < best_sse:
                best_clusters, best_sse = clusters, sse
            # Epoch termination condition
            if np.isclose(gain, 0, atol=0.00001):
                break
            last_sse = sse
    return best_clusters

def bisecting_kmeans(points, k=2, epochs=10, max_iter=100, verbose=False):
    """
    Clusters the list of points into `k` clusters using bisecting k-means clustering algorithm.
    Internally, it uses the standard k-means with k=2 in each iteration.
    """
    points = convert_to_2d_array(points)
    clusters = [points]
    while len(clusters) < k:
        max_sse_i = np.argmax([SSE(c) for c in clusters])
        cluster = clusters.pop(max_sse_i)
        two_clusters = kmeans(
            cluster, k=2, epochs=epochs, max_iter=max_iter, verbose=verbose)
        clusters.extend(two_clusters)
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
verbose = False
max_iter = 500
epochs = 100

# Run bisecting k-means algorithm
clusters = bisecting_kmeans(points=points, k=k, verbose=verbose, max_iter=max_iter, epochs=epochs)

# Visualize the clustering results
visualize_clusters(clusters, df['Condition_Label'])
