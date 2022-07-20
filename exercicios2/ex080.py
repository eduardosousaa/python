lista = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break
        pos += 1
print(f'Lista: {lista}')
