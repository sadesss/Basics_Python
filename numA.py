import numpy as np

# Определение матриц
A = np.array(
    [
        [400 + (159999 / 400) * 1j, -(1 / 400) * 1j, -400],
        [-(1 / 400) * 1j, 200 + (319999 / 400) * 1j, 800j],
        [-400, 800j, 500 + 800j],
    ]
)
B = np.array([[300 + 200j], [100 + 200j], [0]])
print(A)
print(B)
# Решение уравнения AX = B
X = np.linalg.solve(A, B)

print(X)
