#correção
n = count = s = 0
n = int(input('Digite um número: '))
while n != 999:
    s += n
    count += 1
    n = int(input('Digite um número: '))
print('Foram {} números e a soma deles deu {}'.format(count, s))