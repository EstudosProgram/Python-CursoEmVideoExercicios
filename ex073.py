times_brasileirao = ('Flamengo','Chapecoense','Cruzeiro','Bragantino',
                     'Palmeiras','Bahia','Fluminense','Atlético-MG',
                     'Botafogo','Mirassol','Corinthians','Grêmio',
                     'Ceará','Vasco','São Paulo','Santos','Vitória',
                     'Internacional','Fortaleza','Juventude','Sport')
print(f'O 5 primeiros colocados são: {times_brasileirao[:5]}')
print(f'Os últimos 4 colocados na tabela: {times_brasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(times_brasileirao)}')
print(f'O Chapecoense está na {times_brasileirao.index('Chapecoense')+1} posição')