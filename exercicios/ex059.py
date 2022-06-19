from time import sleep
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
solicitado = 0
while solicitado != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    solicitado = int(input('Qual a operação solicitada: '))
    if solicitado == 1:
        print('A somo de {} + {} é igual a {}!'.format(valor1, valor2, valor1 + valor2))
        print('-==' * 10)
    elif solicitado == 2:
        print('A multiplicação de {} * {} é igual a {}!'.format(valor1, valor2, valor1*valor2))
        print('-==' * 10)
    elif solicitado == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor digitado foi o {}!'.format(valor1, valor2, maior))
        print('-==' * 10)
    elif solicitado == 4:
            print('Digite os números novamente...')
            valor1 = int(input('Digite um valor: '))
            valor2 = int(input('Digite um valor: '))
    elif solicitado == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    print('-==' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')