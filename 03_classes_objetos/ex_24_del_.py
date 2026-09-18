class ConexaoRuim:
    def __init__(self, destino: str) -> None:
        self.destino = destino
        print(f"Abrindo conexao com {self.destino}")

    def __del__(self) -> None:
        print(f"Fechando conexao com {self.destino}")


c = ConexaoRuim("10.0.0.1")
c = None
print("Finalizando programa!")
