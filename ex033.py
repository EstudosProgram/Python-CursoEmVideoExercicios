n1 = int(input('\033[35mDigite o primeiro número: \033[m'))
n2 = int(input('\033[36mDigite o segundo número: \033[m'))
n3 = int(input('\033[34mDigite o terceiro número: \033[m'))
#Verificando o número maior
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[7m O maior número é o {} \033[m'.format(maior))
#Verificando o número menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[7m O menor número é o {} \033[m'.format(menor))

#Versão normal e mais comprida
#if n1 > n2 and n1 > n3:
#    print('O maior número é {} '.format(n1))
#elif n2 > n1 and n2 > n3:
#    print('O maior número é {} '.format(n2))
#elif n3 > n1 and n3 > n2:
#    print('O maior número é {} '.format(n3))


