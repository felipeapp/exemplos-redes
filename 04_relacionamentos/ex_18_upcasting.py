"""
Exercicio 18 | Upcasting: tratar todos como Produto.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Monte um cardapio com prato, bebida e combo. Escreva as funcoes
    total() e mais_barato(), que recebem uma lista de Produto, e
    mostre que elas servem para qualquer subtipo.

Rode:  python3 ex_18_upcasting.py
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


class Prato(Produto):
    pass


class Bebida(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(codigo, nome, preco)
        self.volume_ml = volume_ml


class Combo(Produto):
    def __init__(self, codigo: int, nome: str, desconto: int, *produtos: Produto) -> None:
        super().__init__(codigo, nome, 0)
        self.produtos = list(produtos)
        self.desconto = desconto

    @property
    def preco(self) -> int:
        soma = sum(p.preco for p in self.produtos)
        return soma - soma * self.desconto // 100


def total(produtos: list[Produto]) -> int:
    return sum(p.preco for p in produtos)


def mais_barato(produtos: list[Produto]) -> Produto:
    menor = produtos[0]
    for p in produtos:
        if p.preco < menor.preco:
            menor = p
    return menor


# --- demonstracao ----------------------------------------------------
feijoada = Prato(1, "Feijoada", 4500)
suco = Bebida(2, "Suco de caju", 800, 500)
combo = Combo(3, "Almoco completo", 10, feijoada, suco)

cardapio = [feijoada, suco, combo]     # tres tipos, vistos como Produto
for p in cardapio:
    print(f"{p.nome:<16} {reais(p.preco)}")
print("total:", reais(total(cardapio)))
print("mais barato:", mais_barato(cardapio).nome)

# --- por que assim ---------------------------------------------------
# Todo prato, bebida e combo e um Produto, entao pode ser usado onde
# se espera um Produto. As funcoes nao precisam saber quem e quem --
# e funcionarao tambem para subtipos que ainda nem existem. Subir na
# hierarquia e sempre seguro.
