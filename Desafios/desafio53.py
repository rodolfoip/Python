palavra = str(input('Digite um palavra: ')).lower()
palavraP = palavra.replace(' ', '').replace(',','').replace('-','').replace('ô','o')
palindromo = ''
for c in range(len(palavraP), 0, -1):
    palindromo = palindromo + palavraP[c - 1]
print(palindromo)
if palavraP == palindromo:
    print('A frase ou palavra "{}" é PALÍNDROMO'.format(palavra))
