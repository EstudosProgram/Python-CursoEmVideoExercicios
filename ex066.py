#Foi easy
cont = s = 0
while True:
    n = int(input('Digite um número (999 faz parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram {cont} números e a soma deu {s}')