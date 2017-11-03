n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O maior valor é o {}'.format(n1))
elif n1 < n2:
    print('O Maior valor é o {}'.format(n2))
else:
    print('Não existe maior os dois valores são iguais')