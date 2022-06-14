num = int(input('Digite um número inteiro: '))
print('''Escolha qual será a base de conversão: 
[1] - Para binário
[2] - Para octal
[3] - Para hexadecimal''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} comvertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} comvertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} comvertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Valor inválido, tente novamente!')