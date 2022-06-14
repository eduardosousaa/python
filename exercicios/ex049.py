num = int(input('Digite um número: '))
cont = 0
for c in range(0, 10):
    cont += 1
    print('{} * {} = {}'.format(num, cont, num*cont))