from datetime import date
maiorIdade = 0
menorIdade = 0
for c in range(0,7):
    anoNasc = int(input('Digite seu ano de nascimento: '))
    if (date.today().year - anoNasc) >= 18:
        maiorIdade +=1
    else:
        menorIdade +=1
print('{} São menores de idade e {} são maiores de idade'.format(menorIdade,maiorIdade))