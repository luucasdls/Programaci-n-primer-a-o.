import numpy as np

A = np.array([
    [1, 3],
    [2, 4]
])

B = np.array([
    [5, 7],
    [6, 8]
])

resultado = 2 * A + B.T

print(resultado)