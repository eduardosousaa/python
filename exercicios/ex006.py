from cmath import sqrt


n1 = int(input('Digite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O dobro de {} vale {}. \nO triplo de {} é igual a {}. \nA raiz quadrada de {} é igual a {:0.2f}.'.format(n1, dobro, n1, triplo, n1, raiz))
