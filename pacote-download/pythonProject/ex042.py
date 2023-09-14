'''
Refaça o DESAFIO 35 dos triãngulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

-Equilátero: Todos os lados iguais
-Isósceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
'''

#captura de dados
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

#condição para confirmar se pode formar 
if r1 < (r2 + r3) or r2 < (r1 + r3) or r3 < (r1 + r2):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

#condição do tipo do triângulo
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')

#condição caso não se possa formar
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')