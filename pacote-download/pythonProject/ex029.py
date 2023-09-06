ve = float(input('Digite a velocidade do carro(ex: 20): '))
mu = (ve - 80) * 7

if ve >= 81:
    print(f'Sua velocidade era de {ve}Km/h, '
          f'por conta disso você foi multado, '
          f'a multa tem o valor de R${mu:.2f}')
else:
    print('Parabéns você está sendo um otimó condutor!')
