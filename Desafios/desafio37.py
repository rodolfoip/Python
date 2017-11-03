num = int(input('Digite um número inteiro: '))
print('''\033[4;34m[ 1 ]-Converter para binário 
[ 2 ]-Converter para hexadecimal 
[ 3 ]-Converter para octal\n\033[m''')
opcao = int(input('Selecione uma das opções:'))

if opcao == 1:
    print('O valor {} convertido para BINÁRIO fica {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} convertido para HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
elif opcao == 3:
    print('O valor {} convetido para OCTAL fica {}'.format(num, oct(num)[2:]))
else:
    print('Opção inválida')