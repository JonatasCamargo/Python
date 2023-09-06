print(20 * '-=')
print('Analisador de Triângulos')
print(20 * '-=')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
certo = r1

if r1 < (r2 + r3):
    certo = r1
if r2 < (r1 + r3):
    certo = r2
if r3 < (r1 + r2):
    certo = r3
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
