# Escreva um programa que receba o salário de um funcionário
# se ele ganhar acima de R$1250 10% de aumento, se não 15% de aumento

sa = float(input('Digite seu salário: R$'))
dez = sa + (sa * 10 / 100)
qui = sa + (sa * 15 / 100)

if sa > 1250:
    print(f'Com 10% de aumento seu salário ficou R${dez:.2f}')
else:
    print(f'Com 15% de aumento seu salário ficou R${qui:.2f}')

