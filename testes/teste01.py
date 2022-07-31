lista = []
maior = menor = 0
for c in range(5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores: {lista}')
print(f'Maior: {maior} na posição ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end='')
print()
print(f'Menor: {menor} na posição: ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end='')