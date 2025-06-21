print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = pt + (11 - 1) * r
for i in range(pt, decimo, r):
    print('{}'.format(i), end=' -> ')
print('CABÔ')