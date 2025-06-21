print('{:=^40}'.format(' LOJA DO PERIGO '))
preco = float(input('Qual é o preço das compras? R$'))
pagamento = int(input('''Escolha a FORMA DE PAGAMENTO:
\033[35m[ 1 ]\033[m à vista\033[34m dinheiro/cheque\033[m
\033[35m[ 2 ]\033[m à vista\033[34m cartão\033[m
\033[35m[ 3 ]\033[m parcelado \033[34m2x no cartão\033[m 
\033[35m[ 4 ]\033[m parcelado \033[34m3x ou mais no cartão\033[m 
Qual você vai escolher? '''))
if pagamento == 1:
    print('Pagando à vista no dinheiro ou cheque, sua compra de {:.2f} vai custar: R${:.2f}'.format(preco, preco - (preco * 10 / 100)))
elif pagamento == 2:
    print('Pagando à vista no cartão, sua compra de {:.2f} vai custar: R${:.2f}'.format(preco, preco - (preco * 5 /100)))
elif pagamento == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra será o mesmo valor de R${:.2f}'.format(preco))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = preco + (preco * 20 /100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valor/parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
else:
    print('\033[31mEscolha um número válido, entre 1 a 4')