class Dispositivo:
    total = 0

    def __init__(self, nome: str) -> None:
        self.nome = nome
        Dispositivo.total += 1


rt = Dispositivo("rt-core")
sw = Dispositivo("sw-01")
srv = Dispositivo("srv-web")

print(f"total de dispositivos: {Dispositivo.total}")
print(f"nomes: {rt.nome} | {sw.nome} | {srv.nome}")
print(f"total de dispositivos: {rt.total} | {sw.total} | {srv.total}")
