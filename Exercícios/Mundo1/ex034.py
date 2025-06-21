s = float(input('Qual é o salário do funcionário? R$'))
if s >= 1250:
    ns1 = s * 1.1
    print('Você teve um aumento de 10% e agora seu salário é R${:.2f}'.format(ns1))
else:
    ns2 = s * 1.15
    print('Você teve um aumento de 15% e agora seu salário é R${:.2f}'.format(ns2))