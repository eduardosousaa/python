largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem dimensão de {} x {} e a sua área é de {}m².'.format(largura, altura, area))
print('A quantidade de tinta necessária para pintar a perede é de {} litros'.format(tinta))
