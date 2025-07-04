num = int(input('Escreva um número qualquer: '))
opcoes = int(input('Qual será a base de conversão:\n- 1 Para binário\n- 2 Para octal\n- 3 Para hexagonal\n-> '))
if opcoes == 1:
    print(bin(num)[2:])
elif opcoes == 2:
    print(oct(num)[2:])
elif opcoes == 3:
    print(hex(num)[2:])
else:
    print('Opção incorreta!')