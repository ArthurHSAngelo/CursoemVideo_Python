real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.51
euro = real / 6.02
iene = real / 0.038
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥${:.2f}'.format(real, iene))
print('OBS: valores de acordo com a cotação do dia 09/08/2024')
