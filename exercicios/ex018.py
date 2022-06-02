from math import sin, cos, tan, radians
angulo = int(input('Digite o ângulo: ')) 

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangnte de {:.2f}'.format(angulo, tangente))