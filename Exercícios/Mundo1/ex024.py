cidade = str(input('Em que cidade você nasceu? ')).strip()
print('A sua cidade começa com a palavra "Santo"?')
print(cidade[:5].upper() == 'SANTO')