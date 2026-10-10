"""
Exercicio 07 | Por que a parte da composicao nao e compartilhada.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Mostre o problema de criar um ItemPedido de fora e coloca-lo em
    dois pedidos. Depois mostre que, deixando o pedido criar seus
    itens, o problema desaparece.

Rode:  python3 ex_07_por_que_nao_compartilhar.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade


class Pedido:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        self.itens.append(ItemPedido(produto, quantidade))


# --- demonstracao ----------------------------------------------------
suco = Produto("Suco de caju", 800)

print("1) item criado de fora e compartilhado:")
item = ItemPedido(suco, 2)
p1, p2 = Pedido(1), Pedido(2)
p1.itens.append(item)
p2.itens.append(item)
p1.itens[0].quantidade = 5            # o cliente 1 mudou de ideia
print("   pedido 2 agora tem", p2.itens[0].quantidade, "sucos  <- errado!")

print("2) cada pedido cria o proprio item:")
p1, p2 = Pedido(1), Pedido(2)
p1.adicionar(suco, 2)
p2.adicionar(suco, 2)
p1.itens[0].quantidade = 5
print("   pedido 2 continua com", p2.itens[0].quantidade, "sucos")
print("   sao o mesmo item?", p1.itens[0] is p2.itens[0])

# --- por que assim ---------------------------------------------------
# Quando o item e compartilhado, mexer em um pedido estraga o outro.
# Na composicao, o todo cria as partes e ninguem mais tem a
# referencia -- por isso cada pedido fica com o seu. E o teste do
# apagar: um item so faz sentido dentro do seu pedido.
