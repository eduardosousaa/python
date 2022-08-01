lista = []
for c in range(5):
    num = int(input(f'Digite um valor na posição {c}: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
        pos += 1

print(f'Lista ordenada: {lista}')