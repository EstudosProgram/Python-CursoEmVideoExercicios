#Consegui fazer, mas n consegui deixar alinhado
listagem = ('banana', 7.0, 'maçã', 14, 'uva', 15, 'melão', 20)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for i in range(len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<40}',end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
print('-'*40)