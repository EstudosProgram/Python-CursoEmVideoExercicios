#Foi quase - PS: eu n estava conseguindo fazer pq tinha um metodo ja pronto para ver o max e o min em tupla
from random import randint
nuns_sort = (randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in nuns_sort:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado foi {max(nuns_sort)}')
print(f'O menor valor sorteado foi {min(nuns_sort)}')
