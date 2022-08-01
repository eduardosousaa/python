lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Foram digitados {cont} números na lista')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
