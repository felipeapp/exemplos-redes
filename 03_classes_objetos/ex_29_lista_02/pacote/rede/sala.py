from rede.host import Host


class Sala:
    def __init__(self) -> None:
        self.hosts = []

    def adicionar(self, host: Host) -> bool:
        if self.buscar(host.nome) is None:
            self.hosts.append(host)
            return True
        return False

    def buscar(self, nome_host: str) -> Host | None:
        for host in self.hosts:
            if host.nome == nome_host:
                return host
        return None

    def remover(self, nome_host: str) -> bool:
        host = self.buscar(nome_host)
        if host is not None:
            self.hosts.remove(host)
            return True
        return False


def main() -> None:
    sala = Sala()
    h1 = Host("Servidor-1", "10.230.0.1", 10)

    sala.adicionar(h1)
    h2 = sala.buscar("Servidor-1")

    print(f"Host 1: {h1}")
    print(f"Host 2: {h2}")

    print(f"É o mesmo objeto? {h1 is h2}")

    h1.nome = "Impressora-2"
    print(f"Nome do host 1: {h1}")
    print(f"Nome do host 2: {h2}")


if __name__ == "__main__":
    main()
