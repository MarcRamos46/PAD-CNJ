#A função write só aceita strings
file = open('FamiliaRamos.txt', 'a')
file.write('Natália Maria')
file.write(';')
file.write('17')
file.write('\n')
file.write('Rafaela Maria')
file.write(';')
file.write('11')
file.write('\n')
file.close()

