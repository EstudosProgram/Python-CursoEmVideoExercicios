texto = str(input('Digite o seu sexo: ')).strip().upper()[0]
while texto not in 'MF':
    texto = str(input('Você digitou errado, é M ou F: ')).strip().upper()[0]
if texto == 'M':
    print('Você é masculino')
else:
    print('Você é feminino')