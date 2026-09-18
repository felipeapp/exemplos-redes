class Servidor:
    def __init__(self, ip: str) -> None:
        self._ip = "0.0.0.0"
        self.ip = ip

    @property
    def ip(self) -> str:
        return self._ip

    @ip.setter
    def ip(self, novo: str) -> None:
        novo = str(novo).strip()
        if novo.count(".") != 3:
            print(f"IP invalido, ignorado: {novo!r}")
            return
        self._ip = novo


srv = Servidor("10.0.0.10")

srv.ip = "banana"
print(f"ip continua: {srv.ip}")

srv.ip = "42"
print(f"ip continua: {srv.ip}")

srv.ip = "10.0.0.99"
print(f"ip aceito  : {srv.ip}")
