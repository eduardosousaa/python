from turtle import st


num = int(input('Digite um número inteiro: '))
escolha = str(input('Escolha qual será a base de conversão: 1-Para binário, 2-Para octal, 3-Para hexadecimal '))
if escolha == 1:
    print('Sua escolha foi o binário!')
elif escolha == 2:
    print('Sua escolha foi o octal!')
elif escolha == 3:
    print('Sua escolha foi o hexadecimal!')
else:
    print('Valor errado, escolha outro!')