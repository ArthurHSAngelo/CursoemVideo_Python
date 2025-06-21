soma_idade = 0
homem_mais_velho = 0
nome_homem = 'a'
soma_mulheres = 0
for p in range (1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem = nome

    if sexo == 'F':
        if idade < 20:
            soma_mulheres += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_mais_velho, nome_homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(soma_mulheres))
