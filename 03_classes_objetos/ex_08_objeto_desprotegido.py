class Servidor:
    def __init__(self, nome: str, status: str = "ativo") -> None:
        self.nome = nome
        self.status = status

    def esta_ativo(self) -> bool:
        return self.status == "ativo"


srv = Servidor("srv-web")
print("status inicial:", srv.status)

srv.status = "banana"
print("status agora  :", srv.status)
print("esta_ativo()  :", srv.esta_ativo(), "<- False, mas pelo motivo errado")
