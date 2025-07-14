#Foi qause
from random import randint
nuns_sort = (randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
print(f'Os valores sorteados foram {nuns_sort[0]} {nuns_sort[1]} {nuns_sort[2]} {nuns_sort[3]} {nuns_sort[4]}')
maior = nuns_sort[0]
menor = nuns_sort[0]
for i in range(0, len(nuns_sort)):
    if i+1 > maior:
        maior = i
    elif i+1 < menor:
        menor = i

    print(f'O maior valor sorteado foi {maior}')
    print(f'O menor valor sorteado foi {menor}')

"""if len(nuns_sort) > maior:
    maior = nuns_sort[+1]
elif len(nuns_sort) < menor:
    menor = nuns_sort[+1]"""