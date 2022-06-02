import math

b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))

hi = math.hypot(b, c)
print('A hipotenusa vai medir {:.2f}'.format(hi))







'''
b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))

a = (b**2 + c**2) ** (1/2)

print('O comprimento da hipotenusa é igual a {:.2f}'.format(a))'''