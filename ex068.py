#Quase consegui - PS: estava certo, foi questão do print que eu colocava no fim 'deu par' ou 'deu impar'
from random import randint
from time import sleep
computador = randint(0, 10)
print('-*='*10)
print('Bem Vindo ao Jogo de PAR ou ÍMPAR!')
print('-*='*10)
sleep(1)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    par_impar = ' '
    while par_impar not in 'PpIi':
        par_impar = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
    if par_impar == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-*=' * 10)
print('=-' * 10)
print(f'GAME OVER! Você venceu {cont} vez(es)')
