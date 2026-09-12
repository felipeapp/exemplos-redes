class Servidor:
    def __init__(self, nome: str, status: str = "ativo") -> None:
        self.nome = nome
        self.status = status

    def esta_ativo(self) -> bool:
        return self.status == "ativo"


class Rack:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.servidores: list[Servidor] = []

    def adicionar(self, servidor: Servidor) -> None:
        self.servidores.append(servidor)

    def total_ativos(self) -> int:
        return len([s for s in self.servidores if s.esta_ativo()])

    def __str__(self) -> str:
        return f"Rack {self.nome}: {len(self.servidores)} servidores, {self.total_ativos()} ativos"


rack = Rack("A1")
rack.adicionar(Servidor("srv-web"))
rack.adicionar(Servidor("srv-db", "inativo"))
rack.adicionar(Servidor("srv-dns"))

print(rack)
