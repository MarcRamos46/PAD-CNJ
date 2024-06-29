import numpy as np

vetor = np.array([1.7, 2, 3, 4])
matriz = np.array([[4, 5, 6], [7, 8, 9], [0, 0, 0]])

print("Vetor:")
for item in vetor:
    print(item, end=' ')
print()
print(vetor.ndim, vetor.shape, vetor.dtype, vetor.size)

print("Matriz:")
for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()
print(matriz.ndim, matriz.shape, matriz.dtype, matriz.size)
