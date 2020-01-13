import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg

# 4. Вычислите LU-разложение матрицы:
#
# После этого придумайте вектор правых частей и решите полученную линейную систему трех уравнений с данной матрицей.


A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
B = np.array([1, 2, 4])
P, L, U = scipy.linalg.lu(A)

print(P)
print(L)
print(U)

print(f'det A = {np.linalg.det(A)}')
print(f'Ответ: {np.linalg.solve(A,B)}')

# det A = 432.00000000000017
# Ответ: [ 1. -0. -0.]