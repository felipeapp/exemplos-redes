"""
Exercicio 19 | Downcasting com isinstance.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    O entregador precisa saber quantos mililitros de bebida vao no
    pedido para escolher a caixa termica. Escreva
    volume_bebidas(itens), que soma volume_ml * quantidade apenas
    dos itens que sao bebidas. Mostre tambem a diferenca entre
    isinstance e type.

Rode:  python3 ex_19_downcasting_isinstance.py
"""


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco


class Prato(Produto):
    pass


class Bebida(Produto):
    def __init__(self, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(nome, preco)
        self.volume_ml = volume_ml


class BebidaAlcoolica(Bebida):
    def __init__(self, nome: str, preco: int, volume_ml: int, teor: float) -> None:
        super().__init__(nome, preco, volume_ml)
        self.teor = teor


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade


def volume_bebidas(itens: list[ItemPedido]) -> int:
    total_ml = 0
    for item in itens:
        if isinstance(item.produto, Bebida):   # e uma bebida?
            total_ml += item.produto.volume_ml * item.quantidade
    return total_ml


# --- demonstracao ----------------------------------------------------
feijoada = Prato("Feijoada", 4500)
suco = Bebida("Suco de caju", 800, 500)
cerveja = BebidaAlcoolica("Cerveja", 1200, 600, 4.5)

itens = [ItemPedido(feijoada, 1), ItemPedido(suco, 2), ItemPedido(cerveja, 1)]
print("volume de bebidas:", volume_bebidas(itens), "ml")

print("isinstance(cerveja, Bebida) :", isinstance(cerveja, Bebida))
print("isinstance(cerveja, Produto):", isinstance(cerveja, Produto))
print("type(cerveja) is Bebida     :", type(cerveja) is Bebida)
print("issubclass(Bebida, Produto) :", issubclass(Bebida, Produto))

# --- por que assim ---------------------------------------------------
# Visto como Produto, o objeto so garante o que Produto tem. Para
# usar o volume_ml, e preciso descer -- e em Python se pergunta
# antes, com isinstance. Ele respeita a hierarquia: a cerveja e uma
# Bebida. O type() compara so a classe exata e erraria aqui.
