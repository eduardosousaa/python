from ast import Num


num = cont = qtd = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont +=1
    qtd += num
print(cont - 1)
print(qtd - 999)