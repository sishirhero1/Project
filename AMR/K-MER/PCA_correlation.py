import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Step 1: Read data
data = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7.tsv", sep="\t")

# Step 2: Separate features and target
X = data.drop(columns=["Condition"])
y = data["Condition"]

# Step 3: Encode target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define colors for plotting
colors = np.where(y == "Resistant", 'blue', 'orange')

# Step 4: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 6: Plot PCA results
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=colors, alpha=0.8)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Plot')
plt.savefig("PCA7_correlation.png")
plt.show()
