import random

def organizar_lista(vetor,qtd):
  for i in range(1, qtd):
    valor = vetor[i]
    j = i - 1
    
    while j >= 0 and vetor[j] > valor:
      vetor[j + 1] = vetor[j]
      j -= 1
    vetor[j + 1] = valor
    print(vetor)
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
