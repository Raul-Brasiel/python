def insertion_sort_count(array):
    n = len(array)
    copias = 0  # contador de cópias dentro do while

    for i in range(1, n):
        chave = array[i]
        j = i - 1

        # desloca elementos maiores que a chave
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]  # cópia do elemento
            copias += 1
            j -= 1

        array[j + 1] = chave  # inserção da chave na posição correta

    return array, copias


# Testando com o array da questão
valores = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
ordenado, total_copias = insertion_sort_count(valores)

print("Vetor ordenado:", ordenado)
print("Total de cópias dentro do while:", total_copias)