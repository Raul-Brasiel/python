def merge_sort(lista):
    # Caso base: lista com 1 ou 0 elementos já está ordenada
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas metades
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Chama recursivamente o merge_sort nas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Combina as duas metades ordenadas
    return merge(esquerda, direita)


def merge(esquerda, direita):
    lista_ordenada = []
    i = j = 0

    # Intercala os elementos das duas listas em ordem crescente
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    while i < len(esquerda):
        lista_ordenada.append(esquerda[i])
        i += 1

    while j < len(direita):
        lista_ordenada.append(direita[j])
        j += 1

    return lista_ordenada


# Exemplo de uso
valores = [38, 27, 43, 3, 9, 82, 10]
ordenado = merge_sort(valores)
print("Lista original:", valores)
print("Lista ordenada:", ordenado)