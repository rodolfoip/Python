print('MOSTRANDO NÚMEROS IMPARES E MULTIPLOS DE 3, NO INTERVALO ENTRE 1 E 500')
soma = 0
count = 0
for c in range(1,501,2):
    if (c % 3) == 0:
        soma += c
        count +=1
print('{} são impares e multiplos de 3, resultando na soma de {}'.format(count, soma))