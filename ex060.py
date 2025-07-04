#NÃO CONSEGUI FAZER
num = int(input('Digite um número: '))
count = 0
mult= num
'''while count != num:
    mult = num * (num -1)
    count += 1
    print(' = {}', end='x')
print('{}!'.format(num), end='')

print(' = {}',end='')'''

#FOR - consegui
for c in range(num-1, 0, -1):
    print('{} x {}'.format(num, c))
    mult = mult*c
print(mult)