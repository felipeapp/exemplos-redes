class Servidor:
    def __init__(self, ip: str) -> None:
        self._ip = ip

    def get_ip(self) -> str:
        return self._ip

    def set_ip(self, novo: str) -> None:
        self._ip = novo


srv = Servidor("10.0.0.10")
srv.set_ip("10.0.0.99")
print(f"srv.get_ip() = {srv.get_ip()} <- funciona, mas e verboso")
