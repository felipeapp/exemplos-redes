class Vlan:
    def __init__(self, numero: int, nome: str) -> None:
        self.numero = numero
        self.nome = nome.strip().capitalize()

    def __str__(self) -> str:
        return f"VLAN {self.numero} - {self.nome}"


def main() -> None:
    vlan1 = Vlan(10, "Marketing")
    vlan2 = Vlan(20, "Financeiro")
    vlan3 = Vlan(30, "    tecnologia da INFORMAÇÃO    ")

    print(vlan1)
    print(vlan2)
    print(vlan3)


if __name__ == "__main__":
    main()
