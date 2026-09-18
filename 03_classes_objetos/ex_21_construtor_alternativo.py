class Dispositivo:
    def __init__(self, nome: str, ip: str, status: str = "ativo") -> None:
        self.nome = nome.strip()
        self.ip = ip.strip()
        self.status = status.strip().lower()

    @classmethod
    def de_texto(cls, linha: str) -> Dispositivo:
        partes = [p.strip() for p in linha.split(";")]
        if len(partes) == 2:
            nome, ip = partes
            return cls(nome, ip)
        nome, ip, status = partes
        return cls(nome, ip, status)

    def __str__(self) -> str:
        return f"{self.nome:<10} {self.ip:<12} {self.status}"


print(Dispositivo("rt-core", "10.0.0.1"))
print(Dispositivo.de_texto("sw-01 ; 10.0.0.2"))
print(Dispositivo.de_texto("srv-web;10.0.0.10;inativo"))
