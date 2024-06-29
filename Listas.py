lista_compras = ['maçãs', 'leite', 'arroz', 'frango', 'iogurte', 'feijão', 'banana', 'melancia', 'ovos']
tamanho = len(lista_compras)

print('Minha lista de compras tem o tamanho', tamanho)
print('O primeiro elemento da lista é',lista_compras[0])
#print('O último elemento da lista é',lista_compras[5])
print('Último elemento da lista:',lista_compras[len(lista_compras) - 1])
print()
#for i in range(len(lista_compras)):
#    print('O elemento', i, 'da minha lista de compras é', lista_compras[i])
i = 0
while i < len(lista_compras):
    print('O elemento', i, 'da minha lista é', lista_compras[i])
    i += 1




