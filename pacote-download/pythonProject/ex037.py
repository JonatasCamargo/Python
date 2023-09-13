'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

#captura de dados
num = int(input('Digite um número inteiro: '))

#escolha do usuário
escolha = int(input('Qual será base de conversão?\n (- [1] para binário - [2] para octal - [3] para hexadecimal): '))

#condição caso a escolha seja 1
if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

#condição caso a escolha seja 2
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

#condição caso a escolha seja 3
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

#condição caso a escolha não for entre 1 e 3
else:
    print('Escolha errada. Tente novamente.')