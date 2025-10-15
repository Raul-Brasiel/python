# 🧩 Merge Sort em Python

Esse código implementa o algoritmo de ordenação **Merge Sort**, um dos métodos mais eficientes e estáveis para organizar grandes volumes de dados.  

---

## 📚 Sobre o algoritmo

O **Merge Sort** segue o paradigma **Dividir para Conquistar (Divide and Conquer)**:

1. **Divisão:** o vetor é dividido repetidamente em duas metades até restarem listas com apenas um elemento.
2. **Conquista:** as sublistas são ordenadas (implicitamente, pois listas unitárias já estão em ordem).
3. **Combinação:** as listas ordenadas são intercaladas, formando listas maiores até chegar ao vetor final ordenado.

Esse processo garante que todos os elementos sejam comparados de forma eficiente, mantendo uma **complexidade de tempo O(n log n)** em todos os casos (melhor, médio e pior).

---

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
