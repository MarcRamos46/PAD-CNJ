#LENDO DO TECLADO
print("Olá!!")
nome = input("Digite seu nome: ")
print("Bem-vindo(a)! " + nome)
idade = int(input("Qual sua idade? ")) #A função input() sempre recebe um STRING
aposentadoria = int(input("Com qual idade você espera se aposentar? "))

anos_faltantes = aposentadoria - idade
print(f'{nome}, faltam {anos_faltantes} anos para você se aposentar.')





