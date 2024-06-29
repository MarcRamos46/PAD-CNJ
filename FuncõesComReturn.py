import matematica
numero = int(input("Digite um número ou -1 para sair: "))
while (numero != -1):
    resultado = matematica.fatorial(numero)
    print('Fatorial de', numero, 'é', resultado)
    numero = int(input("Digite um número ou -1 para sair: "))
print()
print('Fim do Programa')



