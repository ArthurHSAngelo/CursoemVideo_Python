s = float(input('Qual é o salário do Funcionário? R$'))
s2 = s + (s * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, s2))
