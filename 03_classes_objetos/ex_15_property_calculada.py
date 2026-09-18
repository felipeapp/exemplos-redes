class Servidor:
    def __init__(self, nome: str, ip: str) -> None:
        self.nome = nome.strip()
        self.ip = ip.strip()

    @property
    def etiqueta(self) -> str:
        return f"{self.nome}@{self.ip}"


srv = Servidor("srv-dns", "10.0.0.12")
print(f"srv.etiqueta = {srv.etiqueta}")

srv.ip = "10.0.0.99"
print(f"srv.etiqueta = {srv.etiqueta}")
