n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2

print('E sua média foi: {}'.format(media))

if media < 5.0:
    print('Reprovado!!!')
elif 7 > media > 5.0:
    print('Recuperação!!')
else:
    print('Aprovado!!!')
