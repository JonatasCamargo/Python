''' 
Faça um programa que leia o peso de cinco pessoas.No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 0

#laço de iteração
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))

#condição identificar o maior e menor
    if pess == 1:
        maior = pess
        menor = pess
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg')

print(f'O menor peso lido foi de {menor}Kg')        