import numpy as np

dados = np.genfromtxt("questao3.csv", delimiter=";", skip_header= 0, dtype=np.intc)
resultado1 = dados[1].sum()
resultado2 = dados.sum(0)[2]
print(resultado1, resultado2)

