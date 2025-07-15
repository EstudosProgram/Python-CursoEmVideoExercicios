#Passei desse ex - Consegui fazer, mas teve questa de repetição de print que eu n consegui tirar
valores = 0
numeros = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')