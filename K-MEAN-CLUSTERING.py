import random
import math

# Sample dataset (Height, Weight, Shoe Size, Gender)
dataset = [
    (140, 35, 5, "Boy"), (130, 30, 4, "Girl"), (145, 40, 6, "Boy"),
    (135, 32, 5, "Girl"), (150, 45, 7, "Boy"), (128, 28, 4, "Girl"),
    (155, 50, 8, "Boy"), (132, 31, 4, "Girl"), (148, 42, 6, "Boy"),
    (138, 34, 5, "Girl")
]

# Initialize centroids randomly (pick two points from dataset)
k = 2
centroids = random.sample([data[:3] for data in dataset], k)

# K-Means Clustering
for _ in range(5):  # Run for a fixed number of iterations
    clusters = {i: [] for i in range(k)}
    
    # Assign each point to the nearest centroid
    for data in dataset:
        distances = [math.sqrt(sum((data[i] - centroid[i])**2 for i in range(3))) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(data)
    
    # Recalculate centroids
    for i in range(k):
        if clusters[i]:
            centroids[i] = tuple(sum(feature) / len(feature) for feature in zip(*[data[:3] for data in clusters[i]]))

# Assign cluster labels based on majority gender in each cluster
cluster_labels = {}
for i in range(k):
    gender_count = {"Boy": 0, "Girl": 0}
    for data in clusters[i]:
        gender_count[data[3]] += 1
    cluster_labels[i] = max(gender_count, key=gender_count.get)

# Naïve Bayes Classification
# Replace input() with predefined values due to non-interactive environment
test_child = (140, 38, 5)  # Example test case

# Determine the cluster
distances = [math.sqrt((test_child[0] - centroid[0])**2 + (test_child[1] - centroid[1])**2 + (test_child[2] - centroid[2])**2) for centroid in centroids]
cluster_index = distances.index(min(distances))
classified_label = cluster_labels[cluster_index]

print(f"The child with characteristics {test_child} is classified as: {classified_label}")
