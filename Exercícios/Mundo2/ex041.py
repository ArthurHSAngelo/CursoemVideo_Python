from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A sua categoria é: MIRIM')
elif 9 < idade <= 14:
    print('A sua categoria é: INFANTIL')
elif 14 < idade <= 19:
    print('A sua categoria é: JUNIOR')
elif 19 < idade <= 25:
    print('A sua categoria é: SÊNIOR')
else:
    print('A sua categoria é: MASTER')
