nome = input('\033[37mDigite seu nome completo: \033[m')
dividido = nome.split()
print("""primeiro: \033[31;44m {} \033[m
último:   \033[33;45m {} \033[m
""".format(dividido[0], dividido[-1]))