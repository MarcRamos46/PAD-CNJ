import numpy as np

meusdados = np.genfromtxt("exercicio06.csv", delimiter=',', skip_header=0, dtype=np.intc)
print('Array:')
print(meusdados)
print('Shape do array:', meusdados.shape)

matriz = meusdados.reshape((-1,10))
print('Matriz:')
print(matriz)
print('Shape da matriz:', matriz.shape)
print('Total dos valores da cada linha:', matriz.sum(1))
print('Total dos valores da matriz:', matriz.sum())




