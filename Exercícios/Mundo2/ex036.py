valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
ano = int(input('Em quantos anos vai ser o financiamento? '))
prazo = ano * 12
valor_prestacao = valor_casa / prazo

if valor_prestacao <= (salario * 30 /100):
    print('\033[32m EMPRÉSTIMO APROVADO!\033[m')
    print('\033[34m O valor da sua parcela mensal é de\033[m \033[35mR${:.2f}\033[m \033[34mpara ser pago em {} meses\033[m'.format(valor_prestacao,prazo))
    print('\033[34m E também a parcela máxima que você pode pagar é de\033[m \033[35mR${:.2f} \033[m'.format(salario * 30 / 100))
else:
    print('\033[31m EMPRÉSTIMO NEGADO! \033[m')
    print('\033[33m Valor da parcela é maior do que 30% do seu salário \033[m')
    print('\033[34m O valor da parcela é\033[m \033[35mR${:.2f} \033[m'.format(valor_prestacao))
    print('\033[34m A parcela máxima para você seria de\033[m \033[35mR${:.2f} \033[m'.format(salario * 30 / 100))
