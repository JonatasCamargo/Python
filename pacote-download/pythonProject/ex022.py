nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras (sem contar os espaços)'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) <== mesmo objetivo que o código de cima.