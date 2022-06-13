valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Em quantos anos você deseja pagar: '))

qtd = (valorcasa / anos) / 12
prestacao = salario * 0.30
if qtd < prestacao:
    print('\033[1;32;40m''Emprestimo bancário aprovado!''\033[m')
else:
    print('\033[1;31;40m''Emprestimo bancário negado!''\033[m')
print('Valor da prestação é de R${:.2f}'.format(prestacao))
print('Valor a ser pago por mês é de R${:.2f}'.format(qtd))