class Servidor:
    def __init__(self, ip: str) -> None:
        self._ip = ip


srv = Servidor("10.0.0.10")
print("srv._ip =", srv._ip, "<- funciona: e um aviso, nao uma tranca")
