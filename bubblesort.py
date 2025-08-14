import random

qtd = int(input('Quantos números: '))
opcao = int(input('1-Digitar números\n2-Preencher automático\n'))
vetor = []

if opcao == 1:
  for i in range(0, qtd):
    vetor.append(int(input(f'Digite um número para a posição {i}: ')))
elif opcao == 2:
  vetor = random.sample(range(1, 50), qtd)
else:
  print('Opcão inválida!')

print('Vetor:')
for j in vetor:
        print(f'{j}', end=' ')

print('\nOrganizando o vetor em ordem crescente...')
while qtd > 1:
  #for i in vetor:
  #  print(f'{i}', end=' ')
  #print('\n')
  for i in range(0,qtd-1):
    if(vetor[i] > vetor[i+1]): #verifica se o elemento atual é maior que o próximo do vetor e faz a troca
        c = vetor[i]
        vetor[i] = vetor[i+1]
        vetor[i+1] = c
  qtd -= 1

print('Vetor organizado: ')
for i in vetor:
    print(f'{i}', end=' ')