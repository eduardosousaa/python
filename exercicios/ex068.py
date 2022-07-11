from random import randint
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    resultado = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer [P/I]: ')).upper().strip()[0]
        print('=-' * 15)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}. ', end='')
    print('DEU PAR' if resultado % 2 == 0  else 'DEU ÍMPAR')
    if tipo == 'P':
        if resultado % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        if resultado % 2 == 1:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {cont} vezes!')

    