from itertools import count

frase = str(input('Digite um frase qualquer: ')).upper().strip()
contador = frase.upper().count('A',0)
print('\033[1;97mA primeira posição que aparece na frase: {}'.format(frase.find('A')+1))
print('\033[1;97mA ultima posição que aparece na frase: {}'.format(frase.rfind('A')+1))
print('\033[1;97mA letra "a" apareceu {} vez(es)'.format(contador))