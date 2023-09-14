'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from time import sleep #importando biblioteca para 'temporizar'
from random import randint #importando biblioteca para randomizar
itens = ('Pedra', 'Papel', 'Tesoura')

#aplicando a randomização em itens
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

#temporizando o JO-KEN-PÔ
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print('-=' * 11)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-=' * 11)

#condições sobre escolhas do computador e jogador
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')

#condições sobre escolhas do computador e jogador
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida') 

#condições sobre escolhas do computador e jogador
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
