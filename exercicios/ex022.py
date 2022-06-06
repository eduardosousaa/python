nome = str(input('Digite o seu nome completo: '))

print('Analisando o seu nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

nome1 = nome.replace(" ", "")
print('Seu nome tem ao todo {} letras'.format(len(nome1)))

dividido = nome.split()
dividido = dividido[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido, len(dividido)))