distancia = float(input('Digite a distância percorrida em km: '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    print('O preço da passagem foi de R${:.2f}'.format(distancia*0.50))
else:
    print('E o preço da passagem será de R${:.2f}'.format(distancia*0.45))