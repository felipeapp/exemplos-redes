from dataclasses import dataclass
from datetime import datetime


@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int
    medida: str
    id: int = 0
    cadastro: datetime | None = None

    def __repr__(self) -> str:
        cadastro_formatado = self.cadastro.strftime("%d/%m/%Y %H:%M:%S") if self.cadastro else "-"
        return (
            f"###\nID: {self.id}\nNome: {self.nome}\nPreço: R${self.preco:.2f}\n"
            f"Quantidade: {self.quantidade}\nMedida: {self.medida}\nCadastro: {cadastro_formatado}"
        )
