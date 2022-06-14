frase = str(input('Digite uma frase: ')).replace(' ', '')
comprimento = len(frase)
for c in range(frase[comprimento], 0, -1):
    if c == frase:
        print('A frase é um palíndromo!')
    else:
        print('A frase não é um palíndromo!')