"""
Exercicio 05 | Agregacao: o cardapio reune produtos.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie Produto (codigo, nome, preco em centavos) e Cardapio (nome,
    lista de produtos). O cardapio recebe produtos prontos em
    incluir() e pode retirar(). Coloque o mesmo produto em dois
    cardapios, retire de um e mostre que ele continua no outro.

Rode:  python3 ex_05_agregacao_cardapio.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, codigo: int, nome: str, preco: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.preco = preco            # em centavos

    def __str__(self) -> str:
        return f"{self.nome:<16} {reais(self.preco)}"


class Cardapio:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.produtos: list[Produto] = []

    def incluir(self, produto: Produto) -> None:       # recebe o produto PRONTO
        self.produtos.append(produto)

    def retirar(self, produto: Produto) -> None:
        if produto in self.produtos:
            self.produtos.remove(produto)

    def listar(self) -> None:
        print(f"--- {self.nome} ---")
        for p in self.produtos:
            print("  ", p)


# --- demonstracao ----------------------------------------------------
suco = Produto(1, "Suco de caju", 800)
feijoada = Produto(2, "Feijoada", 4500)
sopa = Produto(3, "Sopa de legumes", 2200)

almoco = Cardapio("Almoco")
noite = Cardapio("Noite")
almoco.incluir(suco)
almoco.incluir(feijoada)
noite.incluir(suco)                   # o mesmo suco nos dois
noite.incluir(sopa)

noite.retirar(suco)
almoco.listar()
noite.listar()
print("o suco continua existindo:", suco.nome)

# --- por que assim ---------------------------------------------------
# Na agregacao, as partes vem de fora e tem vida propria. O suco
# existia antes dos cardapios, pode estar em varios ao mesmo tempo,
# e retira-lo de um cardapio so desfaz a ligacao -- nao destroi o
# produto.
