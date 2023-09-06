dia = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
vt = (60 * dia) + (0.15 * km)
print(f'O total a pagar é de R${vt:.2f}')
