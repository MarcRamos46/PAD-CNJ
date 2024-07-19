import numpy as np
import pandas as pd

dict = {"Marcelo": np.random.randint(0,101), "Natalia": np.random.randint(0,101), "Rafaela": np.random.randint(0,101), "Eugênia": np.random.randint(0,101), "João Marcelo": np.random.randint(0,101)}
print(dict)

print()

s = pd.Series(dict)
print(s)

print()

print(f'A maior nota é {s.max()}')
print(f'A menor nota é {s.min()}')
print(f'A média das notas é {s.mean()}')

