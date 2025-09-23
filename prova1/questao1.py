def verifica(lista):
  n = len(lista)
  for i in range(n-1):
    if lista[i] > lista[i+1]:
      return False
  return True
