#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
n = int(input('Digite um número: '))
for c in range(n,1,-1):
    n = n * (c -1)
print(n)