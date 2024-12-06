import socket


def main() -> None:
    with socket.create_connection(("127.0.0.1", 5000)) as socket_cliente:
        apelido = input("Digite seu apelido: ")
        socket_cliente.sendall(apelido.encode())

        while len(apelido) >= 3:
            mensagem = input("Digite uma mensagem: ")
            socket_cliente.sendall(mensagem.encode())

            if mensagem.lower() == "sair":
                break


try:
    main()
except (ConnectionRefusedError, ConnectionAbortedError):
    print("\nOcorreu um erro na conexão com o servidor!")
except KeyboardInterrupt:
    print("\nO usuário abortou a execução do programa!")
except Exception:
    print("\nOcorreu um erro desconhecido!")
