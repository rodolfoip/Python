palavra = str(input('Digite um palavra: ')).lower()
palavraJunta = ''.join(palavra.split())
palindromo = ''
for c in range(len(palavraJunta), 0, -1):
    palindromo = palindromo + palavraJunta[c - 1]
if palavraJunta == palindromo:
    print('A frase ou palavra "{}" é PALÍNDROMO'.format(palavra))
