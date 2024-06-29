#frase = "Esse é o curso de Python - Foco em iniciantes"
#indice = frase.find("Esse")
#print(indice)

frase1 = "Hoje eu só quero que o dia termine bem"
#Método find() retorna o índice do primeiro caractere da string encontrada
inicio = frase1.find('eu')
fim = frase1.find('bem', inicio + 1)
print(frase1[inicio:fim])


