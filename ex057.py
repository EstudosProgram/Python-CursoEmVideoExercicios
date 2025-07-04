texto = 'T'
while texto != 'M' and texto!= 'F':
    print('Você digitou errado, é M ou F')
    texto = str(input('Digite o seu sexo: ')).upper()
if texto == 'M':
    print('Você é masculino')
else:
    print('Você é feminino')