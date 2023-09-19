'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa, mostre:

-A média aritimética
-Qual é o nome do Homem mais velho
-Quantas mulheres têm menos de 20 anos
'''


média = 0
velho = 0
velho_homem = 0
nome_velho = 0
maior = 0
menor = 0

#laço iteração
for p in range (1, 5, 1):
    print('-=' * 10, f'{p}ª PESSOA', '-=' * 10)    
    nome = str(input('Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

#condição para armazenar a idade em 'média'. (cálculo será feito no print)
    if idade >= 0:
        média += idade
    else:
        print('Digite uma idade verdadeira!')

#condição para o homem mais velho
    if p == 1 and sexo in 'Mm':
        velho_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > velho_homem:
        velho_homem = idade
        nome_velho    

#condição para a mulher com menos de 20 anos
    if idade <= 20 and sexo == 'F':
        menor += 1
    else:
        maior += 1        

print('-=' * 20)
print(f'A média de idade do grupo é de {média / 4:.1f}')    

print(f'O homem mais velho tem {velho_homem} anos e se chama {nome_velho}.')

print(f'Ao todo tivemos {menor} mulheres com menos de 20 anos')
print('-=' * 20)
