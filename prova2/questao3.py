def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        chave_string = array[i]
        j = i - 1
        while j >= 0 and len(array[j]) > len(chave_string):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave_string
    return array

lista = ['Ana', 'Roberto', 'Beatriz', 'João', 'Clara', 'Lu']
lista_ordenada = insertion_sort(lista)
print(lista_ordenada)