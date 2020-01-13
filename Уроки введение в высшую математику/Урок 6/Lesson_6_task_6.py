import numpy as np

# 6. Найдите одно из псевдорешений вырожденной системы:
#
# Попробуйте также отыскать и нормальное псевдорешение.

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])

Q, R = np.linalg.qr(A)

print(A)
print(Q)
print(R)

R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]

X1 = np.linalg.solve(R1, B1)
print(X1)
X=np.append(X1, 0)
print(X) #[1.50000000e+00 3.92767275e-15 0.00000000e+00]
print(np.linalg.norm(X)) #1.499999999999996
print(np.linalg.norm(np.dot(A,X) - B)) #1.224744871391589

X = np.linalg.lstsq(A,B, rcond=-1)[0]
print(f'Ответ: {X}') #Ответ: [ 1.25  0.5  -0.25]

print(np.linalg.norm(X)) #1.3693063937629126
print(np.linalg.norm(np.dot(A,X) - B)) #1.2247448713915892