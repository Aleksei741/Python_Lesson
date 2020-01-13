import numpy as np
import matplotlib.pyplot as plt

#1. Решите линейную систему:

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
X = np.linalg.solve(A, B)
print(f'Ответ: Х1 = {X[0]}, X2 = {X[1]}, X3 = {X[2]}')

# Ответ: Х1 = -9.200000000000001, X2 = 0.9000000000000006, X3 = 6.466666666666666