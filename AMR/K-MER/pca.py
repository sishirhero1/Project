import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the merged data
merged_data = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/merged_output_norm_Horizontal.tsv", sep="\t")

# Encode the labels 'Resistant' and 'Susceptible' with numeric values
label_encoder = LabelEncoder()
merged_data['Label'] = label_encoder.fit_transform(merged_data['Condition'])

# Separate features and labels
X = merged_data.drop(['Genome', 'Condition', 'Label'], axis=1)
y = merged_data['Label']

if X.isnull().values.any():
    print("NaN values found in the dataset. Handling NaNs...")
    X = X.fillna(X.mean()) 
# Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot PCA results
plt.figure(figsize=(10, 8))
plt.scatter(X_pca[y==0, 0], X_pca[y==0, 1], color='orange', label='Susceptible')
plt.scatter(X_pca[y==1, 0], X_pca[y==1, 1], color='blue', label='Resistant')
plt.title('PCA of Merged Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)

# Save the plot as PNG
plt.savefig("/mnt/d/Projects/Abhishek_sir_project/AMR/PCA_Horizontals_norm.png")

# Show the plot
plt.show()
