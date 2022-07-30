valores = (int(input(f'Digite um valor: '))), (int(input(f'Digite outro valor: '))), (int(input(f'Digite outro valor: '))), (int(input(f'Digite outro valor: ')))

print(valores)

print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3)} posição')
else:
    print('O valor 3 não foi digitado!')
print(f'Os valores pares digitados foram: ', end='')
for c in valores:
    if c % 2 == 0:
        print(f'{c} ', end='')
