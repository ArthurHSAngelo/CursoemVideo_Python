from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
u = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
adv = randint(0,5)
if u == adv:
    print('PARABÉNS! Você venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(adv,u))