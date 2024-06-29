import numpy as np

#Metodo sum()

numeros = np.ones((4, 3), dtype=int) * 20
print(numeros)
soma = numeros.sum()
print("Soma:",soma)

dados = np.ones((3,2), dtype=int) * 10
soma_colunas = dados.sum(0)#retorna um array com a soma dos valores das colunas
soma_linhas = dados.sum(1)
print(dados)
print("Vetor soma_colunas:",soma_colunas)
print("Vetor soma_linhas:",soma_linhas)
print("---------------------------------")

#Metodo diff() => gera um array com as diferenças dos elementos(segundo - primeiro, terceiro - segundo, quarto - terceiro...)
dados_poisson = np.random.poisson(lam=3, size=(4,3))
print(dados_poisson)
print(np.diff(dados_poisson))
print("--------------------------------------------")

#Metodo cumsum() => somas cumulativas
numeros = np.ones((3, 3), dtype=int) * 2
print(numeros)
print(f'Somas cumulativas:\n{np.cumsum(numeros)}')
#Metodo cumprod() => produtos cumulativos
print(f'Produtos cumulativos: \n{np.cumprod(numeros)}')

print("----------------------------------")
#Metodo ediff1d() => retorna um array de 1 dimensão formado pelas diferenças dos elementos
vetorx = np.array([2, 8, 3, 11, -7])
vetory = np.array([[2, 4, 5], [0, 0, 1], [2, 2, 3]])
print(vetory)
print(np.ediff1d(vetory))
#print(vetorx)
#print(np.ediff1d(vetorx))













