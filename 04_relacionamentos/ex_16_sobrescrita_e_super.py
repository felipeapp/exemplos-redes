"""
Exercicio 16 | Sobrescrita, com e sem super().

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Escreva descricao() em Produto. Sobrescreva em Bebida e em
    Prato, reaproveitando a versao da mae com super(). Depois
    sobrescreva tambem o __str__ de Bebida, sem super(), e compare
    com o Prato, que nao o sobrescreve.

Rode:  python3 ex_16_sobrescrita_e_super.py
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

    def descricao(self) -> str:
        return f"{self.nome} - {reais(self.preco)}"

    def __str__(self) -> str:
        return f"{self.nome:<16} {reais(self.preco)}"


class Bebida(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(codigo, nome, preco)
        self.volume_ml = volume_ml

    def descricao(self) -> str:                       # estende a da mae
        return f"{super().descricao()} - {self.volume_ml} ml"

    def __str__(self) -> str:                         # substitui a da mae
        return f"{self.nome} ({self.volume_ml} ml)  {reais(self.preco)}"


class Prato(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, serve: int = 1) -> None:
        super().__init__(codigo, nome, preco)
        self.serve = serve

    def descricao(self) -> str:
        return f"{super().descricao()} - serve {self.serve}"


# --- demonstracao ----------------------------------------------------
suco = Bebida(1, "Suco de caju", 800, 500)
feijoada = Prato(2, "Feijoada", 4500, serve=2)

print(suco.descricao())
print(feijoada.descricao())
print(suco)            # __str__ sobrescrito em Bebida
print(feijoada)        # __str__ herdado de Produto

# --- por que assim ---------------------------------------------------
# Sobrescrever e redefinir na filha um metodo da mae, com o mesmo
# nome e os mesmos parametros. Com super(), a filha estende em vez
# de reescrever: se o formato mudar em Produto, Bebida e Prato
# acompanham. O Python procura o metodo na classe do objeto e sobe
# ate achar.
