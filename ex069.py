#esta quase lá - PS: errei na estrutura de onde colocar os ifs
cont_h = 0
cont_pes = 0
cont_mulheres = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('Digite o seu sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        cont_pes += 1
    elif sexo in 'Mm':
        cont_h += 1
    elif sexo in 'Ff' and idade < 20:
        cont_mulheres += 1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Possuem {cont_pes} pessoa(s) maior de 18 anos')
print(f'São {cont_h} homem(ns) cadastrados')
print(f'São {cont_mulheres} mulher(es) menor(es) de 20 anos')
