A = float(input('Digite o primeiro segmento: '))
B = float(input('Digite o segundo segmento: '))
C = float(input('Digite o terceiro segmento: '))


if abs(B-C) < A < B + C and abs(A-C) < B < A + C and abs(A-B)< C < A+B:
    if A != B != C != A:
        print('Triangulo escaleno')
    elif A == B == C:
        print('Triângulo equilátero')
    else:
        print('Triângulo isósceles')
else:
    print('Os segmentos inseridos não podem formar um triangulo!!!')
