import socket
from threading import Thread


def tratar_cliente(socket_cliente: socket.socket, endereco_cliente: tuple[str, int]) -> None:
    try:
        with socket_cliente:
            apelido = socket_cliente.recv(1024).decode().strip()
            print(f"Cliente conectado: {endereco_cliente} - {apelido}")

            while len(apelido) >= 3:
                mensagem = socket_cliente.recv(1024).decode().strip()

                if mensagem is None or mensagem == "" or mensagem.lower() == "sair":
                    print(f"{apelido} saiu!")
                    break
                else:
                    print(f"{apelido} disse: {mensagem}")
    except (ConnectionRefusedError, ConnectionAbortedError):
        print(f"\nO cliente {endereco_cliente} abortou a conexão!")
    except Exception:
        print(f"\nOcorreu um erro desconhecido tratando o cliente {endereco_cliente}!")


with socket.create_server(("0.0.0.0", 5000)) as socket_servidor:
    while True:
        print("Esperando um cliente conectar...")
        socket_cliente, endereco_cliente = socket_servidor.accept()
        Thread(target=tratar_cliente, args=(socket_cliente, endereco_cliente)).start()
