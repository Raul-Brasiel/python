#Escreva uma função que permute os elementos de um vetor inteiro v[0..n-1] 
# de modo que eles fiquem em ordem decrescente. Inspire-se no algoritmo Selectionsort.

def ordenar_decrescente(vetor):
    n = len(vetor)
    for i in range(n):
        index_maior = i
        for j in range(i + 1, n):
            if vetor[j] > vetor[index_maior]:
                index_maior = j
        vetor[i], vetor[index_maior] = vetor[index_maior], vetor[i]
    return vetor

vetor = [5, 2, 9, 1, 5, 6]
print(f'Vetor: {vetor}')
print('Ordenando...')
ordenar_decrescente(vetor)
print(f'Lista final: {vetor}')