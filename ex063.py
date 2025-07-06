#Não consegui essa bomba tbm
n = int(input('Digite um número inteiro: '))
count = 1
while count != n:
    fibonacci = count + (count - 1)
    print('{}'.format(fibonacci),end='->')
    count += 1