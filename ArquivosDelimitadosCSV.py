file = open('Familia.csv', 'r')
file.readline()#descartando a primeira linha/cabeçalho

idades = 0
pesos = 0
quantidade = 0
for line in file:#A cada iteração(linha por linha do arquivo) é criada um lista usando o método split(';') tendo o ; como separador.
    formed_list = line.split(';')
    idades = idades + int(formed_list[1])
    pesos = pesos + float(formed_list[2].replace(',','.'))
    quantidade += 1
file.close()

print('Família Ramos:')
print(f'Idade média é {idades/quantidade} anos.')
print(f'Peso médio é {pesos/quantidade:.2f} Kg.')

