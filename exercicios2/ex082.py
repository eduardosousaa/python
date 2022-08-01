lista1 = []
lista2 = []
lista3 = []

while True:
    lista1.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar [S/N]: ')).upper()
    if continuar == 'N':
        break
for c in lista1:
    if c % 2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)

print(f'Lista completa: {lista1}')
print(f'Lista com os pares: {lista2}')
print(f'Lista com os ímpares: {lista3}')
