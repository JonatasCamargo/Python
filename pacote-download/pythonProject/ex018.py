from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print(f'O ângulo de {an} tem o seno de {se:.2f}')
print(f'O ângulo de {an} tem o cosseno de {co:.2f}')
print(f'O ângulo de {an} tem a tangente de {ta:.2f}')
