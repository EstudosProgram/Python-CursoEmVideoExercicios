#Utilizando com o FOR
"""while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    else:
        print('-'*20)
        for i in range(1, 11):
            mult = n * i
            print(f'{n} x {i} = {mult}')
        print('-' * 20)
print('FIM')"""

#Utilizando com o WHILE
while True:
    cont = 0
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    while cont < 10:
        cont += 1
        mult = n * cont
        print(f'{n} x {cont} = {mult}')
print('FIM')