'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
'''


#captura de dados
frase = str(input('Digite uma frase: ')).strip().upper()

#cortes por espaços (separação)
palavras = frase.split()

#agrupamento de caracteres
junto = ''.join(palavras)

#inversão da frase digitada
inverso = ''

#Iteração para ler os carcateres de trá para frente
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso da {junto} é {inverso}')    

#condição se é palíndromo ou não
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo')    
