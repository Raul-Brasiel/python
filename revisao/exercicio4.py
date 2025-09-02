# Escreva uma versão recursiva do algoritmo de ordenação por seleção.

def organizar_lista_recursivo(vetor, inicio=0):
    if inicio >= len(vetor) - 1:
        return vetor

    index_menor = inicio
    for j in range(inicio + 1, len(vetor)):
        if vetor[j] < vetor[index_menor]:
            index_menor = j

    if index_menor != inicio:
        vetor.insert(inicio, vetor[index_menor])
        vetor.pop(index_menor + 1)
        print(vetor)

    return organizar_lista_recursivo(vetor, inicio + 1)

vetor = [5, 2, 9, 1, 5, 6]
print(f'Vetor: {vetor}')
print('Ordenando...')
organizar_lista_recursivo(vetor)
print(f'Lista final: {vetor}')