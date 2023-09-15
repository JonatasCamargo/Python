'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

#captura de dados
n = int(input('Digite um número inteiro: '))
s = 0

#laço de iteração
for c in range(1,n+1):
    if n % c == 0:  #condição para verficar quantas vezes ele pode ser dividido e o resto ser igual a zero
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')    
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {s} vezes')

#condição para verificar se é ou não número primo
if s == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')    
