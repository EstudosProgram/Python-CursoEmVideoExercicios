#Não consegui essa bomba tbm
termo = int(input('Digite quantos termos você quer mostrar: '))
count = 3
t1 = 0
t2 = 1
print('{} -> {} '.format(t1, t2), end='')
while count <= termo:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')