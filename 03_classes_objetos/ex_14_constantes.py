STATUS_VALIDOS = ("ativo", "inativo", "manutencao")
VLAN_PADRAO = 1


class Servidor:
    def __init__(self, nome: str, status: str = "ativo", vlan: int = VLAN_PADRAO) -> None:
        self.nome = nome.strip()
        self._status = "inativo"
        self.status = status
        self.vlan = vlan

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, novo: str) -> None:
        novo = str(novo).strip().lower()
        if novo not in STATUS_VALIDOS:
            print(f"status invalido, ignorado: {novo!r}")
            return
        self._status = novo

    def esta_ativo(self) -> bool:
        return self._status == "ativo"


srv = Servidor("srv-web")

srv.status = "banana"
print("status continua:", srv.status)

srv.status = "  MANUTENCAO "
print("status aceito e normalizado:", srv.status)
print("esta_ativo():", srv.esta_ativo())
