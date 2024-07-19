import numpy as np

valores = np.random.randint(0, 6, (5,5))
print(valores)
resultado = np.where((valores > 5) | (valores == 3), valores, 0)
print(resultado)

