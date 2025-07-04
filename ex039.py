from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_nasc
if idade == 18:
    print('Já é hora de se alistar!')
elif idade < 18:
    print('Ainda vai se alistar')
else:
    print('Se já passou {} anos para se alistar!'.format(idade - 18))