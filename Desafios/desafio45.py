from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
print('{:#^30}'.format(' JOKENPÔ '))
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogadaUsuario = int(input('Qual sua escolha?\n'))
jogadaComputador = int(randint(0,2))
#Pedra fode tesoura
#Papel fode pedra
#Tesoura fode papel
print('JO')
sleep(0.3)
print('KE')
sleep(0.3)
print('PO')
sleep(0.3)
print('-='*15)
print('Computador escolheu {}'.format(itens[jogadaComputador]))
print('Você escolheu {}'.format(itens[jogadaUsuario]))
print('-='*15)
if jogadaComputador == 0 and jogadaUsuario == 0 or jogadaComputador == 1 and jogadaUsuario == 1 or jogadaComputador == 2 and jogadaUsuario == 2:
    print('Empate!!!')
elif jogadaComputador == 0 and jogadaUsuario == 1 or jogadaComputador == 1 and jogadaUsuario == 2 or jogadaComputador == 2 and jogadaUsuario == 0:
    print('Você ganhou!!!')
else:
    print('Você perdeu!!!')