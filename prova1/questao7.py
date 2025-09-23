def organizar_lista_recursivo(vetor, qtd=None):
    if qtd is None:
        qtd = len(vetor)
    if qtd <= 1:
        return vetor
      
    organizar_lista_recursivo(vetor, qtd - 1)
  
    valor = vetor[qtd - 1]
    j = qtd - 2
    while j >= 0 and vetor[j] > valor:
        vetor[j + 1] = vetor[j]
        j -= 1
    vetor[j + 1] = valor
    print(vetor)
    return vetor
