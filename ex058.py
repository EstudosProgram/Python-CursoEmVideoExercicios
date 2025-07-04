from random import randrange
num_sorteado = randrange(0, 10)
chute = 0
while chute != num_sorteado:
    chute = int(input('Digite um chute inteiro: '))
    if chute < num_sorteado:
        print('O número é maior')
        chute = int(input('Digite um chute inteiro: '))
    else:
        print('O número é menor')
        chute = int(input('Digite um chute inteiro: '))
print('Parabéns! Você acertou o número sorteado')
