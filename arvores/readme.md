# Implementação de Árvore AVL em Python

Este repositório contém uma implementação completa e didática de uma **Árvore AVL** desenvolvida em Python. O código utiliza variáveis e funções em português e não faz uso de bibliotecas externas para a estrutura de dados.

## 🌳 O que é uma Árvore AVL?

Uma Árvore AVL é uma árvore binária de busca (BST) **auto-balanceável**. A característica fundamental é que a diferença de altura entre as subárvores esquerda e direita de qualquer nó (chamada de **Fator de Balanceamento**) deve ser sempre -1, 0 ou 1.

Se a árvore se tornar desbalanceada após uma inserção ou remoção (fator atinge -2 ou 2), o algoritmo aplica **Rotações** automáticas para restaurar o equilíbrio, garantindo complexidade $O(\log n)$ para as operações principais.

## ⚙️ Funcionalidades

O código (`arvore_avl.py`) implementa as seguintes operações:

* **`inserir(raiz, chave)`**: Adiciona um novo valor e verifica o balanceamento.
* **`remover(raiz, chave)`**: Remove um nó e reajusta a árvore (trata nós folhas e nós com filhos).
* **`buscar(raiz, chave)`**: Procura um valor específico.
* **`rotacao_direita` e `rotacao_esquerda`**: Funções fundamentais para o rebalanceamento.
* **`obter_balanceamento`**: Calcula a diferença de altura entre subárvores.

## 🔄 Rotações Implementadas

O algoritmo trata automaticamente os 4 casos de desbalanceamento:

1.  **Rotação Direita (Caso Esq-Esq):** Desbalanceamento na subárvore esquerda do filho esquerdo.
2.  **Rotação Esquerda (Caso Dir-Dir):** Desbalanceamento na subárvore direita do filho direito.
3.  **Rotação Dupla (Esq-Dir):** Rotação à esquerda no filho, seguida de rotação à direita no pai.
4.  **Rotação Dupla (Dir-Esq):** Rotação à direita no filho, seguida de rotação à esquerda no pai.

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Execução
1.  Baixe o arquivo `arvore_avl.py`.
2.  No terminal, execute:

```bash
python arvore_avl.py
