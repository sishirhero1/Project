import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA
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

# Step 5: Perform Kernel PCA
kpca = KernelPCA(n_components=2, kernel='rbf')  # You can choose different kernels
X_kpca = kpca.fit_transform(X_scaled)

# Step 6: Plot Kernel PCA results
plt.figure(figsize=(8, 6))
plt.scatter(X_kpca[y == "Resistant", 0], X_kpca[y == "Resistant", 1], c='blue', alpha=0.8, label='Resistant')
plt.scatter(X_kpca[y == "Susceptible", 0], X_kpca[y == "Susceptible", 1], c='orange', alpha=0.8, label='Susceptible')
plt.xlabel('Kernel Component 1')
plt.ylabel('Kernel Component 2')
plt.title('Kernel PCA Plot')
plt.legend(loc='upper right')  # Add legend
plt.savefig("PCA_kernel7.png")

