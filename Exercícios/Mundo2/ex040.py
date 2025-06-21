n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('O aluno está \033[31mREPROVADO')
elif 5 <= media <= 6.9:
    print('O aluno está em \033[33mRECUPERAÇÃO.')
elif (media >= 7):
    print('O aluno está \033[32mAPROVADO')
