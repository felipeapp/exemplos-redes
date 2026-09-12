class Servidor:
    def __init__(self, nome: str, ip: str, status: str = "ativo", vlan: int = 1) -> None:
        self.nome = nome
        self.ip = ip
        self.status = status
        self.vlan = vlan


padrao = Servidor("srv-web", "10.0.0.10")
completo = Servidor("srv-db", "10.0.0.11", "inativo", 20)

print(f"{padrao.nome}: status={padrao.status} vlan={padrao.vlan}")
print(f"{completo.nome}: status={completo.status} vlan={completo.vlan}")
