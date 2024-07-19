import pandas as pd
import numpy as np

nd = np.random.randn(10)
print(nd)

serie = pd.Series(nd)
print(serie[serie<0])
