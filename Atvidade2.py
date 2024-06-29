# PROGRAMA QUE CALCULA E EXIBE A QUANTIDADE DE NÚMEROS PARES NA TUPLA ABAIXO:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 8, 2, 4, 5, 4, 9, 9, 12, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 40, 44, 4, 4, 4)
cont = 0
for n in numbers:
    if (n % 2) == 0:
        print(n, end=' ')
        cont += 1
print()
print(f'Foram encontrados {cont} números pares.')




