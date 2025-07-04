percorrido_em_km = float(input('Quantos kms percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))
preco_a_pagar = (percorrido_em_km * 0.15) + (dias * 60)
print('Você deve pagar R${:.2f}!'.format(preco_a_pagar))