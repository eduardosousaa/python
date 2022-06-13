valor = float(input('\033[1;32;40m''Digite o valor do produto: ''\033[m'))
print('**' * 20)
print('1 - À vista dinheiro ou cheque.')
print('2 - À vista no cartão.')
print('3 - Em até 2x no cartão.')
print('4 - Em mais 3x ou mais.')
print('**' * 20)
pagamento = int(input('\033[1;32;40m''Digite de acordo com a tabela a cima a forma de pagamento: ''\033[m'))
if pagamento == 1:
    print('Valor a ser pago é de R${:.2f}'.format(valor - (valor * 0.10)))
elif pagamento == 2:
    print('Valor a ser pago é de R${:.2f}'.format(valor - (valor * 0.5)))
elif pagamento == 3:
    print('Valor a ser pago é de R${:.2f}'.format(valor))
elif pagamento == 4:
    print('Valor a ser pago é de R${:.2f}'.format(valor + (valor * 0.20)))
else:
    print('Forma de pagamento invávilda, tente novamente!')