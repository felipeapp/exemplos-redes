class Servidor:
    def __init__(self, nome: str, ip: str, status: str = "ativo", vlan: int = 1) -> None:
        self.nome = nome.strip()
        self.ip = ip.strip()
        self.status = status.strip().lower()
        self.vlan = vlan

    def esta_ativo(self) -> bool:
        return self.status == "ativo"

    def __str__(self) -> str:
        marca = "on " if self.esta_ativo() else "off"
        return f"[{marca}] {self.nome:<10} {self.ip:<12} vlan {self.vlan}"


print(Servidor("srv-web", "10.0.0.10"))
print(Servidor("srv-db", "10.0.0.11", "inativo", 20))
