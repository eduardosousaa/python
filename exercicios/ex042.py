print('--' * 20)
print('         Analisador de triângulos')
print('--' * 20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem sim formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
if r1 == r2 and r3:
    print('TRIÂNGULO EQUILÁTERO')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('TRIÂNGULO ISÓSCELES')
elif r1 != r2 and r2 != r3 and r3 != r1:
    print('TRIÂNGULO ESCALENO')