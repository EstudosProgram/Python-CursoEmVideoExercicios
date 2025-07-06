#tbm não consegui
opcao = 'S'
quant = 0
s = 0
while opcao != 'N':
    n = int(input('Digite um número inteiro: '))
    s += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    opcao = str(input('Deseja continuar [S/N]: ')).upper()

media = s / quant
print('Você digitou {} números e a média é {:.2f}'.format(quant, media))
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))
