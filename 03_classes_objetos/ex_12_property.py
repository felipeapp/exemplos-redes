class Servidor:
    def __init__(self, ip: str) -> None:
        self._ip = ip

    @property
    def ip(self) -> str:
        return self._ip


srv = Servidor("10.0.0.10")
print("srv.ip =", srv.ip, "<- parece atributo, mas e um metodo")
