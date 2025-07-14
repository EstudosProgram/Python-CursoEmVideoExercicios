times_brasileirao = ('Flamengo','Chapecoense','Cruzeiro','Bragantino','Palmeiras','Bahia','Fluminense','Atlético-MG','Botafogo','Mirassol','Corinthians','Grêmio','Ceará','Vasco','São Paulo','Santos','Vitória','Internacional','Fortaleza','Juventude','Sport')
print(f'O 5 primeiros colocados são: {times_brasileirao[:5]}')
print(f'Os últimos 4 colocados na tabela: {times_brasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(times_brasileirao)}')
#Não consegui fazer a letra D
for posicao in range(0,len(times_brasileirao)):
    if 'Chapecoense' in times_brasileirao:
        print(posicao)
    else:
        print('O Chapecoense não está na lista')