"""
Exercicio 20 | Da escada de isinstance a sobrescrita.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Escreva uma etiqueta diferente para cada tipo de produto,
    primeiro com uma escada de isinstance, depois com descricao()
    sobrescrita em cada classe. Acrescente uma Sobremesa e compare o
    trabalho nas duas versoes.

Rode:  python3 ex_20_escada_vs_sobrescrita.py
"""


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def descricao(self) -> str:
        return self.nome


class Prato(Produto):
    def __init__(self, nome: str, serve: int) -> None:
        super().__init__(nome)
        self.serve = serve

    def descricao(self) -> str:
        return f"{self.nome} (serve {self.serve})"


class Bebida(Produto):
    def __init__(self, nome: str, volume_ml: int) -> None:
        super().__init__(nome)
        self.volume_ml = volume_ml

    def descricao(self) -> str:
        return f"{self.nome} ({self.volume_ml} ml)"


class Sobremesa(Produto):                     # classe nova
    def descricao(self) -> str:
        return f"{self.nome} (sobremesa)"


def etiqueta_com_escada(p: Produto) -> str:
    if isinstance(p, Bebida):
        return f"{p.nome} ({p.volume_ml} ml)"
    if isinstance(p, Prato):
        return f"{p.nome} (serve {p.serve})"
    return p.nome                             # a Sobremesa cai aqui


# --- demonstracao ----------------------------------------------------
cardapio = [Prato("Feijoada", 2), Bebida("Suco de caju", 500),
            Sobremesa("Pudim")]

print("com a escada de isinstance:")
for p in cardapio:
    print("  ", etiqueta_com_escada(p))

print("com descricao() sobrescrita:")
for p in cardapio:
    print("  ", p.descricao())

# --- por que assim ---------------------------------------------------
# Na escada, cada classe nova obriga a voltar a funcao e acrescentar
# mais um if -- e a Sobremesa saiu sem a marca porque ninguem lembrou.
# Com a sobrescrita, cada classe responde por si e a Sobremesa
# trouxe a propria descricao. Se o codigo pergunta o tipo para fazer
# a mesma coisa de jeitos diferentes, ele esta pedindo uma
# sobrescrita: e o polimorfismo, que vem mais adiante.
