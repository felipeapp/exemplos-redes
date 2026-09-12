class Servidor:
    def __init__(self, nome: str, ip: str, status: str) -> None:
        self.nome = nome
        self.ip = ip
        self.status = status

    def esta_ativo(self) -> bool:
        return self.status == "ativo"


srv = Servidor("srv-web", "10.0.0.10", "ativo")
print(f"{srv.nome} criado ja completo, ativo = {srv.esta_ativo()}")

# Tentar criar sem status vai gerar erro
# Servidor("srv-db", "10.0.0.11")
