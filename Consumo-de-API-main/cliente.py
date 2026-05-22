# pip install requests

import requests #cria os pacotes HTTP
import os #bibliotecas do sistema operacional, para limpar a tela e encerrar
import sys

# CONFIGURAÇÃO DE REDE
# Se rodar no mesmo PC: use "localhost"
# Se rodar em PCs diferentes: coloque o IP da máquina (ex: "192.168.1.5")
IP_DO_SERVIDOR = "localhost" 
PORTA = "8000"
URL_API = f"http://{IP_DO_SERVIDOR}:{PORTA}/eventos"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# OPERAÇÃO 1: LER/LISTAR (GET) ---
def listar_eventos():
    print("\n--- LISTA DE EVENTOS (GET) ---")
    try:
        # Abre uma conexão TCP na porta 8000
        resposta = requests.get(URL_API)
        
        # Lê o número que voltou no cabeçalho HTTP
        if resposta.status_code == 200:
            eventos = resposta.json() #converte o texto json que o servidor mandou
            if not eventos: #Se estiver vazio
                print("Nenhum evento cadastrado.")
            else:
                for ev in eventos:
                    print(f"ID: {ev['id']} | Evento: {ev['nome']} | Palestrante: {ev['palestrante']}")
        else:
            print(f"Erro ao buscar dados: {resposta.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

# OPERAÇÃO 2: CRIAR/CADASTRAR (POST)
def cadastrar_evento():
    print("\n--- NOVO EVENTO (POST) ---")
    try:
        id_ev = int(input("Digite o ID do evento: "))
        nome = input("Nome do Evento: ")
        palestrante = input("Nome do Palestrante: ")

        dados = {"id": id_ev, "nome": nome, "palestrante": palestrante}

        # Converte para texto JSON e coloca no Corpo (Body) do pacote HTTP.
        # E envia o JSON para a API
        resposta = requests.post(URL_API, json=dados)

        if resposta.status_code == 200:
            print("✅ Evento cadastrado com sucesso!")
        else:
            print(f"❌ Erro: {resposta.status_code} - {resposta.text}")
            
    except ValueError:
        print("Erro: O ID deve ser um número.")

# --- OPERAÇÃO 3: UPDATE (PUT) ---
def atualizar_evento():
    print("\n--- ATUALIZAR EVENTO (PUT) ---")
    id_alvo = input("Digite o ID do evento que deseja alterar: ")
    
    # URL específica (ex: .../eventos/1)
    url_especifica = f"{URL_API}/{id_alvo}"
    
    # Precisamos mandar o objeto completo novamente
    print("Preencha os novos dados:")
    novo_nome = input("Novo Nome do Evento: ")
    novo_palestrante = input("Novo Palestrante: ")
    
    dados = {"id": int(id_alvo), "nome": novo_nome, "palestrante": novo_palestrante}
    
    #envia o pacote com put
    # o servidor pega o que tem nesse endereço e substitui pelo novo json
    resposta = requests.put(url_especifica, json=dados)
    
    if resposta.status_code == 200:
        print("✅ Evento atualizado!")
    else:
        print(f"❌ Erro ao atualizar: {resposta.text}")

# --- OPERAÇÃO 4: DELETE (DELETE) ---
def deletar_evento():
    print("\n--- DELETAR EVENTO (DELETE) ---")
    id_alvo = input("Digite o ID do evento para excluir: ")
    
    url_especifica = f"{URL_API}/{id_alvo}"
    
    #envia o pacote com delete
    resposta = requests.delete(url_especifica)
    
    if resposta.status_code == 200:
        print("🗑️ Evento excluído com sucesso!")
    else:
        print(f"❌ Erro ao excluir: {resposta.text}")

# --- MENU PRINCIPAL ---
def menu():
    while True:
        print("\n" + "="*30)
        print(" SISTEMA DE GESTÃO DE EVENTOS ")
        print("="*30)
        print("1. Listar Eventos")
        print("2. Cadastrar Evento")
        print("3. Atualizar Evento")
        print("4. Excluir Evento")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_eventos()
        elif opcao == '2':
            cadastrar_evento()
        elif opcao == '3':
            atualizar_evento()
        elif opcao == '4':
            deletar_evento()
        elif opcao == '5':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()