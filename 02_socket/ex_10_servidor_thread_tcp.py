import socket
import threading


def tratar_cliente(socket_cliente: socket.socket, endereco_cliente: tuple[str, int]) -> None:
    try:
        with socket_cliente:
            print(f"Cliente conectado: {endereco_cliente}")
            apelido = socket_cliente.recv(1024).decode()

            while len(apelido) >= 3:
                mensagem = socket_cliente.recv(1024).decode()
                print(f"{apelido} disse: {mensagem}")

                if mensagem == "" or mensagem.lower() == "sair":
                    print(f"{apelido} pediu para sair!")
                    break
    except ConnectionError:
        print(f"Erro de conexão com o cliente {endereco_cliente}!")


def iniciar_servidor() -> None:
    with socket.create_server(("", 5000)) as socket_servidor:
        while True:
            print("Esperando cliente conectar...")
            socket_cliente, endereco_cliente = socket_servidor.accept()
            threading.Thread(target=tratar_cliente, args=(socket_cliente, endereco_cliente)).start()


if __name__ == "__main__":
    iniciar_servidor()
