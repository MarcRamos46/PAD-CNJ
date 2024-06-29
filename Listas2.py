lista_compras = ['banana', 'leite', 'arroz', 'frango', 'leite', 'iogurte']
'''
sublista = lista_compras[1:4]
print('SUBLISTA:')
for item in sublista:
    print(item)

lista_compras[len(lista_compras) - 1] = 'refrigerante'
print('=> OUTRA FORMA:')
for item in lista_compras[2:9]:
    print(item)
'''
print('=> Lista original:', end=' ')
for item in lista_compras:
    print(item,end=' ')
print()

del lista_compras[1]# Exclui o elemente de índice 1
lista_compras.remove('arroz') # Remove o primeiro elemento arroz da lista
lista_compras.pop() # Remove o último elemento da lista

print('=> Lista sem o elemento de índice 1 da lista anterior:',end=' ')
for item in lista_compras:
    print(item,end=' ')
print()

lista_compras.sort()

print('=> Lista ordenada:',end=' ')
for item in lista_compras:
    print(item,end=' ')
print()

lista_compras.sort(reverse=True)

print('=> Lista ao contrário:',end=' ')
for item in lista_compras:
    print(item,end=' ')


