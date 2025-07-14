#Consegui fazer, mas n consegui deixar alinhado
listagem = ('banana', 7.0, 'maçã', 14, 'uva', 15, 'melão', 20)
print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*30)
for i in range(len(listagem)):
    if i % 2 == 0:
        print(listagem[i],end='.'*15)
    else:
        print(f'R${listagem[i]}')
print('-'*30)