def altera_lista(lista):
    lista[0] = 0
    lista[1] = 1
    lista[2] = "macaco"

def imprime_lista(lista):
    for num in lista:
        print(num,end=' ')
    print()

minha_lista = [3, 4, 5]
print("Lista Original:")
imprime_lista(minha_lista)

altera_lista(minha_lista)
print("Lista com alterações:")
imprime_lista(minha_lista)

