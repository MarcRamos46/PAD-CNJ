import numpy as np

dados = np.genfromtxt("EBT.csv", delimiter=';', skip_header=1, usecols=(0, 1), dtype=(np.intc, np.intc))
print(dados.shape)
print(f'Somas: {dados.sum(0)}')

