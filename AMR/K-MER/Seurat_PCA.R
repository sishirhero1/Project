library(dplyr)
library(ggplot2)
library(Seurat)

# Data path
data_path <- "D:/Projects/Abhishek_sir_project/AMR/merged_output_norm_Horizontal.tsv"

head(data)

# Exclude 'genome id' and 'Conditions' columns for PCA
data_pca <- data %>%
  select(-Genome, -Condition)

# Perform PCA
pca_result <- prcomp(data_pca, center = TRUE, scale. = TRUE)

# Summary of PCA
summary(pca_result)

# Extract the PCA scores
pca_scores <- as.data.frame(pca_result$x)

# Add the 'Conditions' column back to the PCA scores for plotting
pca_scores$Conditions <- data$Conditions

# Plot the PCA results
ggplot(pca_scores, aes(x = PC1, y = PC2, color = Conditions)) +
  geom_point(size = 2) +
  labs(title = "PCA of Genome Data", x = "Principal Component 1", y = "Principal Component 2") +
  theme_minimal()