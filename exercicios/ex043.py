peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em M: '))
imc = peso / (altura **2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MÓRBIDA')