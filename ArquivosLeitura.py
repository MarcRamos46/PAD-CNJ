'''
arq = open("ficha1.txt", "r")
for linha in arq:
    print('Linha lida: ', linha)
arq.close()

print("-------------------------")
'''
arq = open("ficha1.txt", "r")
for linha in arq:
    lista = linha.split("-")
    nome = lista[0]
    idade = int(lista[1])
    print(nome, "tem", idade, "anos de idade.")
arq.close()
