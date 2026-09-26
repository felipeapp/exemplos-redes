PROTOCOLOS = ["tcp", "udp"]
PORTA_MIN = 1
PORTA_MAX = 65535


class Service:
    def __init__(self, nome: str, protocolo: str, porta: int) -> None:
        self.nome = nome.strip().lower()

        if protocolo.lower() in PROTOCOLOS:
            self.protocolo = protocolo.lower()
        else:
            print(f"Protocolo inválido. Valor informado: {protocolo}")

        if isinstance(porta, int) and PORTA_MIN <= porta <= PORTA_MAX:
            self.porta = porta
        else:
            print(f"Porta inválida. Valor informado: {porta}")

    def __str__(self) -> str:
        return f"{self.nome} {self.porta}/{self.protocolo}"


def main() -> None:
    ssh = Service("SSH", "tcp", 22)
    print(ssh)

    Service("DNS", "icmp", 70000)


if __name__ == "__main__":
    main()
