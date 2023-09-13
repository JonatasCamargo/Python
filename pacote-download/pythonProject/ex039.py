'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

#captura de dados
from datetime import date
atual = date.today().year

ano_nasc = int(input('Digite seu ano de nascimento: '))

#calculo idade
idade = atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {atual}')

#condição para jovem com 18 anos
if idade == 18:
    print('Você tem que se alistar imediatamente!')

#condição para menor de idade
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para você se alistar')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')

#condição para jovens acima de 18 anos
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em: {ano}')
