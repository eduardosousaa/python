import random
sorteado = random.randint(0,5)
palpite = int(input('Adivinhe o número sorteado: '))
if palpite == sorteado:
    print('Parabéns, você acertou o número!')
else:
    print('Não foi dessa vez, tente novamente!')
