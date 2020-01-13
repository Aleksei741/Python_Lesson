import numpy as np

# 3. Сколько решений имеет линейная система:
#
#
# Если ноль – то измените вектор правой части так, чтобы система стала совместной, и решите ее.

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
BT = np.array([[3], [2], [1]])
B = np.array([3, 2, 1])

print(f'Ранг A {np.linalg.matrix_rank(A, 0.0001)}')
C = np.concatenate((A,BT), axis=1)
print(f'Ранг C {np.linalg.matrix_rank(C, 0.0001)}')

print(f'Ответ: {np.linalg.solve(A,B)}')
#Ответ: [-9.66666667 15.33333333 -6.        ]