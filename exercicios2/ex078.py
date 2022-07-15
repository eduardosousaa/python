lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=' * 30)
print(f'Você digitou os valores {lista}')
print('-=' * 30)
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()