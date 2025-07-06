from random import randrange
num_sorteado = randrange(0, 10)
chute = 0
count = 0
while chute != num_sorteado:
    chute = int(input('Digite um chute inteiro: '))
    if chute < num_sorteado:
        print('O número é maior')
        count += 1
    else:
        print('O número é menor')
        count += 1
print('Parabéns! Você acertou o número sorteado com {} palpites'.format(count))