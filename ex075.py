#Passei desse ex - Consegui fazer, mas teve questa de repetição de print que eu n consegui tirar
valores = 0
numeros = ()
cont = 1
cont9 = 0
while cont <= 4:
    valores = int((input(f'Digite o {cont}° valor: ')))
    numeros += (valores,)
    cont += 1
for i in range(0, len(numeros)):
    if numeros[i] == 9:
        cont9 += 1
for i in range(0, len(numeros)):
    if numeros[i] == 3:
        print(f'O número 3 aparece na {i+1}ª posição')
    else:
        print('Não há o número 3')
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        print(f'Os valores pares digitados foram {numeros[i]}')
print(f'O valor 9 apareceu {cont9} vez(es)')


