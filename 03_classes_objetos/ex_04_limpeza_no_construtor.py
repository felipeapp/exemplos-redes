class Servidor:
    def __init__(self, nome: str, ip: str, status: str = "ativo") -> None:
        self.nome = nome.strip()
        self.ip = ip.strip()
        self.status = status.strip().lower()


sujo = Servidor("  SRV-Web ", " 10.0.0.10  ", "ATIVO")
print(f"nome='{sujo.nome}'")
print(f"ip='{sujo.ip}'")
print(f"status='{sujo.status}'")
