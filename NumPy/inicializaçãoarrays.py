import numpy as np

#Utilizando os metodos:

vetor_zeros = np.zeros(4, dtype=np.intc)
matriz_zeros = np.zeros((3,2))
matriz_uns = np.ones((5,5), dtype=np.intc)
matriz_de_6 = np.full((4,4), 6, dtype=np.intc)

print(vetor_zeros)
print(matriz_zeros)
print(matriz_uns)
print(matriz_de_6)

print()

vetor1 = np.arange(0, 15)
print('Vetor1:', vetor1)

vetor2 = np.linspace(20, 40, 6)
print(f'Vetor2: {vetor2}')



