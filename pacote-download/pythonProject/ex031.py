di = float(input('Digite a distância(Km) da sua viagem(ex:20): '))
p1 = di * 0.50
p2 = di * 0.45

if di <= 200:
    print(f'O valor de sua viagem de {di}Km ficará R${p1:.2f}')
else:
    print(f'O valor de sua viagem de {di}Km ficará R${p2:.2f}')

"""
MODO SIMPLIFICADO
di = float(input('Digite a distância(Km) da sua viagem(ex:20): '))
preço = di * 0.50 if di <= 200 else di * 0.45
print(f'O valor de sua viagem de {di}Km ficará R${preço:.2f}')
"""
