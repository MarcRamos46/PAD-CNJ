import numpy as np

vetor = np.linspace(2, 32, 12, dtype=np.intc)
#print(vetor)

vetor_alterado = vetor.reshape((-1, 2))#O valor -1 faz com que o numpy deduza o valor adequado para coluna ou linha
vetor[0] = -1
vetor[len(vetor) - 1] = -1
print(vetor)
print(vetor_alterado)


