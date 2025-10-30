def sep ( array , left , right ) :
    print(f"    SEP(L={left}, R={right}) - Array: {array[left:right+1]}")
    
    # O pivô é o valor em array[right]
    # Nota: O valor em array[right] PODE MUDAR durante o loop
    print(f"    -> Pivô inicial (valor): {array[right]}")
    
    j = right
    # Loop de 'right-1' descendo até 'left'
    for i in range ( right - 1 , left - 1 , -1) :
        
        # Compara o elemento atual com o elemento NA ÚLTIMA POSIÇÃO (que pode ter mudado)
        print(f"      i={i}. Compara array[{i}] ({array[i]}) > array[{right}] ({array[right]})")
        
        if array [ i ] > array [ right ]:
            print(f"        -> TROCA: array[{i}] ({array[i]}) <-> array[{right}] ({array[right]})")
            
            # Executa a troca
            array [ i ] , array [ right ] = array [ right ] , array [ i ]
            j = i # Atualiza o índice 'j'
            
            print(f"        -> Array agora: {array[left:right+1]}, j={j}")
        
    print(f"    -> SEP Retornando j={j}")
    return j

def quicksort(array, left, right):
    print(f"QUICKSORT(L={left}, R={right})")
    
    if left < right:
        # Chama a sua função de partição
        pivot_index = sep(array, left, right)
        
        print(f"  -> Pivô final no índice: {pivot_index}")

        # Chamadas recursivas
        print(f"  -> Chamando Esq: QUICKSORT(L={left}, R={pivot_index - 1})")
        quicksort(array, left, pivot_index - 1)
        
        print(f"  -> Chamando Dir: QUICKSORT(L={pivot_index + 1}, R={right})")
        quicksort(array, pivot_index + 1, right)
    
    # Prints para os casos base (o que acontece com subvetores pequenos)
    elif left == right:
        print(f"  -> Caso Base (1 elemento): L={left}, R={right}. (Subvetor: [{array[left]}]).")
    else: 
        print(f"  -> Caso Base (0 elementos): L={left}, R={right}. (Subvetor vazio).")

# --- Função auxiliar para rodar os testes ---
def run_test(test_name, arr, expected_asc):
    print(f"\n--- INICIANDO TESTE: {test_name} ---")
    print(f"Original: {arr}")
    
    arr_copy = list(arr) 
    
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    
    print("\n--- TESTE FINALIZADO ---")
    print(f"Resultado (Seu código):  {arr_copy}")
    print(f"Esperado (Crescente):    {expected_asc}")
    
    # Compara o resultado com as duas ordenações
    if arr_copy == expected_asc:
        print("Status: OK (Crescente)")
    elif arr_copy == sorted(arr, reverse=True):
         print("Status: OK (Decrescente)")
    else:
        print("Status: FALHOU (Não ordenado)")
    print("--------------------------------------")

# --- Casos de Teste ---
if __name__ == "__main__":
    
    # Teste 1: Vetor pequeno (onde a lógica será mais fácil de ver)
    run_test("Vetor pequeno", 
             [3, 1, 2], 
             [1, 2, 3])

    # Teste 2: Vetor padrão
    run_test("Vetor padrão", 
             [8, 3, 1, 6, 4, 10, 2], 
             [1, 2, 3, 4, 6, 8, 10])
    
    # Teste 3: Vetor vazio
    run_test("Vetor vazio", 
             [], 
             [])

    # Teste 4: Vetor com 1 elemento
    run_test("Vetor com 1 elemento", 
             [5], 
             [5])
    
    # Teste 5: Vetor já ordenado (ascendente)
    run_test("Vetor já ordenado (asc)", 
             [1, 2, 3, 4, 5], 
             [1, 2, 3, 4, 5])
    
    # Teste 6: Vetor em ordem inversa (descendente)
    run_test("Vetor ordenado (desc)", 
             [5, 4, 3, 2, 1], 
             [1, 2, 3, 4, 5])

    # Teste 7: Vetor com elementos duplicados
    run_test("Vetor com duplicatas", 
             [4, 2, 5, 2, 4, 5, 1], 
             [1, 2, 2, 4, 4, 5, 5])

# O problema central da função sep é que ela não implementa corretamente um algoritmo de particionamento. Uma partição de Quicksort deve garantir uma de duas coisas:
# Que o pivô esteja em sua posição final, com todos os menores à esquerda e maiores à direita e Que o array seja dividido em dois sub-vetores (um de menores, um de maiores), sem garantir a posição final do pivô