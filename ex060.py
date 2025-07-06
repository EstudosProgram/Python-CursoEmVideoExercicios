#Utilizando o math
"""from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))"""

#NÃO CONSEGUI FAZER -> resolução
num = int(input('Digite um número: '))
c = num
f = 1
print('{}! '.format(num),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f),end='')

#FOR - consegui
"""for c in range(num-1, 0, -1):
    print('{} x {}'.format(num, c))
    mult = mult*c
print(mult)"""
