n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 > n2 and n2 < n3:
    print('{} é maior'.format(n1))
    print('{} é menor'.format(n2))
elif n2 > n1 and n3 < n1:
    print('{} é maior'.format(n2))
    print('{} é menor'.format(n3))
elif n3 > n1 and n1 < n2:
    print('{} é maior'.format(n3))
    print('{} é menor'.format(n1))