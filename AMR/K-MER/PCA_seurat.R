library(dplyr)
library(ggplot2)
library(Seurat)

# Load the data without setting row names initially
data_path <- "D:/Projects/Abhishek_sir_project/AMR/merged_output_norm_Horizontal.tsv"
data <- read.csv(data_path, sep = "\t", header = TRUE, na.strings = "NA",row.names = 1)

# Check for duplicate row names in the first column
if (any(duplicated(data[, 1]))) {
  warning("Duplicate row names found in the data. Creating unique row names.")
  data[, 1] <- make.unique(as.character(data[, 1]))
}

# Transpose the data (genes as rows, cells as columns)
data <- t(data)
names(data) <- data[1,]
data <- data[-1,]



# Extract metadata before modifying data
metadata <- data.frame(Condition = data$Condition)
rownames(metadata) <- rownames(data)

# Remove the metadata column from the data
data <- data[, -which(colnames(data) == "Condition")]

# Ensure all data is numeric and handle non-numeric values
data[] <- lapply(data, function(x) as.numeric(as.character(x)))

# Check for NA values in the data
if (any(is.na(data))) {
  cat("Columns with NA values:\n")
  print(colnames(data)[colSums(is.na(data)) > 0])
  stop("The data contains NA values. Please ensure the data is clean before proceeding.")
}

# Print summary statistics to ensure data is clean
cat("\nSummary of the data:\n")
print(summary(data))

# Create a Seurat object without metadata first
seurat_object <- CreateSeuratObject(counts = data)

# Add Metadata using AddMetaData function
seurat_object <- AddMetaData(object = seurat_object, metadata = metadata)

# Normalize the data
seurat_object <- NormalizeData(seurat_object)

# Find variable features
seurat_object <- FindVariableFeatures(seurat_object)

# Scale the data
seurat_object <- ScaleData(seurat_object)

# Run PCA
seurat_object <- RunPCA(seurat_object, features = VariableFeatures(object = seurat_object))

# Print PCA results
print(seurat_object[["pca"]], dims = 1:2, nfeatures = 5)

# Plot PCA
DimPlot(seurat_object, reduction = "pca", group.by = "Condition") +
  labs(title = "PCA of Merged Data")

# Save the plot
ggsave("D:/Projects/Abhishek_sir_project/AMR/PCA_Seurat_Norm_Horizontal.png")
