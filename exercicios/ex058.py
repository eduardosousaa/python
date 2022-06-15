from random import randint
from time import sleep
sorteando = randint(0,10)
palpite = 0
cont = 0
print('--' * 20)
print('          Jogo de adivinhação')
print('--' * 20)
while sorteando != palpite:
    palpite = int(input('Adivinhe o número sorteado: '))
    print('PROCESSANDO...')
    sleep(1)
    cont += 1
print('Você acertou o número sorteado em {} tentativa(s)!'.format(cont))

