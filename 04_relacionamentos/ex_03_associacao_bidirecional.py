"""
Exercicio 03 | Associacao bidirecional: o cliente ve seus pedidos.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Faca o cliente conhecer os proprios pedidos. Garanta que os dois
    lados fiquem sempre juntos: ao criar um pedido, ele ja deve
    aparecer na lista do cliente.

Rode:  python3 ex_03_associacao_bidirecional.py
"""


# --- solucao ---------------------------------------------------------
class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.pedidos: list[Pedido] = []             # o outro lado da associacao

    def quantos_pedidos(self) -> int:
        return len(self.pedidos)


class Pedido:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self.numero = numero
        self.cliente = cliente
        cliente.pedidos.append(self)  # mantem os dois lados juntos


# --- demonstracao ----------------------------------------------------
ana = Cliente("Ana")
Pedido(1, ana)
Pedido(2, ana)
Pedido(3, Cliente("Bruno"))

print(ana.nome, "fez", ana.quantos_pedidos(), "pedidos:")
for p in ana.pedidos:
    print("  pedido", p.numero, "- cliente:", p.cliente.nome)

# --- por que assim ---------------------------------------------------
# Na associacao bidirecional, o risco e um lado saber e o outro nao.
# Colocando o registro dentro do construtor do Pedido, e impossivel
# criar um pedido sem que o cliente fique sabendo. Mesmo assim, use
# bidirecional so quando os dois lados realmente precisarem navegar.
