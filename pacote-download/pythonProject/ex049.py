'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

#captura de dados
n = int(input('Digite um número inteiro: '))

#laço de iteração 1 a 10
for c in range(1, 11):
    print(n * c)
    