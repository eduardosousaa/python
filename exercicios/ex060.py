n = int(input('Digite um número para calcular a fatorial: '))
c = n
m = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    m *= c
    c -= 1
print('{}'.format(m), end='')

'''
n = int(input('Digite um número para calcular a fatorial: '))
r = 1 
for c in range(1, n+1):
    r *= c
print('O fatorial de {} é igual a {}'.format(n, r))
'''