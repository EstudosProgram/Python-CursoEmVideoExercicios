valor = float(input('Digite o valor do produto: '))
opcao = int(input("""Escolha a forma de pagamento:
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
-> """))
if opcao == 1:
    print('No total deu: R${:.2f}'.format(valor - valor * (10 / 100)))
elif opcao == 2:
    print('No total deu: R${:.2f}'.format(valor - valor * (5 / 100)))
elif opcao == 3:
    print('No total deu: R${:.2f}'.format(valor))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('No total deu: R${:.2f} por mês'.format((valor + valor * (20 / 100)) / parcelas))
else:
    print('Opção inválida!')