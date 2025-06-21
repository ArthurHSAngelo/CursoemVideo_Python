d = int(input('Quantos dias o carro foram alugados? '))
km = float(input('Quantos Km foram rodados? '))
total = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
