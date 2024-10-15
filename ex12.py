fatorial = n = int(input('Digite um número: '))

i = 1
while i < n:
    fatorial = fatorial*i
    i+=1
print(f'O fatorial de {n} é {fatorial}')