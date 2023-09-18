'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são mmaiores.
'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

soma = 0


for pess in range (1, 8, 1):
    print('-=' * 20)    
    nasceu = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasceu

    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('-=' * 20)

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')            

print(f'E também tivemos {totmenor} pessoas menores de idade')