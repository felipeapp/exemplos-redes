import socket

IP_PORTA = ("0.0.0.0", 5000)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(IP_PORTA)

while True:
    print("\nEsperando dados do cliente...")
    dados, endereco_cliente = socket_servidor.recvfrom(1024)

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

    socket_servidor.sendto(str(resposta).encode(), endereco_cliente)
