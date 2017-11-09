# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = ['Telefonou para a vitima', 'Esteve no local do crime', 'Mora perto da vitima', 'Devia para a vitima',
             'Ja trabalhou para a vitima']
cont = 0
for c in range(0, 5):
    print(perguntas[c])
    opcao = int(input('[ 0 ] Para SIM \n[ 1 ] Para nao\n'))
    if opcao == 0:
        cont += 1
    else:
        print('Digite uma opçao valida')
        c -= 1
if cont == 2:
    print('Suspeito')
elif 3 < cont <=4:
    print('Cumplice')
elif cont == 5:
    print('Assasino')
