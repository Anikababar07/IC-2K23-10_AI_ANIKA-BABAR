import numpy as np
from sklearn.decomposition import PCA

# Create sample dataset
data = np.array([
    [2.5, 2.4, 1.2],
    [0.5, 0.7, 0.3],
    [2.2, 2.9, 1.5],
    [1.9, 2.2, 1.1],
    [3.1, 3.0, 1.8],
    [2.3, 2.7, 1.4]
])

# Create PCA model to reduce data to 2 dimensions
pca = PCA(n_components=2)

# Transform the data
reduced_data = pca.fit_transform(data)

print("Original Data Shape:", data.shape)
print("Reduced Data Shape:", reduced_data.shape)

print("\nData after PCA:")
print(reduced_data)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)