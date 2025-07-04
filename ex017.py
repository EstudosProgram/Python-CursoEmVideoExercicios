import math

catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjacente)
print('Hipotenusa = {:.2f}'.format(hipotenusa))