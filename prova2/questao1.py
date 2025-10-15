def buuble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def inserir(vetor, x):
    vetor.append(x)
    listas = buuble_sort(vetor)
    return listas

lista = [2, 5, 1, 3, 8]
lista_ordenada = inserir(lista, 9)
print(lista_ordenada)