class Host:
    def __init__(self, nome: str, ip: str, vlan: int) -> None:
        self.nome = nome
        self.ip = ip
        self.vlan = vlan

    def __str__(self) -> str:
        return f"Nome: {self.nome}, IP: {self.ip}, VLAN: {self.vlan}"

    @classmethod
    def de_linha(cls, linha: str) -> Host:
        nome, ip, vlan = linha.split(",")
        return cls(nome.strip(), ip.strip(), int(vlan))


def main() -> None:
    h1 = Host("Servidor-1", "10.230.0.2", 20)
    h2 = Host("Servidor-2", "10.230.0.3", 30)
    h3 = Host.de_linha("Servidor-3,10.230.0.4,40")
    h4 = Host.de_linha("Servidor-4 ,   10.230.0.5,    50")

    print("H1", h1)
    print("H2", h2)
    print("H3", h3)
    print("H4", h4)

    linhas = [
        "Cliente-1,10.225.0.2,20",
        "Cliente-2,10.225.0.3,30",
        "",
        "    ",
        "Cliente-3,10.225.0.4,40",
        "Cliente-4 ,   10.225.0.5,    50",
        "#Cliente-5,10.225.0.6,60",
    ]

    hosts = []
    for elem in linhas:
        linha = elem.strip()
        if linha and not linha.startswith("#"):
            hosts.append(Host.de_linha(linha))

    print("Hosts:")
    for h in hosts:
        print(h)


if __name__ == "__main__":
    main()
