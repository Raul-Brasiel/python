import random
vetor = random.sample(range(1,99),5)
qtd = len(vetor)
print(f'Tamanho do vetor: {qtd}')

print('\nOrganizando vetor: ')
while qtd > 0:
  for i in vetor:
    print(f'{i}', end=' ')
  print('\n')
  for i in range(0,qtd-1):
    if(vetor[i] > vetor[i+1]):
      c = vetor[i]
      vetor[i] = vetor[i+1]
      vetor[i+1] = c
  qtd-=1
print('Vetor organizado: ')
for i in vetor:
  print(f'{i}', end=' ')