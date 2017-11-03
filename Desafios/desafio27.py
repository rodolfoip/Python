nome = input('Digite seu nome: ')
dividido = nome.split()
print('Primeiro nome: {}\nSegundo nome: {}'.format(dividido[0], dividido[len(dividido)-1]))