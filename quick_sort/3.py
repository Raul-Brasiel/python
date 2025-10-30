def qsrt(array, left, right):
    """
    Função principal do QuickSort (Ordem Decrescente)
    """
    print(f"QSRT(L={left}, R={right})")

    # A ÚNICA CORREÇÃO NECESSÁRIA: O CASO BASE
    if left < right:
        size = right - left + 1
        if size == 2:
            print(f"  -> Subvetor de 2 elementos {array[left:right+1]}. Particionando...")
        
        j = partition(array, left, right) 

        print(f"  -> Chamando recursão Esquerda: QSRT(L={left}, R={j-1})")
        qsrt(array, left, j - 1)
        
        print(f"  -> Chamando recursão Direita: QSRT(L={j+1}, R={right})")
        qsrt(array, j + 1, right)
    
    elif left == right:
        print(f"  -> Caso Base (1 elemento): L={left}, R={right}. (Subvetor: [{array[left]}]). Nada a fazer.")
    else: 
        print(f"  -> Caso Base (0 elementos): L={left}, R={right}. (Subvetor vazio). Nada a fazer.")

def partition(array, left, right):
    """
    Sua função de partição original (Lomuto para ordem DECRESCENTE)
    """
    pivot = array[right] 
    i = left - 1
    
    print(f"    PARTITION(L={left}, R={right}, PIVOT={pivot}) Array: {array[left:right+1]}")

    for j in range(left, right):
        # LÓGICA ORIGINAL (Correta para decrescente):
        if array[j] >= pivot: 
            i += 1
            array[i], array[j] = array[j], array[i]
    
    # Coloca o pivô no lugar
    array[i + 1], array[right] = array[right], array[i + 1]
    
    pivot_index = i + 1
    print(f"    -> PIVÔ NO ÍNDICE: {pivot_index}. Array após part.: {array[left:right+1]}")
    return pivot_index

# --- Função auxiliar para rodar os testes ---
def run_test(test_name, arr, expected):
    print(f"\n--- INICIANDO TESTE: {test_name} ---")
    print(f"Original: {arr}")
    
    arr_copy = list(arr) 
    
    qsrt(arr_copy, 0, len(arr_copy) - 1)
    
    print(f"Resultado:  {arr_copy}")
    print(f"Esperado:   {expected}")
    # Usamos assert para garantir que o teste passou
    assert arr_copy == expected
    print("Status: OK")
    print("--------------------------------------")

# --- Casos de Teste (Ordem Decrescente) ---
if __name__ == "__main__":
    
    # Teste 1: Vetor pequeno (2 elementos, já ordenado)
    run_test("Vetor pequeno (Já ordenado Decr.)", [5, 2], [5, 2])
    
    # Teste 1b: Vetor pequeno (2 elementos, invertido)
    run_test("Vetor pequeno (Invertido)", [2, 5], [5, 2])

    # Teste 2: Vetor padrão
    run_test("Vetor padrão", [8, 3, 1, 6, 4, 10, 2], [10, 8, 6, 4, 3, 2, 1])
    
    # Teste 3: Vetor vazio
    run_test("Vetor vazio", [], [])

    # Teste 4: Vetor com 1 elemento
    run_test("Vetor com 1 elemento", [5], [5])
    
    # Teste 5: Vetor já ordenado (decrescente)
    run_test("Vetor já ordenado (desc)", [5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
    
    # Teste 6: Vetor em ordem inversa (crescente)
    run_test("Vetor ordenado (asc)", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

    # Teste 7: Vetor com elementos duplicados
    run_test("Vetor com duplicatas", [4, 2, 5, 2, 4, 5, 1], [5, 5, 4, 4, 2, 2, 1])
# A função original qsrt não tem um "caso base" para parar a recursão. Ela continuará chamando a si mesma mesmo para subvetores vazios (left > right), o que causará um IndexError na função partition (ao tentar acessar array[right]). A correção é adicionar um if left < right: no início da função qsrt.
