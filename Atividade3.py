def funcao(a, b):
    a = a + 1
    b[1] = a
    b[2] = b[1] * 2

def imprimir(lista):
    for item in lista:
        print(item,'',end='')
    print()

var = 10
lista = [1, 2, 3]
funcao(var, lista)

print(var)
imprimir(lista)

