'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogod de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles
'''

#importando biblioteca
from time import sleep

#fazendo o laço regressivo
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Começou os fogosssss!!!\n BUMMMM!!!')    
