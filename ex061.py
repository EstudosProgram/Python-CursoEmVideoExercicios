#Não consegui mas ficou quase lá
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = 0
decimo = primeiro_termo + (10 - 1) * razao
while pa != decimo:
    pa += primeiro_termo*razao
    print(pa,end='->')
print('Acabou')