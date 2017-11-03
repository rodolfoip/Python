maiorPeso = 0
menorPeso = 9999
for c in range(0, 5):
    peso = float(input('Escreva aqui seu peso: '))
    if peso < menorPeso:
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso

print('O menor peso medido foi {} e o maior {}'.format(menorPeso, maiorPeso))
