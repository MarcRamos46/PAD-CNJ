import numpy as np

matriz = np.array([[46, 46], [20, 17], [11, 7]])
print("Matriz de inteiros:")
for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()
print("Matriz 2:")
matriz2 = np.array([['Brasil', 'Argentina'],
                    ['Uruguai', 'Paraguai'],
                    ['Mexico', 'Porto Rico']])
print(matriz2)
print(f'Dimensao: {matriz2.ndim}\nFormato:{matriz2.shape}\nTipo de dados:{matriz2.dtype}\nTamanho:{matriz2.size}')
print()

lista_nomes = ['marcelo', 'eugenia', 'rafaela', 'natalia', 'joao']
array_nomes1 = np.array(lista_nomes)
for nome in array_nomes1:
    print(nome)
print("=> Qtd de itens:", array_nomes1.size)
print('*' * 10)

array_nomes2 = np.array(['Marcelo', 'Eugenia', 'Rafaela', 'Natalia', 'Joao', 'rick gordao'])
for nome in array_nomes2:
    print(nome)
print("=> Qtd de itens:", array_nomes2.size)
