"""
Exercicio 09 | Quantidade variavel de argumentos com *args.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Faca o metodo incluir() do cardapio aceitar um, varios ou nenhum
    produto na mesma chamada.

Rode:  python3 ex_09_args.py
"""


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco


class Cardapio:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.produtos: list[Produto] = []

    def incluir(self, *produtos: Produto) -> None:     # produtos e uma tupla
        for produto in produtos:
            self.produtos.append(produto)
        print(f"incluidos {len(produtos)}; total no cardapio: "
              f"{len(self.produtos)}")


# --- demonstracao ----------------------------------------------------
suco = Produto("Suco de caju", 800)
feijoada = Produto("Feijoada", 4500)
pudim = Produto("Pudim", 1200)

almoco = Cardapio("Almoco")
almoco.incluir(suco)                       # um
almoco.incluir(feijoada, pudim)            # varios
almoco.incluir()                           # nenhum, sem erro

# --- por que assim ---------------------------------------------------
# O asterisco junta todos os argumentos posicionais em uma tupla.
# Dentro do metodo, um laco trata todos do mesmo jeito -- seja um,
# sejam varios. E o equivalente aos varargs do Java (Produto...
# produtos).
