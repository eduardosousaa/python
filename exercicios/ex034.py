salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    print('O seu salário é de {}R$, com o aumento passa a ser {}R$'.format(salario, salario + (salario*0.15)))
else:
    print('O seu salário é de {}R$, com o aumento passa a ser {}R$'.format(salario, salario + (salario*0.10)))