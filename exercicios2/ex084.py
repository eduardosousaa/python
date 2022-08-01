lista1 = []
lista2 = []
cont = 0
while True:
    lista1(str(input('Digite uma pessoa: ')))
    lista2(int(input('Digite o seu peso: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {cont} pessoas')