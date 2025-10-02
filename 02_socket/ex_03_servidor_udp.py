import socket

# Criação do socket, IPv4 e UDP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP e porta associados ao servidor
IP_PORTA = ("", 5000)
socket_servidor.bind(IP_PORTA)

# Recebendo os dados
print("Esperando dados do cliente...")
dados, endereco_cliente = socket_servidor.recvfrom(1024)

# Decodifica os dados
texto = dados.decode()

# Mostra os dados
print(f"Dados recebidos de {endereco_cliente}: {texto}")

# Codifica e envia a resposta
dados = "Obrigado pelos dados!"
socket_servidor.sendto(dados.encode(), endereco_cliente)

# Libera os recursos do socket
socket_servidor.close()
