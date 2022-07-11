from ast import Num


num = cont = qtd = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont +=1
    qtd += num
print('Você digitou {} numeros e a soma entre eles foi de {}'.format(cont, qtd))