from random import randint
from time import sleep
sorteado = randint(0,5)
print('--' * 20)
print('          Jogo de adivinhação')
print('--' * 20)
palpite = int(input('Adivinhe o número sorteado: '))
print('PROCESSANDO...')
sleep(3)
if palpite == sorteado:
    print('Parabéns, você acertou o número!')
else:
    print('Não foi dessa vez, tente novamente!')
    print('Você escolheu o número {}, mais o sorteado foi o número {}.'.format(palpite, sorteado))
