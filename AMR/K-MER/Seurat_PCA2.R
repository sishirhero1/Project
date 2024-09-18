# Load libraries
library(Seurat)

# Load your data from the tsv file (replace with your actual path)
data_path <- "D:/Projects/Abhishek_sir_project/AMR/merged_output_norm_Horizontal.tsv"
data <- read.csv(data_path, sep = "\t", header = TRUE, na.strings = "NA")

# Identify features (gene expression) and class label column
features <- colnames(data)[2:(ncol(data) - 1)]  # Exclude first and last column (assuming genome ID and condition)
class.label <- colnames(data)[ncol(data)]  # Assuming class label is in the last column

# Check data types (optional)
str(data)

# Assuming data is loaded correctly, convert to Seurat object
data <- CreateSeuratObject(data)

# Filter rows with missing values (adjust threshold as needed)
data <- data[complete.cases(data)]  # Removes rows with any missing values
data <- Filter(data, all(!is.na(data@exprs)))    # Filter based on complete data in expression matrix


# Identify highly variable features (optional)
data <- FindVariableFeatures(data, selection.method = "vst")
data <- NormalizeData(data, normalization.method = "LogNormalize", scale.factor = 10000)  # Normalize data

# Define the number of principal components (PCs) to compute
n.pcs <- 10

# Run PCA on the normalized data
reduced.data <- RunPCA(data, npcs = n.pcs)

# Explore explained variance ratio (optional)
ElbowPlot(reduced.data)

# Project cells onto the first 2 PCs for visualization
DimPlot(reduced.data, reduction = "pca", dims = 1:2, color = class.label)

# Additional analysis (optional)
# You can access the top PCs using:
# top.pcs <- reduced.data@pca@rotation[, 1:n.pcs]

# Classification using supervised methods (alternative approach)
# Consider libraries like 'glm' and 'e1071' for classification on the normalized data (data@scaled.data)
# based on class labels.
