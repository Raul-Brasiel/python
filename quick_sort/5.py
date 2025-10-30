invocation_trace = []

def quicksort(array_name_str, left, right):
    """
    Simula as invocações recursivas do Quicksort com base 
    na lógica deduzida (pivot_index = right - 1).
    """
    
    # Adiciona a invocação atual à lista de rastreamento
    invocation_str = f"quicksort({array_name_str}, {left}, {right})"
    invocation_trace.append(invocation_str)
    
    # Caso base (igual ao do exemplo)
    if left < right:
        
        # Lógica de particionamento DEDUZIDA do Exemplo 1:
        # O pivô é sempre o penúltimo índice.
        pivot_index = right - 1
        
        # Chamada recursiva para a "esquerda" do pivô
        quicksort(array_name_str, left, pivot_index - 1)
        
        # Chamada recursiva para a "direita" do pivô
        quicksort(array_name_str, pivot_index + 1, right)

# --- Execução do Exemplo 1 (para verificação) ---
# Reinicia o rastreador
invocation_trace = [] 
# O primeiro argumento é apenas uma string para corresponder à saída
quicksort("array", 1, 4)

print("--- Sequência do Exemplo 1 (array[1..4] = 77 55 33 99) ---")
for line in invocation_trace:
    print(line)


# --- Execução do Exemplo 2 (O exercício) ---
# Reinicia o rastreador
invocation_trace = []
quicksort("array", 1, 6)

print("\n--- Sequência do Exemplo 2 (array[1..6] = 55 44 22 11 66 33) ---")
for line in invocation_trace:
    print(line)