import socket #Biblioteca para TCP/IP

def iniciar_servidor(host='localhost', port=8080):
    # Criação do Socket
    # AF_INET indica que usaremos IPv4
    # SOCK_STREAM indica que usaremos TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reusar a porta imediatamente após fechar o servidor (evita erro "Address already in use")
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Vinculação, associa o socket a um host e uma porta específica
        server_socket.bind((host, port))
        
        # Escuta, coloca o servidor em modo de escuta por conexões.
        server_socket.listen(1)
        print(f"Servidor rodando em http://{host}:{port}")

        while True:
            # O código para e espera um cliente tentar conectar
            client_connection, client_address = server_socket.accept()

            # Ler a Requisição. Recebe até 1024 bytes de dados enviados pelo navegador
            request_data = client_connection.recv(1024).decode('utf-8')
            
            # Se não houver dados, ignora
            if not request_data:
                client_connection.close()
                continue

            # Extrai apenas a primeira linha da requisição (ex: GET / HTTP/1.1)
            first_line = request_data.split('\n')[0]
            print(f"Requisição recebida de {client_address}: {first_line}")

            # Construir a Resposta (Response) manualmente
            # Formato HTTP/1.1:
            # - Linha de status (HTTP/1.1 200 OK)
            # - Headers (Content-Type, Content-Length, etc.)
            # - Linha em branco, para separar headers do corpo
            # - Corpo da mensagem
            
            body = "Olá mundo!"
            
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain; charset=utf-8\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Connection: close\r\n"
                "\r\n"  # Linha em branco
                f"{body}"
            )

            # Enviar a Resposta, codificando a string para bytes antes
            client_connection.sendall(response.encode('utf-8'))

            # Fechar a conexão com este cliente
            client_connection.close()

    except KeyboardInterrupt:
        print("\nServidor interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro no servidor: {e}")
    finally:
        # Garante que o socket principal seja fechado ao sair
        server_socket.close()

if __name__ == "__main__":
    iniciar_servidor()