dic1 = {"banheiro": 3, "sala": 2, "quarto": 4}
print(dic1)

dic1["garagem"] = 1

print("Chaves do dicionário:")
for comodo in dic1:
    print(comodo)

print("Valores do dicionário:")
for comodo in dic1:
    print(dic1[comodo])#O índice de um dicionário é a chave "comodo"

print("Imprimindo o par chave-valor:")
for comodo in dic1:
    print(comodo, "=> qtd:", dic1[comodo])

print(dic1.keys())#Exibe as chaves do dicionário
print(dic1.values())#Exibe os valores do dicionário
print(dic1.items())#Exibe tuplas contendo as chaves com seus respectivos valores




