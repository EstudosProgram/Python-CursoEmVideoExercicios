num = int(input('Digite um número: '))
if num % 2 == 0:
    print(' \033[45;30m Par \033[m')
else:
    print('\033[44;30m Impar \033[m')