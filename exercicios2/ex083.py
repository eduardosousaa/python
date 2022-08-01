from cmath import e


s = str(input('Digite um expressão: '))
lista = []
for e in s:
    if e == '(':
        lista.append('(')
    elif e == ')':
        if len(lista) < 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')