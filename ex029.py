veloc = float(input('\033[97mDigite a velocidade do carro: \033[m'))
if veloc > 80.0:
    multa = (veloc-80) * 7
    print('\033[97mA sua multa foi \033[31mR${:.2f}\033[m \033[97mPor favor dirige em até 80km/h'.format(multa))
else:
    print('\033[32mVocê não pagou nenhuma multa! Estava na velocidade permitida')