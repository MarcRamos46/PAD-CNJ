'''
estoque_frutas ={"laranja": 30, "abacaxi": 15, "maçã": 38, "melão":10}
print("Dicionário estoque_frutas original:")
print(estoque_frutas)

estoque_ordenado = {}
chaves_ordenadas = sorted(estoque_frutas,key = estoque_frutas.get)

for chave in chaves_ordenadas:
    estoque_ordenado[chave] = estoque_frutas[chave]
print("Dicionário estoque_frutas ordenado conforme seus valores:")
print(estoque_ordenado)
'''
nomes = {20: "Maria Eugênia", 10: "João Marcelo", 8: "Marcelo", 13: "Rafaela", 11: "Natália"}
print("=> Dicionário inicial:")
print(nomes)

print("=> Dicionário ordenado:")
nomes1 = dict(sorted(nomes.items()))
print(nomes1)

nomes_ordenado = {}
chaves_ordenadas = sorted(nomes, key = nomes.get)
print("=> Chaves Ordenadas: ", chaves_ordenadas)
print()

for chave in chaves_ordenadas:
    nomes_ordenado[chave] = nomes[chave]
print("=> Dicionário ordenado conforme os valores(aqui são strings):")
print(nomes_ordenado)





