from datetime import date

anoNasc = int(input('Digite a seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade == 18:
    print('\033[1;31mEstá na hora de se alistar nas forças desarmadas\033[m')
elif idade < 18:
    print('\033[32mVocê ainda terá de se alistar em {} anos,'.format(18-idade), end='')
    print(' ou seja em {} você deverá se alistar\033[m'.format(anoNasc + 18))
else:
    print('\033[7mO seu alistamento foi em {}\033[m'.format(anoNasc + 18))

