from datetime import date
nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Qual é o seu sexo? (mas ou fem):'))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano_atual))
if sexo == 'mas':
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        ano = ano_atual + (18-idade)
        print('Seu alistamento será em {}.'.format(ano))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        ano = ano_atual - (idade - 18)
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Você sendo do sexo feminino não precisa fazer o alistamento militar obrigatório.')
