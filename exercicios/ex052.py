for c in range(0, 2):
    num = int(input('Digite um número: '))
    if num > 1 and num % 1 == 0 and num % num == 0:
        print('O número {} é primo!'.format(num))
    else:
        print('O número {} não é primo!'.format(num))