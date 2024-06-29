import csv
arq = open("matriz.csv", "r")
leitor_csv = csv.reader(arq, delimiter=',')

i = 0
for linha in leitor_csv:
    print(linha[i])
    i+=1
arq.close()

