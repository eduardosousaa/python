lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    continuar = str(input('Quer continuar: [S/N]')).upper()
    if continuar == 'N':
        break
lista.sort()
print(f'Lista: {lista}')