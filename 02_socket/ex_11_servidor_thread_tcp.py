import socket


def tratar_cliente(socket_cliente) -> None:
    dados = socket_cliente.recv(1024)
    apelido = dados.decode()
    print(f"Cliente conectado: {endereco_cliente} - {apelido}")

    while True:
        dados = socket_cliente.recv(1024)
        mensagem = dados.decode()

        if mensagem == "sair":
            print(f"{apelido} saiu!")
            socket_cliente.close()
            break
        else:
            print(f"{apelido} disse: {mensagem}")


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(("0.0.0.0", 5000))
socket_servidor.listen(2)

while True:
    print("Esperando um cliente conectar...")
    socket_cliente, endereco_cliente = socket_servidor.accept()
    tratar_cliente(socket_cliente)
