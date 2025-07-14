num_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
usuario = int(input('Digite um número entre 0 e 20: '))
while True:
    if usuario > 20 or usuario < 0:
        usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {num_extenso[usuario]}')