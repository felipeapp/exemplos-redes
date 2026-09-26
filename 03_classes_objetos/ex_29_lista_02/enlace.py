class Enlace:
    def __init__(self, nome: str, banda: int) -> None:
        self.nome = nome.strip().upper()

        if isinstance(banda, int) and banda > 0:
            self.banda = banda
        else:
            print(f"A banda deve ser um valor positivo. Valor informado: {banda}")


def main() -> None:
    Enlace("Enlace do Programador 1", 100)
    Enlace("Enlace do Programador 2", 0)
    Enlace("Enlace do Programador 3", -50)
    Enlace("Enlace do Programador 3", "mil")  # pyright: ignore[reportArgumentType]


if __name__ == "__main__":
    main()
