import numpy as np

#Trabalhando com o método random.rand():
#Gera números no intervalo [0,1) - distribuição uniforme
print("Matriz aleatória numpy.random.rand():")
matriz_rand = np.random.rand(2, 2)
print(matriz_rand)

print("Vetor aleatório numpy.random.rand():")
vetor_rand = np.random.rand(4)
print(vetor_rand)

#Gerando uma matriz aleatoria de inteiros:
print("Matriz aleatória de inteiros:")
matriz = np.random.randint(0, 20, (4,3))
print(matriz)

#Gerando uma matriz aleatória a partir de uma distribuição de Poisson:
print("Matriz aleatória Poisson:")
poisson = np.random.poisson(lam=4.0, size=(3,3))#lam é o parâmetro lambda de uma distribuição de Poisson
print(poisson)


