for c in range(0, 2):
    peso = float(input('Digite o peso em kg: '))
    maior = peso[0]
    menor = peso[0]
    if peso[1] > peso[0]:
        maior = peso[1]
        menor = peso[0]
print('Maior = {}'.format(maior))
print('Menor = {}'.format(menor))