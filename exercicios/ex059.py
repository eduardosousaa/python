solicitado = 0
while solicitado != 4:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite um valor: '))
    maior = 0
    while solicitado != 5:
        print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
        solicitado = int(input('Qual a operação solicitada: '))
        if solicitado == 1:
            print('A somo de {} + {} é igual a {}!'.format(valor1, valor2, valor1 + valor2))
        elif solicitado == 2:
            print('A multiplicação de {} * {} é igual a {}!'.format(valor1, valor2, valor1*valor2))
        elif solicitado == 3:
            if valor1 > valor2:
                maior = valor1
            else:
                maior = valor2
            print('O mais valor digitado foi o {}!'.format(maior))
