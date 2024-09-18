import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import skfuzzy as fuzz

def convert_to_2d_array(points):
    """
    Converts `points` to a 2-D numpy array.
    """
    points = np.array(points)
    if len(points.shape) == 1:
        points = np.expand_dims(points, -1)
    return points

def visualize_clusters(points, u, plot_save_path):
    """
    Visualizes the first 2 dimensions of the data as a 2-D scatter plot and saves the plot as a PNG file.
    """
    plt.figure(figsize=(10, 8))
    cluster_labels = np.argmax(u, axis=0)
    for i in range(u.shape[0]):
        cluster_points = points[cluster_labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')
    plt.title('Fuzzy C-means Clustering of Merged Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.savefig(plot_save_path)
    plt.show()

# Parameters that can be varied
input_file_path = '/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output_norm.tsv'
columns_to_exclude = ['Genome', 'Condition', 'Condition_Label']
plot_save_path = "/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/FuzzyCMeans0.png"
c = 2  # Number of clusters
m = 2  # Fuzziness parameter
error = 0.005  # Convergence criterion
max_iter = 100  # Maximum number of iterations

# Import the data
df = pd.read_csv(input_file_path, sep='\t')

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
df['Condition_Label'] = df['Condition'].astype('category').cat.codes

# Drop rows with missing values
df = df.dropna()

# Prepare the data
points = df.drop(columns=columns_to_exclude).values

# Perform Fuzzy C-means clustering
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    points.T, c, m, error=error, maxiter=max_iter, init=None, seed=42)

# Visualize the clustering results
visualize_clusters(points, u, plot_save_path)
