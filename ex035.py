r1 = int(input('Digite a reta 1: '))
r2 = int(input('Digite a reta 2: '))
r3 = int(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triângulo')
else:
    print('\033[1;31mNão é possivel')