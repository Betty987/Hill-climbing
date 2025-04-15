import numpy as np
import matplotlib.pyplot as plt

# Define a generic quadratic function: f(x) = ax^2 + bx + c
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Hill climbing algorithm to find a root
def hill_climbing(start, step_size, max_iterations, tolerance, a, b, c):
    current_x = start
    path = [current_x]
    
    for _ in range(max_iterations):
        current_value = quadratic(current_x, a, b, c)
        
        # Stop if close to a root (function value near zero)
        if abs(current_value) < tolerance:
            break
            
        # Evaluate left and right steps
        left_x = current_x - step_size
        right_x = current_x + step_size
        left_value = quadratic(left_x, a, b, c)
        right_value = quadratic(right_x, a, b, c)
        
        # Move to the point with smaller absolute function value
        if abs(left_value) < abs(current_value):
            current_x = left_x
        elif abs(right_value) < abs(current_value):
            current_x = right_x
        else:
            # Reduce step size if no improvement
            step_size *= 0.5
            
        path.append(current_x)
    
    return current_x, path

# Parameters
a, b, c = 3, -5, 2  # Coefficients 
start_points = [-5, 5]  # Start points 
step_size = 0.1
max_iterations = 1000
tolerance = 1e-6

# Find roots
roots = []
paths = []
for start in start_points:
    root, path = hill_climbing(start, step_size, max_iterations, tolerance, a, b, c)
    roots.append(root)
    paths.append(path)

# Plotting
x = np.linspace(-5, 1, 400) 
y = quadratic(x, a, b, c)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label=f'f(x) = {a}x² + {b}x + {c}')  # Plot quadratic
plt.axhline(0, color='black', linestyle='-', alpha=0.3)
plt.axvline(0, color='black', linestyle='-', alpha=0.3)

# Plot paths with valid format strings
for i, (root, path) in enumerate(zip(roots, paths)):
    path_y = [quadratic(x, a, b, c) for x in path]
    color = 'r-' if i == 0 else 'g-'  # Red for first path, green for second
    plt.plot(path, path_y, color, marker='o', label=f'Path from x={start_points[i]:.1f}', alpha=0.6)
    plt.plot(root, quadratic(root, a, b, c), marker='*', color=color[0], markersize=15, label=f'Root ≈ {root:.2f}')

plt.title(f'Hill Climbing to Find Roots of {a}x² + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.savefig('hill_climbing_quadratic_generic.png')