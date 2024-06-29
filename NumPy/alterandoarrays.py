import numpy as np

matriz = np.ones((3,3), dtype=int)#retorna uma matriz 3 x 3 de uns.
#print(matriz)
matriz[0][0] = 33
#print(matriz)
matriz += 14
print(matriz)
matriz[2] *= 2
print(matriz)



