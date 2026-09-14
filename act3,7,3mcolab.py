import numpy as np
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

At = A.T
Aat = A + At
print("Matriz 'A' sin transposición.")
print(A)

print("Matriz 'A' con transposición.")
print(At)

print("Matriz (A+At)")
print(Aat)

rango = np.linalg.matrix_rank(Aat)
print("El rango de (A+At) es:", rango)