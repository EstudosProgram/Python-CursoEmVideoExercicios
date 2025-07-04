cidade = input('Digite o nome da sua cidade: ')
dividido = cidade.split()
print('Começa com o nome SANTO, true ou false ? {}'.format('Santo' in dividido[0]))
#Outra forma
#print('Começa com o nome SANTO, true ou false ? {}'.format(cidade[:5] == 'Santo'))