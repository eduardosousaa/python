from random import randint

recebe = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print('Os valores sorteados são: ', end='')
for c in recebe:
    print(f'{c} ', end='')
print(f'\nMaior número: {max(recebe)}\nMenor número: {min(recebe)}')
 
