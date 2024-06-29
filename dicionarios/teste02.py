estoque_frutas ={"laranja": 30, "abacaxi": 15, "maçã": 38, "melão":10}

print("Estoque inicial de frutas:")
for fruta in estoque_frutas:
    print("Fruta:",fruta, "=> qtd:", estoque_frutas[fruta])

estoque_frutas["pera"] = 42
estoque_frutas["manga"] = 60
print()

print("Novo estoque:")
for fruta in estoque_frutas:
    print("Fruta:",fruta, "=> qtd:", estoque_frutas[fruta])
print()

#Retirando maçã com o comando del:
print("Retirei maçã da lista:")
del estoque_frutas["maçã"]
print(estoque_frutas.items())

#Retirando abacaxi com o comando dicionario.pop("chave"):
print("Retirei abacaxi da lista:")
estoque_frutas.pop("abacaxi")
print(estoque_frutas.items())

print()
#Retirando o último elemento da lista
print("Retirei o último elemento:")
estoque_frutas.popitem()
print(estoque_frutas)




