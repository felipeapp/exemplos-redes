# Lidando com uma lista de dispositivos de forma orientada a objetos


class Dispositivo:
    def __init__(self, nome: str, ip: str, ativo: bool) -> None:
        self.nome = nome
        self.ip = ip
        self.ativo = ativo

    def imprimir(self) -> None:
        print(f"Nome: {self.nome}, IP: {self.ip}, Ativo: {self.ativo}")


dispositivos = [
    Dispositivo("Roteador", "10.230.0.2", True),
    Dispositivo("Switch", "10.230.0.3", True),
    Dispositivo("Servidor", "10.230.0.4", False),
]

for dispositivo in dispositivos:
    dispositivo.imprimir()
