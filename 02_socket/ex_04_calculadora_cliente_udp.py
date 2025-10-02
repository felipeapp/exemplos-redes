import socket

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP_PORTA = ("127.0.0.1", 5000)
dados = f"{numero1};{numero2};{operacao}".encode()

socket_cliente.sendto(dados, IP_PORTA)
print("Dados enviados!")

dados, endereco_servidor = socket_cliente.recvfrom(1024)
print(f"Resposta do servidor:\n{dados.decode()}")

socket_cliente.close()
