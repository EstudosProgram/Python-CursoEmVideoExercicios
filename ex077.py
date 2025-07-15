#Não consegui fazer
palavras = ('oi', 'tudo', 'para', 'amo', 'o', 'gato')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')