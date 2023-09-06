## forma mais rapída
n1 = float(input('Digite um número: '))
print(f'O número digitado foi {n1} \n O seu dobro é {n1 * 2} \n '
      f'Seu triplo é {n1 * 3} \n E sua raiz é {n1 ** (1/2):.2f}')

## forma para quem ainda pretende usar as variaveis no código
n1 = float(input('Digite um número: '))
db = n1 * 2
tr = n1 * 3
ra = n1 ** (1/2)
print(f'O número digitado foi {n1}, o seu dobro é {db}, seu triplo {tr} e sua raiz {ra:.2f}')