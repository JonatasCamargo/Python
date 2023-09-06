'''co = float(input('Digite o comprimento do cateto oposto: '))    ## código sem usar a biblioteca math
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa do triângulo retangulo é: {hi:.2f}')'''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))    ## código usando a biblioteca math
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa do triângulo retangulo é: {hi:.2f}')
