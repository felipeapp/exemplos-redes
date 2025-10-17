# Estudo Dirigido: Threads e Sockets em Python

Este estudo dirigido oferece uma introdução simples e direta aos conceitos de threads e sockets em Python. O objetivo é fornecer o conhecimento básico e essencial para entender, com exemplos práticos e robustos, como utilizar esses recursos em seus projetos.

## Parte 1: Threads - Executando Tarefas em Paralelo

### 1.1. O que são Threads?

Imagine que você está cozinhando: enquanto a água para o macarrão ferve, você pode cortar os vegetais para o molho. Cada uma dessas atividades é como uma "thread" (linha de execução). Em programação, uma thread é uma sequência de instruções que pode ser executada de forma concorrente com outras dentro do mesmo programa.

Isso é especialmente útil para tarefas que envolvem espera (I/O-bound), como fazer o download de um arquivo ou aguardar uma resposta de um servidor na rede. Enquanto uma thread espera, outra pode utilizar o processador, tornando a aplicação mais responsiva.

### 1.2. Módulo `threading`

O principal módulo para trabalhar com threads em Python é o `threading`.

**Exemplo prático:**

```python
import threading
import time


def tarefa_simples(id_thread: int, tempo_espera: float) -> None:
    # Uma função simples que simula uma tarefa demorada
    print(f"Thread {id_thread}: Iniciando.")
    time.sleep(tempo_espera)
    print(f"Thread {id_thread}: Finalizada.")


# Criando as threads
thread1 = threading.Thread(target=tarefa_simples, args=(1, 2))
thread2 = threading.Thread(target=tarefa_simples, args=(2, 1.5))

# Iniciando as threads (elas rodam "em paralelo")
thread1.start()
thread2.start()

print("Programa principal: Aguardando as threads finalizarem...")
# O método join() pausa a execução do programa principal até que a thread termine.
thread1.join()
thread2.join()

print("Programa principal: Todas as threads foram finalizadas.")
```

## Parte 2: Sockets - A Base da Comunicação em Rede

### 2.1. O que são Sockets?

Sockets são a interface padrão para a programação de rede. Eles funcionam como pontos de comunicação entre processos, que podem estar na mesma máquina ou em máquinas diferentes. Pense em um socket como um "telefone" que seu programa usa para "ligar" e "conversar" com outro. A comunicação geralmente envolve dois papéis:

- **Servidor (Server):** Um programa que abre um socket, fica "escutando" em um endereço IP e porta específicos, aguardando conexões.
- **Cliente (Client):** Um programa que cria um socket e o utiliza para se conectar ao servidor.

### 2.2. A Importância do Bloco `with` com Sockets

Quando você abre um socket (ou um arquivo), é crucial garantir que ele seja fechado ao final do uso, mesmo que ocorram erros. O bloco `with` (gerenciador de contexto) automatiza isso.

```python
# 'with' garante que s.close() será chamado automaticamente
# ao final do bloco, seja por sucesso ou por uma exceção.
with socket.create_connection((HOST, PORT)) as s:
    # usa o socket 's'
# aqui fora, o socket 's' já está fechado.
```

Usar `with` evita vazamento de recursos e torna o código mais limpo e seguro do que fechar o socket manualmente.

### 2.3. Funções `create_server` e `create_connection`

Em vez de criar, vincular (`bind`) e escutar (`listen`) manualmente, o Python oferece funções de alto nível que simplificam o processo e aplicam boas práticas por padrão.

- `socket.create_connection((host, port))`: Para o **cliente**. Esta função tenta se conectar a um endereço. Ela lida automaticamente com a escolha entre IPv4 e IPv6 e simplifica a lógica de conexão em uma única chamada.

- `socket.create_server((host, port))`: Para o **servidor**. Esta função cria o socket, faz o `bind` ao endereço e porta, e já o coloca em modo `listen`.

## Parte 3: Juntando Tudo - Um Servidor Multithreading

Agora, vamos aplicar todos os conceitos: um servidor que usa `create_server`, aceita múltiplos clientes e cria uma `thread` dedicada para cada um e faz tratamento de erros.

### Código do Servidor Final (`servidor.py`)

```python
import socket
import threading

# Constantes para o endereço do servidor
HOST = "127.0.0.1"  # localhost
PORT = 5555


def lidar_com_cliente(conn: socket.socket, addr: tuple) -> None:
    """
    Função alvo da thread. Lida com a comunicação de um único cliente.

    'conn' é o objeto socket da conexão.
    'addr' é uma tupla contendo o IP e a porta do cliente.
    """
    print(f"Novo cliente conectado: {addr}")

    # Envolve a comunicação em um try/except para que um cliente com erro
    # não derrube o servidor inteiro.
    try:
        # 'with conn' garante que a conexão deste cliente será fechada.
        with conn:
            while True:
                # Espera receber até 1024 bytes de dados
                data = conn.recv(1024)
                if not data:
                    # Se data está vazio, o cliente encerrou a conexão
                    break
                print(f"Mensagem de {addr}: {data.decode()}")

                # Echo: envia a mesma mensagem de volta ao cliente
                conn.sendall(data)
    except Exception as e:
        print(f"Erro na conexão com {addr}: {e}")

    print(f"Cliente {addr} desconectado.")


# Função principal que inicia o servidor
def main() -> None:
    try:
        with socket.create_server((HOST, PORT)) as server_socket:
            print(f"Servidor pronto para receber conexões em {HOST}:{PORT}")

            while True:
                # Bloqueia a execução até uma nova conexão chegar
                conn, addr = server_socket.accept()

                # Cria e inicia uma nova thread para o cliente que conectou
                thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
                thread.start()
    except KeyboardInterrupt:
        print("\nServidor sendo encerrado pelo usuário.")
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")


if __name__ == "__main__":
    main()
```

### Código do Cliente Final (`cliente_final.py`)

```python
import socket

HOST = "127.0.0.1"
PORT = 5555


# Função principal que inicia o cliente e se conecta ao servidor
def main() -> None:
    try:
        # 'create_connection' simplifica a criação e conexão do socket.
        # O 'with' garante que o socket será fechado corretamente.
        with socket.create_connection((HOST, PORT)) as s:
            print("Conectado ao servidor com sucesso!")
            mensagem = input("Digite sua mensagem ('sair' ou '' para fechar): ").strip()

            if mensagem != "" and mensagem.lower() != "sair":
                # Envia a mensagem codificada em UTF-8
                s.sendall(mensagem.encode())

                # Aguarda a resposta do servidor
                data = s.recv(1024)
                print(f"Servidor respondeu: {data.decode()}")
    # Captura qualquer exceção de rede (ex: servidor offline) de forma genérica
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    print("Conexão encerrada.")


if __name__ == "__main__":
    main()
```

### Como Testar

1.  Salve o código do servidor como `servidor_final.py` e o do cliente como `cliente_final.py`.
2.  Abra um terminal e execute o servidor: `python servidor_final.py`.
3.  Abra **um ou mais** outros terminais e execute o cliente em cada um: `python cliente_final.py`.
4.  Digite mensagens em cada cliente e observe como o servidor responde a todos eles de forma concorrente.
