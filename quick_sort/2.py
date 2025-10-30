import time
import random
import copy

def partition_2(arr, low, high):
    """
    Função para particionar o array e encontrar a posição do pivô.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def iterative_quicksort(arr, low, high):
    """
    Implementação iterativa do algoritmo Quicksort.
    """
    # Cria uma pilha para armazenar os índices.
    # A pilha de execução simula o que a recursão faria.
    stack = []
    
    # Adiciona o intervalo inicial à pilha.
    stack.append((low, high))

    # Loop enquanto a pilha não estiver vazia.
    while stack:
        # Remove o primeiro elemento da pilha.
        low, high = stack.pop()

        # Encontra a posição do pivô.
        pivot_index = partition_2(arr, low, high)

        # Se houver elementos à esquerda do pivô, adiciona o intervalo à pilha.
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        # Se houver elementos à direita do pivô, adiciona o intervalo à pilha.
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def quicksort(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

def run_tests():
    # Tamanhos dos vetores de teste
    sizes = [1000, 10000 ] 
    results = []

    for size in sizes:
        # Geração do vetor aleatório
        original_array = [random.randint(1, size * 2) for _ in range(size)]
        
        # Cria cópias para garantir que ambas as funções trabalhem no mesmo dado não ordenado
        array_rec = copy.copy(original_array)
        array_iter = copy.copy(original_array)

        # Medir tempo - Versão Recursiva
        start_time_rec = time.perf_counter()
        quicksort(array_rec, 0, len(array_rec) - 1)
        end_time_rec = time.perf_counter()
        time_rec = end_time_rec - start_time_rec

        # Medir tempo - Versão Iterativa
        start_time_iter = time.perf_counter()
        iterative_quicksort(array_iter, 0, len(array_iter) - 1)
        end_time_iter = time.perf_counter()
        time_iter = end_time_iter - start_time_iter
        
        # Verifica se a ordenação foi correta (opcional, mas bom para validação)
        # assert array_rec == sorted(original_array)
        # assert array_iter == sorted(original_array)

        results.append({
            "Tamanho": size,
            "Tempo Recursivo (s)": f"{time_rec:.6f}",
            "Tempo Iterativo (s)": f"{time_iter:.6f}"
        })

    return results

#Executa os testes
test_results = run_tests()
print(test_results)

#Tamanho do Vetor	Tempo Quicksort Recursivo (s)	Tempo Quicksort Iterativo (s)
#  1.000	                        0.000982	            0.001094
#  10.000	                        0.012917	            0.013319
#
#Quicksort Recursivo: Vantagens: A versão recursiva é geralmente mais fácil de escrever, entender e manter, pois reflete diretamente a natureza "dividir e conquistar" do algoritmo. O código é mais curto e direto. Desvantagens: Cada chamada recursiva exige que o sistema operacional (ou o interpretador da linguagem) aloque um novo frame na pilha de chamadas para armazenar variáveis locais e o endereço de retorno. Isso representa uma sobrecarga de memória implícita. 
#
#Quicksort Iterativo: Vantagens: O programador tem controle total sobre a pilha (tamanho, alocação), e a sobrecarga de memória é mais previsível (embora o consumo total possa ser similar). Desvantagens: A versão iterativa é significativamente mais complexa de implementar, pois requer o gerenciamento manual da pilha. A lógica de empilhamento e desempilhamento dos índices (o que a recursão faria automaticamente) precisa ser codificada.