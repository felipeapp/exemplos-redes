class Switch:
    def __init__(self, nome: str, total_portas: int = 24) -> None:
        self.nome = nome.strip().upper()
        self.total_portas = total_portas
        self.portas_ocupadas = 0

    def conectar(self) -> bool:
        sucesso = False

        if self.portas_ocupadas < self.total_portas:
            self.portas_ocupadas += 1
            sucesso = True

        return sucesso

    def desconectar(self) -> bool:
        sucesso = False

        if self.portas_ocupadas > 0:
            self.portas_ocupadas -= 1
            sucesso = True

        return sucesso

    def portas_livres(self) -> int:
        return self.total_portas - self.portas_ocupadas


def main() -> None:
    sw = Switch("Switch do Programador", 4)

    print(sw.desconectar())

    print(sw.conectar())
    print(sw.conectar())
    print(sw.conectar())
    print(sw.conectar())
    print(sw.conectar())

    print(sw.portas_livres())


if __name__ == "__main__":
    main()
