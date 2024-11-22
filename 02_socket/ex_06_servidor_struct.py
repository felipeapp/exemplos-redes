import socket
import struct

from ex_06_comum import (
    FORMATO_REQUISICAO,
    FORMATO_RESPOSTA,
    SERVIDOR_PORTA,
    TAMANHO_REQUISICAO,
)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(("0.0.0.0", SERVIDOR_PORTA))
socket_servidor.listen(2)

while True:
    print("\nEsperando um cliente conectar...")
    socket_cliente, endereco_cliente = socket_servidor.accept()
    print(f"Cliente conectado: {endereco_cliente}")

    print("Esperando dados do cliente...")
    dados = socket_cliente.recv(TAMANHO_REQUISICAO)
    nota1, nota2, nota3, nota4 = struct.unpack(FORMATO_REQUISICAO, dados)
    print("Dados recebidos!")

    media = (nota1 + nota2 + nota3 + nota4) // 4

    if media >= 60:
        situacao = "aprovado"
    elif media < 20:
        situacao = "reprovado"
    else:
        situacao = "recuperação"

    resposta = struct.pack(FORMATO_RESPOSTA, media, situacao.encode())
    socket_cliente.sendall(resposta)
    print(f"Resposta enviada: {media} {situacao}!")

    socket_cliente.close()
