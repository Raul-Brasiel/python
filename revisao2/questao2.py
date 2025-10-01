def selection_sort_decrescente (v) :
    n = len (v)
    # percorre todas as posi ções do vetor
    for i in range (n - 1) :
        # assume que o maior est á na posi ção i
        indice_maior = i
        # procura o maior elemento na parte não ordenada
        for j in range (i + 1 , n) :
            if v[j] > v [indice_maior]:
                indice_maior = j
        # troca o maior encontrado com o elemento da posi ção i
        v [i] , v [indice_maior] = v [ indice_maior] , v [i]
    return v

# Exemplo de uso
valores = [72 , 12 , 62 , 69 , 27 , 67 , 41 , 56 , 33 , 74]
print (" Original :", valores)
print (" Ordenado em ordem decrescente :", selection_sort_decrescente (valores))