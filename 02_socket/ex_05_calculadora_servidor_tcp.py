import socket

IP_PORTA = ("", 5000)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(IP_PORTA)
socket_servidor.listen(2)

while True:
    print(40 * "-")
    print("Esperando um cliente conectar...")
    socket_cliente, endereco_cliente = socket_servidor.accept()
    print("Cliente conectado:", endereco_cliente)

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
        resposta = "Erro: divisão por zero!" if numero2 == 0 else numero1 / numero2
    else:
        resposta = "Erro: operador inválido!"

    socket_cliente.sendall(str(resposta).encode())
    socket_cliente.close()
