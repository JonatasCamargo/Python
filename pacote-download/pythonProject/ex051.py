'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
#captura de dados
primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )


ultimo = primeiro + (10-1)*razao
ultimo = ultimo + 1

for c in range(primeiro, ultimo, razao):
    print(c)
