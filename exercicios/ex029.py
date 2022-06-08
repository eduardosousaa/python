velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print('Valor da multa é de {}R$'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija com segurança!')