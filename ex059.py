from time import sleep
val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print("""---- Menu ----
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        soma = val1 + val2
        print('\n\033[1mA soma de {} + {} = {:.2f}\033[m\n'.format(val1, val2, soma))
        sleep(1)
    elif opcao == 2:
        mult = val1 * val2
        print('\n\033[1mA multiplicação de {} x {} = {:.2f}\033[m\n'.format(val1, val2, mult))
        sleep(1)
    elif opcao == 3:
        if val1 > val2:
            print('\n\033[1mO maior número é o número {}\n\033[m\n'.format(val1))
            sleep(1)
        else:
            print('\n\033[1mO maior número é o número {}\n\033[m\n'.format(val2))
            sleep(1)
    elif opcao == 4:
        print('\n\033[31mEscolha novamente os números\033[m\n')
        sleep(1)
        val1 = float(input('Digite o primeiro valor: '))
        val2 = float(input('Digite o segundo valor: '))
        sleep(1)

print('Obrigado, volte sempre!')
