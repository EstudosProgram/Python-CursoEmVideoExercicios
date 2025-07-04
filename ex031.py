dist = float(input('\033[30;43mDigite a distancia da viagem em Km:\033[m '))
if dist <= 200:
    print('O preço da passagem será por \033[1;36;47m R${} \033[m'.format(dist*0.50))
else:
    print('O preço da passagem será por \033[1;36;47m R${} \033[m'.format(dist * 0.45))