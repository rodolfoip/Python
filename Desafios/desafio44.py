print('{:=^40}'.format(' Lojas Jonhson '))
valorProduto = float(input('Digite o valor do produto a ser pago: '))
aVistaDinheiro_cheque = 0.10
aVistaCartao = 0.05
parceladoCartao = 1.20
opcao = int(input('''Digite a opção: 
[ 1 ] Dinheiro ou cheque à vista
[ 2 ] Cartão à vista
[ 3 ] Parcelado no cartão
'''))

if opcao == 1:
    valorFinal = valorProduto - (valorProduto * aVistaDinheiro_cheque)
elif opcao == 2:
    valorFinal = valorProduto - (valorProduto * aVistaCartao)
elif opcao == 3:
    nParcela = int(input('Digite quantas parcelas serão feitas: '))
    if nParcela > 2:
        valorFinal = valorProduto * parceladoCartao
    else:
        valorFinal = valorProduto
    valorParcela = valorFinal / nParcela
    print('O valor das parcelas será R${:.2f}'.format(valorParcela))
else:
    valorFinal = valorProduto
    print('OPÇÃO INVALIDA')
print('O valor do produto é R${:.2f}'.format(valorFinal))
