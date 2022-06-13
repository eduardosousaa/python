from datetime import date
nasc = int(input('Digite a data de nascimento: '))
data = date.today().year - nasc
if data <= 9:
    print('MIRIM')
elif data > 9 and data <= 14:
    print('INFANTIL')
elif data > 14 and data <= 19:
    print('JUNIOR')
elif data == 20:
    print('SÊNIOR')
else:
    print('MASTER')
print('Ano = {}'.format(data))