condição = True
while condição:
    opção = input('Digite qualquer palavra para ser impressa. Digite SAIR para encerrar: ')
    if opção.lower() == 'sair':
        condição = False
    else:
        print("AINDA NO LAÇO!!")
print("=> Fim do Programa")