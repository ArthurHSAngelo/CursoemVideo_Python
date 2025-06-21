v = float(input('Qual é a velocidade atual de um carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    m = (v - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')