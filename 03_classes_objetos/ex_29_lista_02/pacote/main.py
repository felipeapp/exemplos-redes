from rede import Host, Sala


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
