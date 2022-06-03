nome = str(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())

nome1 = nome.replace(" ", "")
print(len(nome1))

dividido = nome.split()
dividido = dividido[0]
print(len(dividido))