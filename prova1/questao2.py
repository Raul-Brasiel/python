def bubble_sorte(array):
  tamanho = len(array)
  for i in range(tamanho):
    trocou = False
    for j in range(0, tamanho-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        trocou = True
    if trocou == False:
      break
