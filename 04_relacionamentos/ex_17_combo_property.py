"""
Exercicio 17 | Sobrescrevendo uma property: o combo.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie Combo, um Produto que reune outros produtos e tem um
    desconto percentual. Sobrescreva a property preco para calcula-
    lo: soma dos produtos menos o desconto. Mostre que o __str__
    herdado ja usa o preco calculado.

Rode:  python3 ex_17_combo_property.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, codigo: int, nome: str, preco: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self._preco = preco

    @property
    def preco(self) -> int:
        return self._preco

    def reajustar(self, percentual: int) -> None:
        self._preco += self._preco * percentual // 100

    def __str__(self) -> str:
        return f"{self.nome:<18} {reais(self.preco)}"


class Combo(Produto):
    def __init__(self, codigo: int, nome: str, desconto: int) -> None:
        super().__init__(codigo, nome, 0)
        self.produtos: list[Produto] = []
        self.desconto = desconto           # percentual

    def incluir(self, *produtos: Produto) -> None:
        for p in produtos:
            self.produtos.append(p)

    @property
    def preco(self) -> int:                       # calculado, nao guardado
        soma = sum(p.preco for p in self.produtos)
        return soma - soma * self.desconto // 100


# --- demonstracao ----------------------------------------------------
feijoada = Produto(2, "Feijoada", 4500)
suco = Produto(1, "Suco de caju", 800)

combo = Combo(10, "Almoco completo", 10)
combo.incluir(feijoada, suco)

print(feijoada)
print(suco)
print(combo)                 # o __str__ de Produto usou o preco do Combo

suco.reajustar(10)           # o suco ficou 10% mais caro...
print(suco)
print(combo)                 # ...e o combo acompanhou sozinho

# --- por que assim ---------------------------------------------------
# O __str__ foi escrito em Produto e ninguem o reescreveu. Mas
# quando ele pede self.preco, o self e um combo -- e o Python
# escolhe a versao do combo. Isso e ligacao dinamica, assunto que
# vem mais adiante. Repare tambem: o Combo e um Produto E tem
# produtos -- heranca e composicao juntas.
