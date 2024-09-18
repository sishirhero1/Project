import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Load the merged data
merged_data = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7_norm.tsv", sep="\t")

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
label_encoder = LabelEncoder()
merged_data['Condition_Label'] = label_encoder.fit_transform(merged_data['Condition'])

# Drop rows with missing values
merged_data = merged_data.dropna()

# Separate features and labels
X = merged_data.drop(['Genome', 'Condition', 'Condition_Label'], axis=1)
y = merged_data['Condition_Label']

# Perform K-means clustering
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# Visualize the clustering results using the original labels
plt.figure(figsize=(10, 8))
plt.scatter(X.values[labels==0, 0], X.values[labels==0, 1], color='orange', label='Cluster 1')
plt.scatter(X.values[labels==1, 0], X.values[labels==1, 1], color='blue', label='Cluster 2')
plt.title('K-means Clustering of Merged Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/CLUST/Kmean7.png")

print(label_encoder.classes_)

