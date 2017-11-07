# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
vetor = []
par = []
impar = []
for c in range(1, 21):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    vetor.append(n)
print("Vetor",vetor, "\nVetor Par",par,"\nVetor impar",impar)
