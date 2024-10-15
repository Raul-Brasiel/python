import random

t = random.sample(range(1, 11), 5)

print('Valores sorteados: ', end='')
for i in t:
    print(f'{i}', end=' ')
print(f'\nMaior: {max(t)}')
print(f'Menor: {min(t)}')