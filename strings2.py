arq = open('FamiliaRamos.txt', 'r')
for linha in arq:
    lista = linha.split(';')
    nome = lista[0]
    idade = int(lista[1])
    print(nome, 'tem', idade, 'anos.')
arq.close()


