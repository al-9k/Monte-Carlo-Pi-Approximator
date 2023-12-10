import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = np.random.rand(2)  # RANDOM POINT GENERATION
        distance = np.sqrt(x**2 + y**2)  # CALCULATE DISTANCE FROM ORIGIN, SEE CONDITIONS BELOW

        if distance <= 1:
            inside_circle += 1

    pi_approximation = 4 * inside_circle / num_samples
    return pi_approximation

# INSERT DESIRED SAMPLES HERE
num_samples = 10000

# APPROXIMATE BY MONTE CARLO SIM
pi_approx = monte_carlo_pi(num_samples)

# PLOT
x_inside, y_inside, x_outside, y_outside = [], [], [], []

for _ in range(num_samples):
    x, y = np.random.rand(2)

    if x**2 + y**2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=5, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=5, label='Outside Circle')
plt.title(f'Monte Carlo Approximation of Pi: {pi_approx}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
