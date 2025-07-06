#tbm não consegui
opcao = ''
count = 1
s = 0
while opcao != 'N':
    n = int(input('Digite um número inteiro: '))
    s += n
    count += 1
    media = s / count
    opcao = str(input('Deseja continuar [S/N]: ')).upper()
print('A média é {:.2f}'.format(media))
