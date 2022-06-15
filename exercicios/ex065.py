r = 'S'
cont = tot = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
    cont += 1
    tot += n
    if n == 0:
        maior == n
        menor == n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Média é igual a {}'.format(tot/cont))
print('O maior número é o {} e o menor é o {}!'.format(maior, menor))