altura = int(input('Qual a altura da parede: '))
largura = int(input('Qual a largura da parede: '))
litrosTinta = float(largura*altura / (2**2))
print('Voce vai precisar de {} litros de tinta'.format(litrosTinta))