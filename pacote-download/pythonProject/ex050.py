'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
'''

#laço de iteração seis inputs
s = 0
for c in range(1, 7):
    n = int(input('Digite um valor inteiro: '))
    if (n % 2) == 0: # condição para somar pares
        s += n
print(f'Está é a soma de todos os números pares digitados: {s}')
