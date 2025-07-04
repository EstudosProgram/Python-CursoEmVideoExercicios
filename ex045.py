import random
from time import sleep

lista = ['pedra','papel','tesoura']
computador = random.choice(lista)
jogador = str(input('Escolha pedra, papel ou tesoura: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
if computador == jogador:
    print('-' * 6)
    print('Empate')
    print('-' * 6)
elif computador == 'pedra' and jogador == 'tesoura' or computador == 'tesoura' and jogador == 'papel' or computador == 'papel' and jogador == 'pedra':
    print('O computador ganhou! O resultado foi {} x {}'.format(computador, jogador))
else:
    print('Você ganhou! O resultado foi {} x {}'.format(jogador, computador))