nome = input('Digite o nome de uma cidade: ')
dividido = nome.lower().split('sant')
print('Começa com santo: {}'.format(dividido[0] in 'sant'))