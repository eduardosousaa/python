while True:
    print('-=' * 20)
    tab = int(input('Quer ver a tabuada de que número: '))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab * c}')
print('Fim')