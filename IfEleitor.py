idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Caso você já tenha o Título de Eleitor, já poderá votar!!")
    if (idade >= 18 and idade <= 70):
        print("Se você é ALFABETIZADO, seu voto é OBRIGATÓRIO!")
    else:
        print("Seu voto é FACULTATIVO!")
else:
    print("VOCÊ NÃO PODE VOTAR!!")
