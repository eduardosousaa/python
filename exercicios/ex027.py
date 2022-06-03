nome = str(input('Digite o seu nome completo: '))

primeiro = nome.split()
primeiro = primeiro[0]
print(primeiro)

ultimo = primeiro[::]
print(ultimo)