from random import randint
from time import sleep
print('-=-' * 10)
print('Olá Usuário! \n De 0 a 5, qual número estou pensando?')
print('-=-' * 10)

teste = (int(input('Digite o número que estou pensando: ')))
num = randint(0, 5)
print('PROCESSANDO...')
sleep(2)

if num == teste:
    print(f'Você  ganhou!, eu estava pensando no número {num}')
else:
    print(f'Você perdeu rsrs, o número que eu estava pensando era {num}')
