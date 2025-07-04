r1 = int(input('Digite a reta 1: '))
r2 = int(input('Digite a reta 2: '))
r3 = int(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triângulo!')
    if r1 == r2 and r2 == r3 and r1 == r3:
        print('Equilátero: todos os lados iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isóceles: dois lados iguais')
    else:
        print('Escaleno: todos os lados diferentes')
else:
    print('\033[1;31mNão é possivel\033[m')