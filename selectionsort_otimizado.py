import random
def organizar_lista(vetor,qtd):
  valor_menor = max(vetor)+1
  print('Organizando o vetor...')
  for i in range(0,qtd):
    trocou = False
    for j in range(i+1,qtd):
      if vetor[j] < vetor[i]:
        if vetor[j] < valor_menor:
          index_menor = j
          valor_menor = vetor[j]
          trocou = True
    if trocou:
      vetor.insert(i,vetor[index_menor])
      vetor.pop(index_menor+1)
      valor_menor = max(vetor)+1
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