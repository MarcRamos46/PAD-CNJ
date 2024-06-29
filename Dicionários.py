# dic = {} => Dicionário vazio

v1 = 10
v2 = v1 * 2
v3 = v2 * 3

dic2 = {"chave1": v1 , "chave2": v2, "chave3": v3}

print(f'Valor: {dic2["chave1"]}')
print(f'Valor: {dic2["chave2"]}')
print(f'Valor: {dic2["chave3"]}')

dic2["chave4"] = 120

print(dic2)

dic2.pop("chave1")

print(dic2)

dic2.popitem()#Retira o ÚLTIMO ELEMENTO DO DICIONÁRIO
print(dic2)

del dic2["chave2"]
print(dic2)

dic2.popitem()
print(dic2)







