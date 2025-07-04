valor_casa = float(input('Qual valor da casa: '))
salario = float(input('Qual seu salário: '))
anual = int(input('Em quantos anos você quer pagar a casa: '))
valor_mensal = valor_casa / (anual * 12)
if valor_mensal >= salario * (30 / 100):
    print('O valor mensal de R${:.2f} não pode ser 30% do seu salário. \033[31mEmpréstimo negado!\033[m'.format(valor_mensal))
else:
    print('\033[32mEmpréstimo liberado!\033[m Seu valor mensal vai ser de R${:.2f}'.format(valor_mensal))