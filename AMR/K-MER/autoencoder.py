import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import Input, Dense

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

# Step 5: Define autoencoder architecture
input_dim = X_scaled.shape[1]
encoding_dim = 2

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = Model(input_layer, decoded)

# Compile the model
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Step 6: Train the autoencoder
autoencoder.fit(X_scaled, X_scaled, epochs=50, batch_size=32, shuffle=True, validation_split=0.2)

# Step 7: Use encoder part to transform data
encoder = Model(input_layer, encoded)
X_encoded = encoder.predict(X_scaled)

# Step 8: Plot the encoded data
plt.figure(figsize=(8, 6))
plt.scatter(X_encoded[:, 0], X_encoded[:, 1], c=y_encoded, cmap='viridis', alpha=0.8)
plt.xlabel('Autoencoder Component 1')
plt.ylabel('Autoencoder Component 2')
plt.title('Autoencoder Plot')
plt.colorbar(label='Class')
plt.savefig("autoencoder.png")

