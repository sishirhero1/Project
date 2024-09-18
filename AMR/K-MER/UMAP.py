import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import umap.umap_ as umap
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

# Step 4: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Perform UMAP
umap_model = umap.UMAP(n_components=2)
X_umap = umap_model.fit_transform(X_scaled)

# Step 6: Plot UMAP results
plt.figure(figsize=(8, 6))
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=y_encoded, cmap='viridis', alpha=0.8)
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.title('UMAP Plot')
plt.colorbar(label='Class')
plt.savefig("UMAP7.png")

