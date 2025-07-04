n = 0
count = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    count += 1
    s += n
print('Foram {} números e a soma deles deu {}'.format(count-1, s-999))