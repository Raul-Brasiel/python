nome = input('Digite o seu nome completo: ').strip()

print(nome.upper())
print(nome.lower())

print(f'Número de letras: {len(nome.replace(' ', ''))}')

print(f'Número de letras do primeiro nome: {len(nome.split()[0])}')