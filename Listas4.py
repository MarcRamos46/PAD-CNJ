#Criando uma lista com dados do usuário:
lista_compras = []

item = input("Digite um item ou sair: ").lower()
while item != 'sair':
    lista_compras.append(item)
    item = input("Digite um item ou sair: ").lower()

lista_compras.sort()

print('=> A lista é:')
for item in lista_compras:
    print(item)

print(type(lista_compras))
