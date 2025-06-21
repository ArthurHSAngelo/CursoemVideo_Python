num = int(input('Digite um número inteiro: '))
opcao = str(input('''Escolha uma das bases para conversão: 
\033[34m[ 1 ]\033[m converter para BINÁRIO
\033[34m[ 2 ]\033[m converter para OCTAL
\033[34m[ 3 ]\033[m converter para HEXADECIMAL
Sua opção: '''))
if opcao == '1':
    print('O número {} convertido para BINÁRIO, seria {}'.format(num, bin(num)[2:]))
elif opcao == '2':
    print('O número {} convertido para OCTAL, seria {}'.format(num, oct(num)[2:]))
elif opcao == '3':
    print('O número {} convertido para HEXADECIMAL, seria {}'.format(num,hex(num)[2:]))
else:
    print('Tinha que ser um número de 1 a 3')
