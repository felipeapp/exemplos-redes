"""
Exercicio 11 | Sobrecarga de operadores: __eq__, __lt__ e __len__.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Faca dois produtos serem iguais quando tiverem o mesmo codigo;
    permita ordenar produtos pelo preco com sorted(); e faca
    len(pedido) devolver o total de unidades.

Rode:  python3 ex_11_operadores.py
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

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __lt__(self, outro: Produto) -> bool:
        return self.preco < outro.preco

    def __str__(self) -> str:
        return f"{self.nome:<16} {reais(self.preco)}"

    def __hash__(self) -> int:
        return hash(self.codigo)


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade


class Pedido:
    def __init__(self) -> None:
        self.itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        self.itens.append(ItemPedido(produto, quantidade))

    def __len__(self) -> int:  # unidades, nao linhas
        return sum(item.quantidade for item in self.itens)


# --- demonstracao ----------------------------------------------------
a = Produto(1, "Suco de caju", 800)
b = Produto(1, "Suco de Caju", 850)  # cadastrado de novo
print("a == b:", a == b, "| a is b:", a is b)

cardapio = [Produto(2, "Feijoada", 4500), a, Produto(3, "Pudim", 1200)]
print("do mais barato ao mais caro:")
for p in sorted(cardapio):
    print("  ", p)
print("mais barato:", min(cardapio).nome)

pedido = Pedido()
pedido.adicionar(a, 2)
pedido.adicionar(cardapio[0])
print("itens no pedido   :", len(pedido.itens))
print("unidades no pedido:", len(pedido))

# --- por que assim ---------------------------------------------------
# Operadores tambem sao metodos. Definindo __eq__, voce decide o que
# e "igual" no seu negocio; com __lt__, sorted(), min() e max()
# passam a funcionar; com __len__, len() devolve o tamanho que faz
# sentido. O 'is' continua comparando identidade.
