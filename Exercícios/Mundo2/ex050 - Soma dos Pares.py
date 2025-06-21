s = 0
c = 0
for i in range(1, 7):
    n = int(input('Digite o {} número: '.format(i)))
    if n % 2 == 0:
        s +=  n
        c += 1
print('Você digitou {} números PARES e a soma dos pares é {}'.format(c, s))