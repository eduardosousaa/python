from ntpath import join


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
tamanho = len(junto)
inverso = ''
#inverso = junto[::-1]
for letra in range(tamanho - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {}, temos um palíndromo!'.format(junto, inverso))
else:
    print('O inverso de {} é {}, não é um palíndromo!'.format(junto, inverso))