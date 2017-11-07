# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
populacaoA = int(80000)
taxaA = float(0.3)
populacaoB = int(200000)
taxaB = float(0.015)
cont = 0
while (populacaoA < populacaoB):
    populacaoA += populacaoA * taxaA
    populacaoB += populacaoB * taxaB
    cont += 1

print("Em {} anos a População de A: {:.0f} será maior que a de População B: {:.0f}".format(cont, populacaoA, populacaoB))