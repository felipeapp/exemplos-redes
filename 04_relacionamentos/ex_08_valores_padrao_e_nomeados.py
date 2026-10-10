"""
Exercicio 08 | Sobrecarga com valores padrao e argumentos nomeados.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Em vez de tres metodos diferentes, escreva um unico
    adicionar(produto, quantidade=1, observacao="") que aceite ser
    chamado de varios jeitos. Mostre tambem a chamada com argumento
    nomeado, informando so a observacao.

Rode:  python3 ex_08_valores_padrao_e_nomeados.py
"""


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int, observacao: str) -> None:
        self.produto = produto
        self.quantidade = quantidade
        self.observacao = observacao

    def __str__(self) -> str:
        obs = f"  ({self.observacao})" if self.observacao else ""
        return f"{self.quantidade}x {self.produto.nome}{obs}"


class Pedido:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int = 1, observacao: str = "") -> None:
        self.itens.append(ItemPedido(produto, quantidade, observacao))


# --- demonstracao ----------------------------------------------------
suco = Produto("Suco de caju", 800)
burger = Produto("Hamburguer", 2900)

pedido = Pedido(1)
pedido.adicionar(suco)                              # tudo padrao
pedido.adicionar(suco, 2)                           # so a quantidade
pedido.adicionar(burger, 1, "sem cebola")           # tudo informado
pedido.adicionar(burger, observacao="ao ponto")     # pula a quantidade

for item in pedido.itens:
    print(item)

# --- por que assim ---------------------------------------------------
# Python nao tem sobrecarga automatica: se voce definir dois
# adicionar(), o segundo apaga o primeiro. Valores padrao resolvem a
# maior parte dos casos, e argumentos nomeados permitem pular os
# parametros que nao interessam.
