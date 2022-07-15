tupla = 'zero', 'um', 'dois', 'três', 'quatro'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {tupla[num]}') 