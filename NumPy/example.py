import numpy as np

dados = np.genfromtxt("arquivoteste.csv", delimiter=',', skip_header=1, usecols=(5, 6), dtype=(np.intc, np.intc))
print(dados)
print(dados.shape)
print(f'Totais(Populacao,Area): {dados.sum(0)}')


