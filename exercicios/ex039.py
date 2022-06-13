from datetime import date
nasc = int(input('Qual a sua data de nascimento: '))
ano = date.today().year - nasc
if ano < 18:
    print('Você ainda vai se alistar!')
    print('Faltam {} ano(s) para o seu alistamento!'.format(18-ano))
elif ano == 18:
    print('Você já está no período de alistamento!')
elif ano > 18:
    print('Você já passou do tempo de alistamento!')
    print('Já se passaram {} ano(s) do seu período de alistamento!'.format(ano-18))
