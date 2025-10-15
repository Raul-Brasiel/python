def selection_sort_decrescente(v):
    n = len(v)
    for i in range (n):
        indice_maior = i
        for j in range (i+1, n) :
            if v[j] > v[indice_maior]:
                indice_maior = j
        v[i], v[indice_maior] = v[indice_maior] , v[i]
    return v

lista = [11,4,30,22,7,26]
selection_sort_decrescente(lista)
print(lista)