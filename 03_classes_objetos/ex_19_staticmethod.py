class Dispositivo:
    def __init__(self, nome: str, ip: str) -> None:
        self.nome = nome
        self.ip = ip

    @staticmethod
    def ip_valido(texto: str) -> bool:
        partes = str(texto).split(".")
        if len(partes) != 4:
            return False
        return all(p.isdigit() and 0 <= int(p) <= 255 for p in partes)


print(Dispositivo.ip_valido("10.0.0.1"))
print(Dispositivo.ip_valido("10.0.0.999"))
print(Dispositivo.ip_valido("banana"))

rt = Dispositivo("rt-core", "10.0.0.1")
print(rt.ip_valido("192.168.0.1"))
