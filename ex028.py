import random

num_sorteado = random.randrange(0, 5)
chute = int(input('\033[34mChute um número de 0 a 5: \033[m'))
if chute == num_sorteado:
    print('\033[42;30m Usuário venceu! \033[m')
else:
    print('\033[31mUsuário perdeu :(\033[m O número era: \033[33m{}\033[m'.format(num_sorteado))