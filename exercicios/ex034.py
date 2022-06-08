salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    print('O seu salário é de R$ {:.2f}, com o aumento passa a ser R$ {:.2f}'.t(salario, salario + (salario*0.15)))
else:
    print('O seu salário é de R$ {:.2f}, com o aumento passa a ser R$ {:.2f}'.format(salario, salario + (salario*0.10)))