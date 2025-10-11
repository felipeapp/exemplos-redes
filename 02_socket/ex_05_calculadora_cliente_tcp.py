import socket

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_PORTA = ("127.0.0.1", 5000)
socket_cliente.connect(IP_PORTA)

dados = f"{numero1};{numero2};{operacao}".encode()
socket_cliente.sendall(dados)
print("Dados enviados!")

dados = socket_cliente.recv(1024)
print(f"Resposta do servidor:\n{dados.decode()}")

socket_cliente.close()
