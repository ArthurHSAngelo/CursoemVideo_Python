from datetime import date
ano_atual = date.today().year
contmenor = 0
contmaior = 0
for i in range (1,8):
    ano_nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(contmaior))
print('E também tivemos {} pessoas menores de idade'.format(contmenor))
