valores = list()
while True:
    n = int(input('Digite valores: '))
    if n not in valores:
        valores.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor já está na lista...')
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
