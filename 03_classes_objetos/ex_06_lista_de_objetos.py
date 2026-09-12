class Servidor:
    def __init__(self, nome: str, ip: str, status: str = "ativo", vlan: int = 1) -> None:
        self.nome = nome
        self.ip = ip
        self.status = status
        self.vlan = vlan

    def esta_ativo(self) -> bool:
        return self.status == "ativo"

    def __str__(self) -> str:
        marca = "on " if self.esta_ativo() else "off"
        return f"[{marca}] {self.nome:<10} {self.ip:<12} vlan {self.vlan}"


inventario = [
    Servidor("srv-web", "10.0.0.10"),
    Servidor("srv-db", "10.0.0.11", "inativo", 20),
    Servidor("srv-dns", "10.0.0.12", "ativo", 20),
]

for s in inventario:
    print(s)

ativos = 0
for s in inventario:
    if s.esta_ativo():
        ativos += 1

print(f"ativos: {ativos} de {len(inventario)}")
