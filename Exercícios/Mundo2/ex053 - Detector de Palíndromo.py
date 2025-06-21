palavra = str(input('Digite uma frase: ')).upper().strip()
palavras = palavra.split()
junto = ''.join(palavras)
palindromo = junto[::-1]
'''for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, palindromo))
if junto == palindromo:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
