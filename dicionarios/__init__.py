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

print("Total de itens:")
total_frutas = 0
for fruta in estoque_frutas:
    total_frutas += estoque_frutas[fruta]
print(f'Frutas em estoque = {total_frutas} unidades.')

