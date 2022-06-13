from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
sorteado = choice(lista)
print('\033[1;36;40m''Vamos jogar Pedra, Papel, Tesoura!''\033[m')
sleep(2)
print('\033[1;33;40m''JOKENPÔ''\033[m')
jogada = str(input('\033[1;33;40m''Escolha uma das opções: '))
print('PROCESSANDO RESULTADO...''\033[40m')
sleep(3)
if jogada == sorteado:
    print('\033[1;36;40m''Empate, jogue novamente!''\033[m')
elif jogada == 'Pedra' and sorteado == 'Tesoura' or jogada == 'Tesoura' and sorteado == 'Papel' or jogada == 'Papel' and sorteado == 'Pedra':
    print('\033[1;32;40m''Você ganhou! {} ganha de {}''\033[m'.format(jogada, sorteado))
else:
    print('\033[1;31;40m''Você perdeu! {} perde para {}''\033[m'.format(jogada, sorteado))