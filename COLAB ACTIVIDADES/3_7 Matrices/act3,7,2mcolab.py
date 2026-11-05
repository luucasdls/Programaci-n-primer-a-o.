import numpy as np

A = np.array([
    [1, 0, 1],
    [4, -1, 4],
    [5, 6, 7]
])

A_inversa = np.linalg.inv(A)

traza = np.trace(A_inversa)

print("Matriz inversa:")
print(A_inversa)

print("Traza:", traza)