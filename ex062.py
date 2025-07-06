#Não consegui fazer pq precisa do ex anterior - vi a resolução
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = primeiro_termo
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print(pa, end=' -> ')
        pa += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais: '))
print('FIM')
