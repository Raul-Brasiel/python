import random
def organizar_lista(vetor, qtd):
  for j in range(qtd):
    naotrocou = True
    for i in range(0,qtd-1):
      if(vetor[i] > vetor[i+1]): #verifica se o elemento atual é maior que o próximo do vetor e faz a troca
          vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
          naotrocou = False
    if naotrocou:
      break
    print(f'Vetor: {vetor}')
  return vetor

qtd = int(input('Digite o tamanho da lista de números: '))
opcao = int(input('1-Digitar números\n2-Preencher automático\nEscolha: '))
vetor = []

if opcao == 1:
  for i in range(0, qtd):
    vetor.append(int(input(f'Digite um número para a posição {i}: ')))
elif opcao == 2:
  vetor = [random.randint(1, 50) for _ in range(qtd)]
else:
  print('Opcão inválida!')

print(f'Vetor desorganizado: {vetor}')

organizar_lista(vetor,qtd)