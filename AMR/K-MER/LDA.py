import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Step 1: Read data
data = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output.tsv", sep="\t")

# Step 2: Separate features and target
X = data.drop(columns=["Condition"])
y = data["Condition"]

# Step 3: Encode target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Step 4: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Perform LDA with one component
lda = LDA(n_components=1)
X_lda = lda.fit_transform(X_scaled, y)

# Step 6: Plot LDA results
plt.figure(figsize=(8, 6))
plt.scatter(X_lda, np.zeros_like(X_lda), c=y_encoded, cmap='viridis', alpha=0.8)
plt.xlabel('LDA Component 1')
plt.title('LDA Plot')
plt.colorbar(label='Class')
plt.savefig("LDA.png")
