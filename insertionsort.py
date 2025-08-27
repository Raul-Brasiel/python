import random

def organizar_lista(vetor,qtd):
  for i in range(1, qtd):
    index = -1
    for j in range(i,-1,-1):
      if vetor[i] < vetor[j]:
        index = j
    if index > -1:
      valor = vetor[i]
      vetor.pop(i)
      vetor.insert(index, valor)
      print(f'{vetor}')
  return vetor

while True:
  qtd = int(input('Digite o tamanho da lista de números: '))
  opcao = int(input('1-Digitar números\n2-Preencher automático\nEscolha: '))
  vetor = []

  if opcao == 1 or opcao == 2:
    if opcao == 1:
      for i in range(0, qtd):
        vetor.append(int(input(f'Digite um número para a posição {i}: ')))
    else:
      vetor = [random.randint(1, 50) for _ in range(qtd)]
    
    print(f'Vetor desorganizado: {vetor}')
    print(f'Vetor organizado: {organizar_lista(vetor,qtd)}')
    break
  else:
    print('Opcão inválida!')