import math

# Sample dataset: (Weight, Size, Color)
dataset = [
    (100, 5, "Red"),
    (120, 6, "Red"),
    (150, 8, "Red"),
    (200, 10, "Blue"),
    (250, 12, "Blue"),
    (300, 15, "Blue")
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_neighbors(train_data, test_point, k):
    """Find k nearest neighbors"""
    distances = [(data, euclidean_distance(test_point, (data[0], data[1]))) for data in train_data]
    distances.sort(key=lambda x: x[1])  # Sort by distance
    return [data[0] for data in distances[:k]]

def naive_bayes_prediction(neighbors):
    """Apply Naïve Bayes to determine the class"""
    class_counts = {"Red": 0, "Blue": 0}

    # Count occurrences of each class in neighbors
    for data in neighbors:
        class_counts[data[2]] += 1

    # Probability computation
    total = sum(class_counts.values())
    probabilities = {color: count / total for color, count in class_counts.items()}
    
    return max(probabilities, key=probabilities.get)

def classify_ball(weight, size, k=3):
    """Classify the color of the ball"""
    neighbors = get_neighbors(dataset, (weight, size), k)
    prediction = naive_bayes_prediction(neighbors)
    return prediction

# Example: Predict ball color for a weight of 180 and size of 9
test_weight = 180
test_size = 6
predicted_color = classify_ball(test_weight, test_size)
print(f"The predicted color of the ball is: {predicted_color}")
