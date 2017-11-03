media = 0.0
maisVelho = 0
nomeMaisVelho = ''
menosVinteAnos = 0
for c in range(0, 4):
    print('-='*15)
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ')
    print('-=' * 15)
    media += idade
    if sexo == 'masc':
        if idade > maisVelho:
            nomeMaisVelho = idade
    elif sexo == 'fem':
        if idade < 21:
            menosVinteAnos += 1
print('''A média de idade é {}, 
o homem mais velho tem {} anos, 
{} mulheres tem menos de 20 anos'''.format(media / 4, nomeMaisVelho, menosVinteAnos))
