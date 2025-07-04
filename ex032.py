ano = int(input('Digite um ano ou coloque 0 para analisar o ano atual: '))
#Extra, se o usuário quiser saber do ano atual se é bissexto
if ano == 0:
    from datetime import date
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano {} é \033[1;4;36mbissexto'.format(ano))
else:
    print('\033[4;31mNão é bissexto')