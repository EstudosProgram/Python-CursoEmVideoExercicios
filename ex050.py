s = 0
count = 0
for i in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        count += 1
print('Foram {} números e a soma dos pares foi = {} '.format(count, s))