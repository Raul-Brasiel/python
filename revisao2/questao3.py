def selection_sort_parcial(v, trocas):
    n = len(v)
    contador = 0

    for i in range(n - 1):
        # encontra o índice do menor elemento
        indice_menor = i
        for j in range(i + 1, n):
            if v[j] < v[indice_menor]:
                indice_menor = j

        # faz a troca
        v[i], v[indice_menor] = v[indice_menor], v[i]
        contador += 1

        # para quando atingir o número desejado de trocas
        if contador == trocas:
            break

    return v


# Exemplo da questão
valores = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
resultado = selection_sort_parcial(valores, 4)

print("Vetor após 4 trocas:", resultado)