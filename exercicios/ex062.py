print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ➝  '.format(termo), end='')
        cont += 1
        termo += razao
    print('PAUSA!')
    mais = int(input('Quantos números você quer digitar a mais? '))
print('Progressão finalizada com {} termos!'.format(total))