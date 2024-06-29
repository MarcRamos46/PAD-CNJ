estoque_frutas ={"laranja": 30, "abacaxi": 15, "maçã": 38, "melão":10}
print("=> Dicionário inicial:")
print(estoque_frutas)
print("=> Ordenação do dicionário pelas chaves(lista):")
print(sorted(estoque_frutas))

print("= > Mostrando chave e valor ordenados pela chave(lista de tuplas):")
print(sorted(estoque_frutas.items()))

#A funcão dict converte a lista de tuplas retornada pelo método sorted em um dicionário, o qual
#é atribuído à variável dic_frutas_ord.
dic_frutas_ord = dict(sorted(estoque_frutas.items()))
print("Dicionário ordenado:")
print(dic_frutas_ord)


