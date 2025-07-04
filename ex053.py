frase = str(input('Digite uma frase: ')).split()
frase_junta = ''.join(frase).upper()
frase_invertida = ''
#vai no último índice até o 0 de forma inversa
for letra in range(len(frase_junta) -1, -1, -1):
    frase_invertida += frase_junta[letra]
print('A frase {} fica assim invertida: {}'.format(frase_junta, frase_invertida))
if frase_junta == frase_invertida:
    print('É Palíndromo')
else:
    print('Não é palíndromo')