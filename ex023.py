#corrijido
num = int(input('Digite um número de 0 a 9999: '))
#voce divide por inteiro e usa 0 %10 para pegar o ultimo que sobrou da divisão
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""unidade: {}
dezena: {}
centena: {}
milhar: {}""".format(u, d, c, m))