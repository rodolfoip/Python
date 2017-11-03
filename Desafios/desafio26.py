frase = input('Digite uma frase: ')
incidencia = frase.lower().count('a')
primeiraOcorrencia = frase.lower().find('a')
ultimaOcorrencia = frase.lower().rfind('a')

print('Quantas vezes apareceu a letra A: {}\nPrimeira ocorrência: {}\nUltima ocorrência: {}'.format(incidencia, primeiraOcorrencia, ultimaOcorrencia))
