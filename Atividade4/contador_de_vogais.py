def ContarVogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    #Iterando sobre cada letra do texto
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


meu_texto = ('My my, hey hey\n'
             'Rock and roll is here to stay\n'
             'It\'s better to burn out than to fade away\n'
             'My my, hey hey\n'
             '\n'
             'Out of the blue and into the black\n'
             'They give you this, but you pay for that\n'
             'An\'once you\'re gone you can never come back\n'
             'When you\'re out of the blue and into the black\n'
             '\n'
             'The king is gone, but he\'s not forgotten\n'
             'This is the story of a Johnny Rotten\n'
             'It\'s better to burn out than it is to rust\n'
             'The king is gone, but he\'s not forgotten\n'
             '\n'
             'Hey hey, my my\n'
             'Rock and roll can never die\n'
             'There\'s more to the picture than meets the eye\n'
             'Hey hey, my my')

qtdvogais = ContarVogais(meu_texto)
print(f'Quantidade de vogais do texto é {qtdvogais}')
print()
inicio = meu_texto.find("They")
fim = meu_texto.find("When", inicio + 1)
trecho = meu_texto[inicio:fim]
print(f'Trecho:\n{trecho}')


