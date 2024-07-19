import numpy as np
import pandas as pd

notas = np.random.randint(0, 101, 5)
s = pd.Series(notas, index=['Rafaela Maria', 'Taylor Swift', 'Sabrina Carpenter', 'OLivia Rodrigo', 'Sofia Lacet'])

print('NOTAS:')
print(notas)
print()
print('NOTAS POR ALUNO:')
print(s)
print()

maxnota = s.max()
minnota = s.min()
media = s.mean()

print(f'A maior nota é {maxnota}')
print(f'A menor nota é {minnota}')
print(f'A média das notas é {media}')

