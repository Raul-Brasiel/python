# 🌳 Árvore Rubro-Negra (Red-Black Tree) em Python

Implementação didática e completa de uma **Árvore Rubro-Negra** (Red-Black Tree) desenvolvida do zero em Python. Este projeto foca na clareza do código e na visualização da estrutura, implementando manualmente todas as rotações e regras de coloração sem o uso de bibliotecas externas.

## 📖 Sobre o Projeto

A Árvore Rubro-Negra é uma árvore binária de busca auto-balanceável. Ela garante que a altura da árvore seja sempre **O(log n)**, assegurando eficiência nas operações de busca, inserção e remoção, mesmo no pior caso.

**Funcionalidades Implementadas:**
* **Inserção (`inserir`):** Adiciona nós e corrige violações automaticamente.
* **Remoção (`remover`):** Remove nós tratando casos complexos (ex: duplo preto).
* **Busca (`buscar`):** Localiza valores na estrutura.
* **Visualização (`imprimir_arvore`):** Renderiza a árvore no terminal mostrando a hierarquia e as cores.

---

## ⚖️ Propriedades da Árvore Rubro-Negra

Para que a árvore seja considerada Rubro-Negra, este algoritmo assegura as seguintes **5 invariantes** após cada modificação:

1.  **Propriedade da Cor:** Todo nó é ou Vermelho ou Preto.
2.  **Propriedade da Raiz:** A raiz é sempre Preta.
3.  **Propriedade da Folha:** Todas as folhas (nós sentinelas `NULO`) são Pretas.
4.  **Propriedade Vermelha:** Se um nó é Vermelho, então ambos os seus filhos são Pretos (não existem nós Vermelhos consecutivos).
5.  **Propriedade da Altura Negra:** Para qualquer nó, todos os caminhos simples dele até as folhas descendentes contêm o mesmo número de nós Pretos.

---

## ⚙️ Funcionamento e Casos de Inserção

Ao inserir um novo nó, ele é sempre colocado inicialmente como **VERMELHO**. Isso pode violar a propriedade 4 (Pai e Filho vermelhos). O algoritmo resolve isso verificando a cor do **Tio** do novo nó.

### 🔄 Rotações
O algoritmo utiliza duas operações básicas para reestruturar a árvore sem perder a ordem dos elementos:
* **Rotação à Esquerda:** O filho da direita sobe, o pai desce para a esquerda.
* **Rotação à Direita:** O filho da esquerda sobe, o pai desce para a direita.

### 🎨 Casos de Correção (Fixup)

Suponha que `K` é o novo nó inserido e `P` é seu Pai. Se `P` for Vermelho, temos um conflito. Olhamos para o **Tio (U)** de `K`:

#### Caso 1: Tio é VERMELHO 🔴
* **Ação:** Recoloração.
* **O que acontece:** O Pai e o Tio tornam-se **Pretos**. O Avô torna-se **Vermelho**.
* **Resultado:** O problema é resolvido localmente, mas a verificação sobe para o Avô (que agora é vermelho).

#### Caso 2: Tio é PRETO ⚫ (Formato Triângulo)
* **Cenário:** O nó `K` e seu Pai `P` estão em direções opostas (ex: Pai é filho esquerdo, `K` é filho direito).
* **Ação:** Rotação Simples no Pai.
* **Resultado:** Transforma o "triângulo" em uma "linha", preparando para o Caso 3.

#### Caso 3: Tio é PRETO ⚫ (Formato Linha)
* **Cenário:** O nó `K` e seu Pai `P` estão na mesma direção (ambos filhos esquerdos ou ambos direitos).
* **Ação:** Rotação no Avô + Troca de Cores.
* **Resultado:** O Pai sobe e vira **Preto**, o Avô desce e vira **Vermelho**. O balanceamento é restaurado.

---

## 🚀 Como Executar

Como o projeto é escrito em Python, não é necessária uma compilação prévia (geração de binário). O código é interpretado diretamente.

### Pré-requisitos
* Python 3.6 ou superior instalado.

### Passo a Passo

* **Clone o repositório e execute o arquivo principal:**
    ```bash
    python arv-red-black.py
    ```

---

## 💻 Exemplo de Uso

O arquivo `arv-red-black.py` contém um bloco de execução que demonstra as funcionalidades. Abaixo, um exemplo de como instanciar e usar a classe:

```python

# 1. Instancia a Árvore
arvore = ArvoreRubroNegra()

# 2. Insere Elementos
# A árvore se auto-balanceará a cada inserção
nums = [4, 2, 5, 3, 6]
for n in nums:
    arvore.inserir(n)

# 3. Visualiza a Estrutura
# (V) = Vermelho, (P) = Preto
arvore.imprimir_arvore()

# Saída Esperada (Visualização Hierárquica):
#                /-- 6 (V)
#        /-- 5 (P)
# Raiz: 4 (P)
#       \        /-- 3 (V)
#        \-- 2 (P)

# 4. Remove Elementos
arvore.remover(40)
