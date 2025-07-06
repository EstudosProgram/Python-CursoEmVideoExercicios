#Não consegui mas ficou quase lá - PS: consegui fazer
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = primeiro_termo
count = 1
while count <= 10:
    print(pa, end=' -> ')
    pa += razao
    count += 1
print('Acabou')