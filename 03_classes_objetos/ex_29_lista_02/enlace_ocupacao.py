LIMITE_SATURACAO = 80


class EnlaceOcupacao:
    def __init__(self, banda_mbps: int, uso_mbps: int = 0) -> None:
        if banda_mbps >= uso_mbps:
            self.banda_mbps = banda_mbps
            self.uso_mbps = uso_mbps
        else:
            print("Uso não pode ser maior que a banda!")

    def registrar_uso(self, mbps: int) -> bool:
        sucesso = False

        if mbps <= self.banda_mbps:
            self.uso_mbps = mbps
            sucesso = True

        return sucesso

    @property
    def ocupacao(self) -> float:
        return (self.uso_mbps / self.banda_mbps) * 100

    @property
    def saturado(self) -> bool:
        return self.ocupacao > LIMITE_SATURACAO


def main() -> None:
    enlace = EnlaceOcupacao(100)

    print(enlace.registrar_uso(50))
    print(f"Ocupação: {enlace.ocupacao:.2f}%")
    print(f"Saturado: {enlace.saturado}")

    print(enlace.registrar_uso(80))
    print(f"Ocupação: {enlace.ocupacao:.2f}%")
    print(f"Saturado: {enlace.saturado}")

    print(enlace.registrar_uso(100))
    print(f"Ocupação: {enlace.ocupacao:.2f}%")
    print(f"Saturado: {enlace.saturado}")

    print(enlace.registrar_uso(120))
    print(f"Ocupação: {enlace.ocupacao:.2f}%")
    print(f"Saturado: {enlace.saturado}")


if __name__ == "__main__":
    main()
