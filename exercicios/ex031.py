distancia = float(input('Digite a distância percorrida em km: '))
if distancia <= 200:
    print('O preço da passagem foi de {}'.format(distancia*0.50))
else:
    print('O preço da passagem foi de {}'.format(distancia*0.45))