'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

#captura de dados
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite novamente um número inteiro: '))

#condição se num1 for maior que num2
if num1 > num2:
    print(f'O primeiro número digitado: {num1} é MAIOR que o segundo: {num2}')

#condição se num2 for maior que num1    
elif num2 > num1:
    print(f'O segundo número digitado: {num2} é MAIOR que o primeiro: {num1}')

#condição se os valores forem iguais    
else:
    print('Não existe valor MAIOR, os dois números são iguais')
