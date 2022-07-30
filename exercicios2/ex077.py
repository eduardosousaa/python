tupla = ('Carro', 'Melancia', 'Futebol', 'Santos', 'Neymar')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end='')