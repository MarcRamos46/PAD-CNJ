import csv  #Biblioteca para ler arquivos csv

arquivo = open('Familia.csv', 'r')
#Cria uma lista com o método reader() da biblioteca csv
#Elimina a necessidade de usar o split(';') dentro do laço for
leitor_csv = csv.reader(arquivo, delimiter=';')
next(leitor_csv)#Pula a primeira linha

total_idades = 0
total_pesos = 0
for linha in leitor_csv:
    total_idades += int(linha[1])
    total_pesos += float(linha[2].replace(',','.'))
arquivo.close()

print('Somatório das idades: ', total_idades, 'anos.')
print('Somatório dos pesos:  ', total_pesos, 'Kg.')


