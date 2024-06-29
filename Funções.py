def saudacao(nome, periodo = 'n'):
    if (periodo == 'm'):
        print('Bom dia,', nome + '.')
    elif (periodo == 't'):
        print('Boa tarde,', nome + '.')
    elif (periodo == 'n'):
        print('Boa noite,', nome + '.')
    else:
        print('PERÍODO INVÁLIDO!')
    print('Este é o curso de Python.')

saudacao('Marcelo', 'm')





