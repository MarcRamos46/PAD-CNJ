# TUPLAS SÃO IMUTÁVEIS
import sys
tupla = ('maçã', 'leite', 'farinha', 'rapadura', 'café')
lista = ['maçã', 'leite', 'farinha', 'rapadura', 'café']

print('Tamanho da TUPLA na memória: ', sys.getsizeof(tupla)) #getsizeof informa a quantidade de bytes que o objeto(lista/tupla) possui
print('Tamanho da LISTA na memória: ', sys.getsizeof(lista))
