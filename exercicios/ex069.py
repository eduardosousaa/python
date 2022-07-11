r = 'S'
maioridade = 0
qtdhomens = 0
qtdmulhures20 = 0
while r == 'S':
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        qtdhomens += 1
    if sexo == 'F' and idade < 20:
        qtdmulhures20 += 1
print(f'{maioridade} pessoas tem mais de 18 anos.')
print(f'{qtdhomens} homens foram cadastrados.')
print(f'{qtdmulhures20} mulhures tem menos de 20 anos.')