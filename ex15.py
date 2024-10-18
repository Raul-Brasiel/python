var = []

for cont in range(0,5):
    var.append(int(input(f'Digite um número para a posição {cont}: ')))
print(f'Você digitou {var}')

print(f'\nMaior: {max(var)} nas posições: ', end='')
for cont, v in enumerate(var):
    if v == max(var):
        print(f'{cont};',end='')

print(f'\nMenor: {min(var)} nas posições: ', end='')
for cont, v in enumerate(var):
    if v == min(var):
        print(f'{cont};',end='')