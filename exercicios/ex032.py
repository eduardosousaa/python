ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))