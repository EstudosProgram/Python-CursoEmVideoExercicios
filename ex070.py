#Cheguei bem próximo - PS: errei tbm a estrutura e corriji o problema do nome
print('-'*30)
frase = 'LOJA DA MILENA'
print(frase.center(30))
print('-'*30)
total = totmil = cont = menor_prod = 0
nome_barato = ''
while True:
    nome_prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor_prod:
        menor_prod = preco
        nome_barato = nome_prod
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print(f'O total foi R${total:.2f}')
print(f'São {totmil} produtos acima de mil reais')
print(f'O produto mais barato é o/a {nome_barato} que custa R${menor_prod}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))