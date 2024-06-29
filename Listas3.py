#INSERINDO ITEM NUMA LISTA: insert() e append()

lista_compras = ['banana', 'leite', 'arroz', 'frango', 'leite', 'iogurte']

print('Lista original: ',end=' ')
for item in lista_compras:
    print(item,end=' ')
print()

lista_compras.insert(0,'manteiga')#Insert: insere um elemento na posição determinada
print(lista_compras)

lista_compras.insert(0,'cuscuz')
print(lista_compras)

lista_compras.append('papel_higiênico')#Append: insere um elemento ao final da lista
for item in lista_compras:
    print(item,end=' ')
