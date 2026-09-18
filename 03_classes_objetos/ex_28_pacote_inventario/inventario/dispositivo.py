from inventario.validacao import ip_valido, status_valido, vlan_valida


class Dispositivo:
    total = 0

    def __init__(self, nome: str, ip: str, status: str = "ativo", vlan: int = 1) -> None:
        self.nome = nome.strip()
        self._ip = "0.0.0.0"
        self._status = "inativo"
        self._vlan = 1
        self.ip = ip
        self.status = status
        self.vlan = vlan
        Dispositivo.total += 1

    @property
    def ip(self) -> str:
        return self._ip

    @ip.setter
    def ip(self, novo: str) -> None:
        if not ip_valido(novo):
            print(f"IP invalido, ignorado: {novo!r}")
            return
        self._ip = str(novo).strip()

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, novo: str) -> None:
        if not status_valido(novo):
            print(f"status invalido, ignorado: {novo!r}")
            return
        self._status = str(novo).strip().lower()

    @property
    def vlan(self) -> int:
        return self._vlan

    @vlan.setter
    def vlan(self, novo: int) -> None:
        if not vlan_valida(novo):
            print(f"VLAN invalida, ignorada: {novo!r}")
            return
        self._vlan = novo

    @classmethod
    def de_texto(cls, linha: str) -> Dispositivo:
        partes = [p.strip() for p in linha.split(";")]
        nome, ip = partes[0], partes[1]
        status = partes[2] if len(partes) > 2 else "ativo"
        vlan = int(partes[3]) if len(partes) > 3 else 1
        return cls(nome, ip, status, vlan)

    @classmethod
    def quantos(cls) -> int:
        return cls.total

    def esta_ativo(self) -> bool:
        return self._status == "ativo"

    def __str__(self) -> str:
        marca = "on " if self.esta_ativo() else "off"
        return f"[{marca}] {self.nome:<10} {self.ip:<12} vlan {self.vlan}"


if __name__ == "__main__":
    print(Dispositivo("rt-core", "10.0.0.1"))
