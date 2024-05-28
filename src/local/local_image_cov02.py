import matplotlib.pyplot as plt
import numpy as np
import math

points = np.array([
    [0, 0],
    [0, 6],
    [3, 6],
    [3, 5],
    [1, 5],
    [1, 4],
    [3, 4],
    [3, 3],
    [1, 3],
    [1, 0],
    [0, 0],
])

plt.plot(points[:, 0], points[:, 1])

cov = np.array([
    [math.cos(math.pi / 2), -math.sin(math.pi / 2)],
    [math.sin(math.pi / 2), math.cos(math.pi / 2)]
])
new_points = np.dot(points, cov.T)
plt.plot(new_points[:, 0], new_points[:, 1])

plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.show()
