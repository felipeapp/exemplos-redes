"""
Exercicio 14 | Hierarquia com varios niveis.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie BebidaAlcoolica, que herda de Bebida e acrescenta o teor
    alcoolico. Mostre que ela recebe o que e de Produto e o que e de
    Bebida.

Rode:  python3 ex_14_varios_niveis.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, codigo: int, nome: str, preco: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class Bebida(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(codigo, nome, preco)
        self.volume_ml = volume_ml

    def eh_grande(self) -> bool:
        return self.volume_ml >= 1000


class BebidaAlcoolica(Bebida):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int, teor: float) -> None:
        super().__init__(codigo, nome, preco, volume_ml)
        self.teor = teor

    def exige_maioridade(self) -> bool:
        return True


# --- demonstracao ----------------------------------------------------
cerveja = BebidaAlcoolica(9, "Cerveja", 1200, 600, 4.5)

print("de Produto        :", cerveja.nome, reais(cerveja.preco))
print("de Bebida         :", cerveja.volume_ml, "ml, grande?", cerveja.eh_grande())
print("de BebidaAlcoolica:", cerveja.teor, "% - maioridade?",
      cerveja.exige_maioridade())

# --- por que assim ---------------------------------------------------
# Cada super() chama o nivel de cima, que chama o seguinte: a
# cerveja herda da cadeia inteira. Mas hierarquias profundas ficam
# dificeis de entender -- dois ou tres niveis costumam bastar.
