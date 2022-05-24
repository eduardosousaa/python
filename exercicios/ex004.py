N = input('Digite algo: ')

print('Tipo primitivo desse valor: {}'.format(type(N)))
print('Só tem espaços? {}'.format(N.isspace()))
print('É númerico? {}'.format(N.isnumeric()))
print('É alfabético? {}'.format(N.isalpha()))
print('É alfanumérico? {}'.format(N.isalnum()))
print('Está em maiúscula? {}'.format(N.isupper()))
print('Está em minúscula? {}'.format(N.isupper()))
print('Está capitalizada? {}'.format(N.istitle()))

