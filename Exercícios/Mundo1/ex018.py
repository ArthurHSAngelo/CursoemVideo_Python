import math
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(a, math.tan(math.radians(a))))
