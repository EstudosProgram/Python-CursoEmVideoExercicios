from datetime import date
n_maiores = 0
n_menores = 0
atual = date.today().year

for i in range(1, 8):
    ano_nasc = int(input('{}- Digite seu ano de nascimento: '.format(i)))
    idade = atual - ano_nasc
    if idade >= 21:
        n_maiores += 1
    else:
        n_menores += 1
print('São {} pessoas maiores de idade'.format(n_maiores))
print('São {} pessoas menores de idade'.format(n_menores))

