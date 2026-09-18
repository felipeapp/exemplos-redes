class Servidor:
    def __init__(self, ip: str) -> None:
        self.__ip = ip


srv = Servidor("10.0.0.10")
# print(srv.__ip) # Isso vai gerar erro
print(f"srv._Servidor__ip = {srv._Servidor__ip}")
