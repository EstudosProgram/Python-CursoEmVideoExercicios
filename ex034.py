salario = float(input('Digite o seu salário: '))
if salario > 1250:
    print('\033[32mSeu salário com aumento: \033[1;30;43mR${}\033[m'.format((salario*0.10)+salario))
else:
    print('\033[32mSeu salário com aumento: \033[1;30;43mR${}\033[m'.format((salario*0.15)+salario))