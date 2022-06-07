velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    print('Valor da multa é de {}R$'.format((velocidade-80)*7))