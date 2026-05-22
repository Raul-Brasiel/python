# Servidor HTTP Simples em Python (Socket Puro)
Este projeto implementa um servidor web básico utilizando a biblioteca padrão socket do Python. O objetivo é demonstrar como funciona a comunicação HTTP "por baixo do capô", sem o uso de frameworks prontos (como Flask, Django ou http.server).

## 📚 Conceitos Básicos
### O Protocolo HTTP

A comunicação na web funciona através de Requisições (Requests) e Respostas (Responses).

1. **Requisição:** O cliente (navegador) envia um texto para o servidor pedindo algo. A primeira linha geralmente contém o método (GET, POST), o caminho (ex: ``/index.html``) e a versão do protocolo.

*    Exemplo: ``GET / HTTP/1.1``

2. **Resposta:** O servidor processa o pedido e devolve um texto formatado.

*    Exemplo: ``HTTP/1.1 200 OK`` (Status), seguido de cabeçalhos e o conteúdo (corpo).

**O que são Sockets?**

Sockets são a porta de entrada e saída para dados na rede.

1. **Socket do Servidor:** Fica "ouvindo" em uma porta específica (ex: 8080).

2. **Accept:** Quando um navegador tenta entrar, o servidor "aceita" e cria um canal direto.

3. **Recv/Send:** O servidor lê o que o navegador mandou (``recv``) e escreve a resposta (``send``) de volta.

## 🚀 Como Executar

**Pré-requisitos**

* Python 3 instalado no seu computador.

**Passo a Passo**

1. **Baixe o código:** Salve o arquivo ``server.py`` em uma pasta.

2. **Abra o terminal:** Navegue até a pasta onde salvou o arquivo.

3. **Execute o servidor:**

```bash
python server.py
```

4. **Teste no Navegador:** Abra seu navegador preferido (Chrome, Firefox, Edge) e acesse: http://localhost:8080

**O que esperar**

* **No Navegador:** Você verá a mensagem de texto simples: "Ola! Voce acessou meu servidor HTTP feito do zero com Sockets."

* **No Terminal:** O servidor imprimirá logs das requisições recebidas, mostrando o IP do cliente e o método solicitado (ex: ``Requisição recebida de ('127.0.0.1', 54321): GET / HTTP/1.1``).

## 🛠 Detalhes da Implementação

O código segue este fluxo:

1. ``socket()``: Cria o ponto de comunicação.

2. ``bind()``: Reserva o endereço localhost na porta 8080.

3. ``listen()``: Aguarda chamadas.

4. ``accept()``: Atende uma chamada do navegador.

5. ``recv()``: Lê o texto bruto que o navegador enviou.

**Resposta Manual:** Montamos uma string formatada seguindo a regra estrita do HTTP (cabeçalhos, linha em branco, corpo) e a enviamos de volta.
