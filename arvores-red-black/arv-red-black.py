import sys

# Constantes para facilitar a leitura das cores
VERMELHO = 1
PRETO = 0

class No:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.cor = VERMELHO  # Regra: Todo novo nó inserido começa como VERMELHO

class ArvoreRubroNegra:
    def __init__(self):
        # Criação do nó sentinela (NULO). 
        # Em vez de usar "None", usamos um nó real pintado de PRETO.
        # Isso evita erros ao tentar acessar a cor de um filho que não existe.
        self.NULO = No(0)
        self.NULO.cor = PRETO
        self.NULO.esquerda = None
        self.NULO.direita = None
        self.raiz = self.NULO
    
    # Rotações (Reorganizam os nós para manter o balanceamento)
    
    def rotacao_esquerda(self, x):
        # O filho da direita (y) sobe para o lugar de x
        # x desce e vira filho da esquerda de y
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.NULO:
            y.esquerda.pai = x
        y.pai = x.pai
        
        # Ajusta o pai do antigo topo (x) para apontar para o novo topo (y)
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, x):
        # O filho da esquerda (y) sobe para o lugar de x
        # x desce e vira filho da direita de y
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.NULO:
            y.direita.pai = x
        y.pai = x.pai
        
        # Ajusta o pai do antigo topo (x) para apontar para o novo topo (y)
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y

    # --- Inserção ---

    def inserir(self, chave):
        # Cria o novo nó
        novo_no = No(chave)
        novo_no.pai = None
        novo_no.esquerda = self.NULO
        novo_no.direita = self.NULO
        novo_no.cor = VERMELHO # Sempre vermelho para não mudar a altura negra

        y = None
        x = self.raiz

        # Desce na árvore procurando onde encaixar o nó (igual a uma árvore comum)
        while x != self.NULO:
            y = x
            if novo_no.valor < x.valor:
                x = x.esquerda
            else:
                x = x.direita

        # Faz a ligação do novo nó com seu pai
        novo_no.pai = y
        if y is None:
            self.raiz = novo_no # Árvore estava vazia
        elif novo_no.valor < y.valor:
            y.esquerda = novo_no
        else:
            y.direita = novo_no

        # Se for a raiz, ela deve ser preta.
        if novo_no.pai is None:
            novo_no.cor = PRETO
            return

        # Se o pai for preto, não precisa fazer nada
        if novo_no.pai.pai is None:
            return

        # Se houver conflito (Pai vermelho + filho vermelho), chama a correção
        self._inserir_correcao(novo_no)

    def _inserir_correcao(self, k):
        # Executa enquanto houver pai vermelho
        while k.pai.cor == VERMELHO:
            # O Pai está na esquerda do Avô
            if k.pai == k.pai.pai.esquerda:
                tio = k.pai.pai.direita
                
                # Caso 1: Tio é VERMELHO -> Apenas recolorir
                if tio.cor == VERMELHO:
                    tio.cor = PRETO
                    k.pai.cor = PRETO
                    k.pai.pai.cor = VERMELHO
                    k = k.pai.pai # Sobe a verificação para o avô
                else:
                    # Caso 2: Tio é PRETO e nó é filho cruzado (formato de triângulo)
                    if k == k.pai.direita:
                        k = k.pai
                        self.rotacao_esquerda(k) # Transforma triângulo em linha
                    
                    # Caso 3: Tio é PRETO e nó forma uma linha reta
                    k.pai.cor = PRETO
                    k.pai.pai.cor = VERMELHO
                    self.rotacao_direita(k.pai.pai) # Rotaciona o avô
            
            # O Pai está na direita do Avô
            else:
                tio = k.pai.pai.esquerda
                
                # Caso 1: Tio Vermelho
                if tio.cor == VERMELHO:
                    tio.cor = PRETO
                    k.pai.cor = PRETO
                    k.pai.pai.cor = VERMELHO
                    k = k.pai.pai
                else:
                    # Caso 2: Tio Preto e Triângulo
                    if k == k.pai.esquerda:
                        k = k.pai
                        self.rotacao_direita(k)
                    
                    # Caso 3: Tio Preto e Linha
                    k.pai.cor = PRETO
                    k.pai.pai.cor = VERMELHO
                    self.rotacao_esquerda(k.pai.pai)
            
            if k == self.raiz:
                break
        
        # Garante que a raiz seja sempre preta ao final
        self.raiz.cor = PRETO

    # --- Remoção ---

    def _transplantar(self, u, v):
        # Substitui a subárvore enraizada em 'u' pela subárvore 'v'
        if u.pai is None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def _minimo(self, no):
        # Encontra o nó mais à esquerda (menor valor)
        while no.esquerda != self.NULO:
            no = no.esquerda
        return no

    def _remover_no_auxiliar(self, no, chave):
        # Busca o nó a ser removido
        z = self.NULO
        while no != self.NULO:
            if no.valor == chave:
                z = no
            if no.valor <= chave:
                no = no.direita
            else:
                no = no.esquerda

        if z == self.NULO:
            print("Chave não encontrada")
            return

        y = z
        cor_original_y = y.cor
        
        # Casos de remoção da Árvore Binária (sem filhos ou 1 filho)
        if z.esquerda == self.NULO:
            x = z.direita
            self._transplantar(z, z.direita)
        elif z.direita == self.NULO:
            x = z.esquerda
            self._transplantar(z, z.esquerda)
        else:
            # Caso com 2 filhos: Busca o sucessor (menor da direita)
            y = self._minimo(z.direita)
            cor_original_y = y.cor
            x = y.direita
            
            if y.pai == z:
                x.pai = y
            else:
                self._transplantar(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y

            self._transplantar(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor

        # Se a cor original do nó removido/movido era PRETA, violamos a regra da altura negra, e precisamos corrigir.
        if cor_original_y == PRETO:
            self._remover_correcao(x)

    def _remover_correcao(self, x):
        # Algoritmo complexo para restaurar o equilíbrio de nós pretos
        while x != self.raiz and x.cor == PRETO:
            if x == x.pai.esquerda:
                irmao = x.pai.direita
                # Caso 1: Irmão Vermelho
                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    x.pai.cor = VERMELHO
                    self.rotacao_esquerda(x.pai)
                    irmao = x.pai.direita

                # Caso 2: Irmão Preto e sobrinhos Pretos
                if irmao.esquerda.cor == PRETO and irmao.direita.cor == PRETO:
                    irmao.cor = VERMELHO
                    x = x.pai
                else:
                    # Caso 3: Irmão Preto e sobrinho esquerdo Vermelho
                    if irmao.direita.cor == PRETO:
                        irmao.esquerda.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rotacao_direita(irmao)
                        irmao = x.pai.direita
                    
                    # Caso 4: Irmão Preto e sobrinho direito Vermelho
                    irmao.cor = x.pai.cor
                    x.pai.cor = PRETO
                    irmao.direita.cor = PRETO
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                # Simétrico (Espelho para o lado direito)
                irmao = x.pai.esquerda
                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    x.pai.cor = VERMELHO
                    self.rotacao_direita(x.pai)
                    irmao = x.pai.esquerda

                if irmao.direita.cor == PRETO and irmao.esquerda.cor == PRETO:
                    irmao.cor = VERMELHO
                    x = x.pai
                else:
                    if irmao.esquerda.cor == PRETO:
                        irmao.direita.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rotacao_esquerda(irmao)
                        irmao = x.pai.esquerda

                    irmao.cor = x.pai.cor
                    x.pai.cor = PRETO
                    irmao.esquerda.cor = PRETO
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = PRETO

    def remover(self, chave):
        self._remover_no_auxiliar(self.raiz, chave)

    # --- Busca ---
    def buscar(self, k):
        return self._buscar_recursivo(self.raiz, k)

    def _buscar_recursivo(self, no, chave):
        # Se achou ou chegou numa folha (NULO)
        if no == self.NULO or chave == no.valor:
            return no
        # Recursão esquerda ou direita
        if chave < no.valor:
            return self._buscar_recursivo(no.esquerda, chave)
        return self._buscar_recursivo(no.direita, chave)

    # --- Impressão Visual ---
    def imprimir_arvore(self):
        print("----- Árvore Rubro-Negra -----")
        # Inicia a impressão recursiva a partir da raiz
        self._imprimir_visual(self.raiz, "", 0)

    def _imprimir_visual(self, no, recuo, direcao):
        if no != self.NULO:
            novo_recuo = recuo + "       "
            
            # Imprime a direita (que visualmente fica em cima)
            self._imprimir_visual(no.direita, novo_recuo, 1)

            # Prepara o desenho dos conectores
            conector = ""
            recuo_atual = ""
            if direcao == 0:   # Raiz
                conector = "Raiz: "
            elif direcao == 1: # Filho Direito
                conector = "/-- "
                recuo_atual = recuo
            else:              # Filho Esquerdo
                conector = "\-- "
                recuo_atual = recuo
            
            texto_cor = " (V)" if no.cor == VERMELHO else " (P)"
            
            # Imprime o valor do nó
            print(f"{recuo_atual}{conector}{no.valor}{texto_cor}")

            # Imprime a esquerda (que visualmente fica embaixo)
            self._imprimir_visual(no.esquerda, novo_recuo, -1)

if __name__ == "__main__":
    arvore = ArvoreRubroNegra()
    elementos = [4, 2, 5, 1, 3, 6]
    
    print(f"Inserindo: {elementos}")
    for el in elementos:
        arvore.inserir(el)
    
    arvore.imprimir_arvore()

    print("\n--- Teste de Busca ---")
    resultado = arvore.buscar(3)
    if resultado != arvore.NULO:
        cor = "Vermelho" if resultado.cor == VERMELHO else "Preto"
        print(f"Nó 3 encontrado. Cor: {cor}")
    
    print("\n--- Teste de Remoção (Removendo 1) ---")
    arvore.remover(1)
    arvore.imprimir_arvore()
