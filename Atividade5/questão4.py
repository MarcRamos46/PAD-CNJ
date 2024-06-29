import csv

arq = open("exemplo.csv", "r")
csv_reader = csv.reader(arq, delimiter=';')
#next(csv_reader)
for linha in csv_reader:
    print(linha[2].replace(',','.'))
    next(csv_reader)#faz o leitor ir para a linha seguinte
arq.close()
