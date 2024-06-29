import numpy as np

array = np.array([[4, 5, 6], [7, 8, 9]])

print("Matriz:")
for linha in array:
    for coluna in linha:
        print(coluna, end=' ')
    print()

print("Item na linha 0, coluna 1: ",  array[0][1])
print("Item na linha 1, coluna 2: ", array[1][2])

