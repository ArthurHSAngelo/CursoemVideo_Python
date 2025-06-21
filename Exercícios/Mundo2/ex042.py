print('-=' * 20)
print('Analisador de Triângulos v2.0')
print('-=' * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    if r1 == r2 == r3:
        print('Com essas retas é possível formar um triângulo EQUILÁTERO')
    elif (r1 == r2 and r1 != r3) or (r2 == r3 and r2 != r1) or (r1 == r3 and r1 != r2):
        print('Com essas retas é possível formar um triângulo ISÓSCELES')
    else:
        print('Com essas retas é possível formar um triângulo ESCALENO')
else:
    print('\033[31mNão é possível formar um triângulo com essas retas!')
