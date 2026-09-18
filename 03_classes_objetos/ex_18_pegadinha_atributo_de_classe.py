class Dispositivo:
    total = 0

    def __init__(self, nome: str) -> None:
        self.nome = nome


rt = Dispositivo("rt-core")
sw = Dispositivo("sw-01")

Dispositivo.total = 10
print(f"lendo pelo objeto: {rt.total} {sw.total}")

rt.total = 99
print(f"rt.total  : {rt.total}")
print(f"sw.total  : {sw.total}")
print(f"da classe : {Dispositivo.total}")
