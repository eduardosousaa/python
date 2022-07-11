r = 'S'
cont = contpreco = menor = c = 0
while r == 'S':
    nome = input('Nome do produto: ')
    preco = int(input('Preço do produto R$: '))
    r = input('Quer continuar? [S/N]: ').upper().strip()
    cont += preco
    c += 1
    if preco > 1000:
        contpreco += 1
    if c == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
print(f'Total gasto foi de R$ {cont}')
print(f'Tem {contpreco} produtos acima de R$ 1000')
print(f'O produto mais barato foi o de R$ {menor}.')