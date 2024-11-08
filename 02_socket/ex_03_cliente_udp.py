import socket

texto = input("Digite o texto para enviar: ")

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP_PORTA_SERVIDOR = ("127.0.0.1", 5000)
socket_cliente.sendto(texto.encode(), IP_PORTA_SERVIDOR)
print("Dados enviados!")

dados, endereco_servidor = socket_cliente.recvfrom(1024)
print(f"Resposta do servidor: {dados.decode()}")

socket_cliente.close()
