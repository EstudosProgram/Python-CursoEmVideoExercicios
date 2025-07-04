soma_idade = 0
maior_idade_h = 0
nome_velho = ''
soma_mulheres = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        nome_velho = nome
        maior_idade_h = idade
    elif sexo in 'Mm' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_velho = nome
    elif sexo in 'Ff' and idade < 20:
        soma_mulheres += 1


media_idade = soma_idade / 4
print('A média da soma de idades do grupo é {} anos'.format(media_idade))
print('O {} é o homen mais velho com {} anos'.format(nome_velho, maior_idade_h))
print('São {} mulherer(es) menor(es) de 20'.format(soma_mulheres))

