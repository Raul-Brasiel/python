def bubble_sort_string (s) :
    # transforma a string em lista de caracteres
    v = list(s)
    n = len (v)
    # algoritmo bubble sort
    for i in range (n - 1) :
        for j in range (n - 1 - i) :
            if v[j] > v [ j + 1]:
                v [j] , v [j + 1] = v [j + 1] , v [j]
    # junta de volta em string
    return "".join (v)

# Exemplo de uso
texto = " algoritmo "
resultado = bubble_sort_string (texto)
print (" Original :", texto)
print (" Ordenado :", resultado)