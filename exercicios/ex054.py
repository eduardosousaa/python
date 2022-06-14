from datetime import date
data = date.today().year
contmaior = 0
contmenor = 0
for idade in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    if data - nasc > 21:
        contmaior += 1
    else:
        contmenor += 1
print('Existem {} pessoa(s) que já atingiram a maioridade.'.format(contmaior))
print('Existem {} pessoa(s) que ainda não atingiram a maioridade.'.format(contmenor))