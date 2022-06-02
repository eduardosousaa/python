from random import choice

a1 = str(input('Nome aluno 1: '))
a2 = str(input('Nome aluno 2: '))
a3 = str(input('Nome aluno 3: '))
a4 = str(input('Nome aluno 4: '))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
