maiorPeso = 0
menorPeso = 0
for c in range(0, 5):
    peso = float(input('Escreva aqui seu peso: '))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso < menorPeso:
            menorPeso = peso
        elif peso > maiorPeso:
            maiorPeso = peso

print('O menor peso medido foi {} e o maior {}'.format(menorPeso, maiorPeso))
