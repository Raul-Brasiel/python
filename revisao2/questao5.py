def insertion_sort_decrescente(array):
    # Percorre do segundo elemento até o fim
    for i in range(1, len(array)):
        chave = array[i]        # elemento a ser inserido
        j = i - 1

        # Move elementos menores que a chave uma posição à frente
        while j >= 0 and array[j] < chave:
            array[j + 1] = array[j]
            j -= 1

        # Insere a chave na posição correta
        array[j + 1] = chave

    return array

# Exemplo de uso
valores = [5, 2, 9, 1, 7]
print("Original:", valores)
print("Ordenado (decrescente):", insertion_sort_decrescente(valores))