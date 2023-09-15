'''
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 a 500
'''

#laço de iteração entre 1 a 500
s = 0
for c in range(1, 500):
    if (c % 2) and (c % 3): # condição se é impar e múltiplo de três
        s += c
print(f'O somatório de todos os valores ímpares múltiplos de três, foi: {s}')
