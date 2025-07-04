print('='*30)
print('      10 TERMOS DE UMA PA')
print('='*30)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
    print(i, end=' -> ')
print('Acabou')