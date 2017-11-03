#Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = [0,0,0]
lista[0] = int(input('Digite o primeiro número: '))
lista[1] = int(input('Digite o segundo número: '))
lista[2] = int(input('Digite o terceiro número: '))

for c in range(0,3):
    for d in range(0,3):
        if lista[c] < lista[d]:
            aux = lista[d]
            lista[d] = lista[c]
            lista[c] = aux
print(lista)