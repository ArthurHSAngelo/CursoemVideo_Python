nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é',nome.upper())
print('Seu nome em minúsculas é',nome.lower())
print('Seu nome tem ao todo', len(nome.replace(' ', '')), 'letras')
print('Seu primeiro nome é', nome.split()[0], 'e ele tem', len(nome.split() [0]), 'letras')