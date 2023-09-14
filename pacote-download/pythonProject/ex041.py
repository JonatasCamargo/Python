'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM     -Até 19 anos: JUNIOR
-Até 14 anos: INFANTIL -Até 25 anos: SÊNIOR
                       -Acima: MASTER
'''

#captura de dados
from datetime import date
atual = date.today().year

ano_nasc = int(input('Digite seu ano de nascimento: '))

#calculo idade
idade = atual - ano_nasc
print(f'O atleta tem {idade} anos')

#condição atleta mirim
if idade <= 9:
    print('Classificação: MIRIM')

#condição atleta infantil    
elif idade <= 14 and idade > 9:
    print('Classificação: INFANTIL')

#condição atleta junior
elif idade <= 19 and idade > 14:
    print('Classificação: JUNIOR')

#condição atleta sênior    
elif idade <= 25 and idade > 19:
    print('Classificação: SÊNIOR')

#condição atleta master    
else:
    print('Classificação: MASTER')  