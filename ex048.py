s = 0
cont = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))