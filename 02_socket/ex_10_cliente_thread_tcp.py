import socket


def main() -> None:
    with socket.create_connection(("localhost", 5000)) as socket_cliente:
        apelido = input("Digite seu apelido: ")
        socket_cliente.sendall(apelido.encode())

        while len(apelido) >= 3:
            mensagem = input("Digite sua mensagem: ")
            socket_cliente.sendall(mensagem.encode())

            if mensagem.lower() == "sair":
                print("Você pediu para sair!")
                break


if __name__ == "__main__":
    try:
        main()
    except ConnectionError:
        print("Erro de conexão com o servidor!")
    except KeyboardInterrupt:
        print("\nO usuário abordou a execução!")
