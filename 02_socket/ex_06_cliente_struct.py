import socket
import struct

from ex_06_comum import (
    FORMATO_REQUISICAO,
    FORMATO_RESPOSTA,
    SERVIDOR_IP,
    SERVIDOR_PORTA,
    TAMANHO_RESPOSTA,
)

nota1 = int(input("Digite a primeira nota [0-100]: "))
nota2 = int(input("Digite a segunda nota [0-100]: "))
nota3 = int(input("Digite a terceira nota [0-100]: "))
nota4 = int(input("Digite a quarts nota [0-100]: "))

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((SERVIDOR_IP, SERVIDOR_PORTA))

dados = struct.pack(FORMATO_REQUISICAO, nota1, nota2, nota3, nota4)
socket_cliente.sendall(dados)
print("Dados enviados!")

resposta = socket_cliente.recv(TAMANHO_RESPOSTA)
media, situacao = struct.unpack(FORMATO_RESPOSTA, resposta)
situacao = situacao.decode().strip()

socket_cliente.close()

print(f"A média foi {media} e a situação foi {situacao}!")
