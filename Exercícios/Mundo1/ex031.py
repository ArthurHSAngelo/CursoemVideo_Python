d = int(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(d))
'''if d <= 200:
    v1 = 0.50 * d
    print('O valor da passagem é de R${:.2f}'.format(v1))
else:
    v2 = 0.45 * d'''
preco = d * 0.50 if d <= 200 else d * 0.45
print('O valor da passagem é de R${:.2f}'.format(preco))