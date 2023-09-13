'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média entre 7.0 ou superior: APROVADO
'''

#captura de dados
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

#cálculo média
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
#condição notas abaixo de 5
if média < 5:
    print('Infelizmente você foi REPROVADO.')

#condição notas abaixo de 6.9 e acima de 5
elif média >= 5 and média < 7:
    print('Infelizmente você ficou de RECUPERAÇÃO.')

#condição notas acima de 6.9
elif média > 7:
    print('PARÁBENS, você foi APROVADO!')    
