class Equipamento:
    sequencial = 0

    def __init__(self, nome: str) -> None:
        Equipamento.sequencial += 1
        self.nome = nome
        self.patrimonio = f"PAT-{Equipamento.sequencial:04d}"

    def __str__(self) -> str:
        return f"Equipamento: {self.nome}, Patrimônio: {self.patrimonio}"

    @classmethod
    def quantos(cls) -> int:
        return cls.sequencial


def main() -> None:
    equipamento1 = Equipamento("Notebook")
    equipamento2 = Equipamento("Impressora")
    equipamento3 = Equipamento("Monitor")

    print(equipamento1)
    print(equipamento2)
    print(equipamento3)

    print(f"Total de equipamentos: {Equipamento.quantos()}")


if __name__ == "__main__":
    main()
