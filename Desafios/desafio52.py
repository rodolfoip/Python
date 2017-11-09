n = int(input('Digite um número inteiro: '))
cont = 0;
for c in range(1, n + 1):
    if (n % c) == 0.0:
        cont += 1
        print('\33[33m', end='')
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')

print('\33[;;m \nO número {} foi divisivel {} vezes'.format(n,cont))
if (cont == 2):
    print('\nEntão ele é um número PRIMO')
else:
    print('Então ele é não um número PRIMO')
