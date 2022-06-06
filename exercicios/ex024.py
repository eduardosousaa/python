cidade = str(input('Digite o nome da sua cidade: ')).strip()

dividido = cidade.split()
dividido = dividido[0]
print('santo' in dividido.lower())