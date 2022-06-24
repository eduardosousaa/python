print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➝  '.format(termo), end='')
    cont += 1
    termo += razao
print('FIM!')


    