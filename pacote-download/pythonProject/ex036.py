'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

#perguntas
valor_casa = float(input('Qual será o valor da casa? '))
salário = float(input('Qual é seu salário atual? '))
qtd_anos = int(input('Em quantos anos deseja pagar as prestações? '))

#calculo para obter valor da prestação
prestação = (valor_casa) / (qtd_anos * 12)

#condição para o empréstimo não aprovado
if prestação >= (salário - (salário * 30 / 100)):
    print('Infelizmente seu empréstimo não foi aceito, pois as parcelas excederão 30% de seu salário')

#condição se o empréstimo foi aprovado
else:
    print(f'Este será o valor de suas parcelas mensais: {prestação:.2f}')  
