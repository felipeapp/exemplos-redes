"""
Exercicio 10 | O tipo do argumento decide o comportamento.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Escreva buscar(chave) no cardapio, que encontre um produto pelo
    codigo (se a chave for int) ou pelo nome (se for str). Devolva
    None se nao encontrar.

Rode:  python3 ex_10_tipo_decide.py
"""


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, codigo: int, nome: str, preco: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class Cardapio:
    def __init__(self) -> None:
        self.produtos: list[Produto] = []

    def incluir(self, *produtos: Produto) -> None:
        for p in produtos:
            self.produtos.append(p)

    def buscar(self, chave: int | str) -> Produto | None:
        for p in self.produtos:
            if isinstance(chave, int) and p.codigo == chave:
                return p
            if isinstance(chave, str) and p.nome == chave:
                return p
        return None


# --- demonstracao ----------------------------------------------------
cardapio = Cardapio()
cardapio.incluir(Produto(1, "Suco de caju", 800),
                 Produto(2, "Feijoada", 4500))

feijoada = cardapio.buscar(2)
suco = cardapio.buscar("Suco de caju")
if feijoada is not None:
    print(feijoada.nome)                     # pelo codigo
if suco is not None:
    print(suco.codigo)                       # pelo nome
print(cardapio.buscar(99))                   # None

# --- por que assim ---------------------------------------------------
# E o mais proximo da sobrecarga do Java: o mesmo metodo reage ao
# tipo do que recebe. Use com moderacao -- se os testes de tipo
# comecarem a crescer, o metodo vira um emaranhado.
