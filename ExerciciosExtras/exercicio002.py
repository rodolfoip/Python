#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Digite uma letra: ')).lower()

if len(letra)== 1:
    if(letra == 'a'or letra == 'b' or letra  == 'c' or letra  == 'd' or letra  == 'e'):
        print('A letra digitada é uma VOGAL!!!')
    else:
        print('A letra digitada é uma CONSOANTE!!!')
else:
    print('Digite apenas uma letra')