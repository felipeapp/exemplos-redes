"""
Exercicio 06 | Composicao: o pedido e feito de itens.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie ItemPedido (produto, quantidade) com subtotal(), e Pedido
    com adicionar(produto, quantidade) e total(). O proprio pedido
    cria seus itens. Recuse quantidade menor ou igual a zero e, se o
    produto ja estiver no pedido, some a quantidade em vez de criar
    outro item.

Rode:  python3 ex_06_composicao_pedido.py
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


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self) -> int:
        return self.produto.preco * self.quantidade

    def __str__(self) -> str:
        return (f"{self.quantidade}x {self.produto.nome:<14} "
                f"{reais(self.subtotal()):>10}")


class Pedido:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        if quantidade <= 0:
            print("quantidade invalida:", quantidade)
            return
        for item in self.itens:
            if item.produto is produto:          # ja existe: soma
                item.quantidade += quantidade
                return
        self.itens.append(ItemPedido(produto, quantidade))   # cria DENTRO

    def total(self) -> int:
        return sum(item.subtotal() for item in self.itens)


# --- demonstracao ----------------------------------------------------
suco = Produto(1, "Suco de caju", 800)
feijoada = Produto(2, "Feijoada", 4500)

pedido = Pedido(1)
pedido.adicionar(feijoada, 1)
pedido.adicionar(suco, 1)
pedido.adicionar(suco, 2)             # vira um item com quantidade 3
pedido.adicionar(suco, 0)             # recusado

for item in pedido.itens:
    print(item)
print("total:", reais(pedido.total()))

# --- por que assim ---------------------------------------------------
# Na composicao, a parte nasce dentro do todo: quem cria o
# ItemPedido e o proprio pedido. Por isso as regras -- quantidade
# valida, nao repetir produto -- ficam escritas em um lugar so. E
# cada item sabe calcular o proprio subtotal; o pedido so soma.
