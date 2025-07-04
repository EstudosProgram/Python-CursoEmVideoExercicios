import datetime

data_nasc = int(input('Digite o ano que você nasceu: '))
idade = datetime.date.today().year - data_nasc
if idade <= 9:
    print('\033[44;30m MIRIM \033[m')
elif idade <= 14:
    print('\033[43;30m INFANTIL \033[m')
elif idade <= 19:
    print('\033[45;30m JUNIOR \033[m')
elif idade == 20:
    print('\033[46;30m SÊNIOR \033[m')
else:
    print('\033[7m MASTER \033[m')