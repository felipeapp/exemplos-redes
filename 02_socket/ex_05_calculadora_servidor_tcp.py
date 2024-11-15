import socket

IP_PORTA = ("0.0.0.0", 5000)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(IP_PORTA)
socket_servidor.listen(2)

while True:
    print("\nEsperando um cliente conectar...")
    socket_cliente, endereco_cliente = socket_servidor.accept()

    print("Esperando dados do cliente...")
    dados = socket_cliente.recv(1024)

    numero1, numero2, operacao = dados.decode().strip().split(";")
    numero1 = float(numero1)
    numero2 = float(numero2)
    print(f"Dados recebidos de {endereco_cliente}: {numero1} {operacao} {numero2}")

    if operacao == "+":
        resposta = numero1 + numero2
    elif operacao == "-":
        resposta = numero1 - numero2
    elif operacao == "*":
        resposta = numero1 * numero2
    elif operacao == "/":
        resposta = numero1 / numero2
    else:
        resposta = "@"

    socket_cliente.sendall(str(resposta).encode())
    socket_cliente.close()
