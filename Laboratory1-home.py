import numpy as np
import matplotlib.pyplot as plt

# Function to compute linear regression coefficients (slope and intercept)
def linear_regression(x, y):
    n = len(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    
    numerator = np.sum((x - m_x) * (y - m_y))
    denominator = np.sum((x - m_x) ** 2)
    
    slope = numerator / denominator
    intercept = m_y - slope * m_x
    
    return slope, intercept

# Function to perform manual input and linear regression
def perform_regression():
    n = int(input("How many data points will you input? "))
    heights = []
    weights = []
    
    # Input data points
    for i in range(n):
        height = float(input(f"Enter the height of student {i+1} (in cm): "))
        weight = float(input(f"Enter the weight of student {i+1} (in kg): "))
        heights.append(height)
        weights.append(weight)
        
    x = np.array(heights)
    y = np.array(weights)
    
    # Perform linear regression
    slope, intercept = linear_regression(x, y)
 
    print(f"\nThe linear regression equation is: y = {slope:.2f}x + {intercept:.2f}")
    regression_line = slope * x + intercept
    
    # Plot the data points and the regression line
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, regression_line, color='red', label=f'Linear Regression (y = {slope:.2f}x + {intercept:.2f})')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.title('Linear Regression: Height vs Weight')
    plt.legend()
    plt.grid(True)
    plt.show()

perform_regression()