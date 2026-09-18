class Dispositivo:
    total = 0

    def __init__(self, nome: str) -> None:
        self.nome = nome
        Dispositivo.total += 1

    @classmethod
    def quantos(cls) -> int:
        return cls.total

    @classmethod
    def zerar_contagem(cls) -> None:
        cls.total = 0


Dispositivo("rt-core")
Dispositivo("sw-01")
print(f"quantos: {Dispositivo.quantos()}")

Dispositivo.zerar_contagem()
print(f"depois de zerar: {Dispositivo.quantos()}")
