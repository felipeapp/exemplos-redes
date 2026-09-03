# Lidando com uma lista de dispositivos de forma estruturada

dispositivos = []


def adicionar_dispositivo(nome: str, ip: str, ativo: bool) -> None:
    dispositivos.append([nome, ip, ativo])


def imprimir(dispositivo: list) -> None:
    print(f"Nome: {dispositivo[0]}, IP: {dispositivo[1]}, Ativo: {dispositivo[2]}")


adicionar_dispositivo("Roteador", "10.230.0.2", True)
adicionar_dispositivo("Switch", "10.230.0.3", True)
adicionar_dispositivo("Servidor", "10.230.0.4", False)

for dispositivo in dispositivos:
    imprimir(dispositivo)
