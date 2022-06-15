cont = 0
media = 0
idadevelho = 0
nomevelho = ''
mulheres20 = 0
for p in range(1, 5):
    print('\033[m''----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ''\033[32m')).strip()
    idade = int(input('\033[m''Idade: ''\033[32m'))
    sexo = str(input('\033[m''Sexo [M/F]: ''\033[32m')).strip().upper()
    cont += idade
    media = cont / 4
    if p == 1 and sexo in 'M':
        idadevelho = idade
        nomevelho = nome
    if idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        mulheres20 += 1
print('\033[m''A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velhor tem {} anos e se chama {}.'.format(idadevelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres20))
