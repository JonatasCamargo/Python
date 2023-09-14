'''
Deselvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
'''

#captura de dados
peso = float(input('Digite seu peso(KG): '))
altu = float(input('Digite seu altura(M): '))

#cálculo IMC
calc = peso / (altu ** 2)
print(f'O seu IMC será: {calc:.1f}')

#condição abaixo do peso
if calc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL, procure um médico!')

#condição peso ideal
elif calc >= 18.5 and calc < 25:
    print('Você está com um PESO NORMAL, PARABÉNS!')

#condição sobrepeso
elif calc >= 25 and calc < 30:
    print('Você está ACIMA DO PESO NORMAL, cuide-se mais!')

#condição obeso    
elif calc >= 30 and calc < 40:
    print('Você está OBESO, faça exercícios e cuide da alimentação!')

#condição obesidade mórbida
elif calc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, procure um médico urgentemente!')   
