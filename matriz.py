import numpy as np

A = np.array([[2,3],[4, 1]])

B = np.array([5, 6])

X = np.linalg.solve(A, B)

print(f"Las soluciones del sistema son: x = {X[0]}, y = {X[1]}")
