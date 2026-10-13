"""
Exercicio 13 | super() e comportamento proprio de cada subclasse.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Faca Bebida receber tambem volume_ml e Prato receber serve
    (quantas pessoas, padrao 1), reaproveitando o construtor de
    Produto com super(). De a Bebida o metodo eh_grande() e ao Prato
    o metodo preco_por_pessoa().

Rode:  python3 ex_13_super_e_comportamento_proprio.py
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

    def __str__(self) -> str:
        return f"{self.nome:<16} {reais(self.preco)}"


class Bebida(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(codigo, nome, preco)    # a parte comum
        self.volume_ml = volume_ml                # a parte nova

    def eh_grande(self) -> bool:
        return self.volume_ml >= 1000


class Prato(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, serve: int = 1) -> None:
        super().__init__(codigo, nome, preco)
        self.serve = serve

    def preco_por_pessoa(self) -> int:
        return self.preco // self.serve


# --- demonstracao ----------------------------------------------------
suco = Bebida(1, "Suco de caju", 800, 500)
jarra = Bebida(2, "Jarra de suco", 2000, 1500)
feijoada = Prato(3, "Feijoada", 4500, serve=2)

print(suco, "| grande?", suco.eh_grande())
print(jarra, "| grande?", jarra.eh_grande())
print(feijoada, "| por pessoa:", reais(feijoada.preco_por_pessoa()))

# --- por que assim ---------------------------------------------------
# Ao escrever um __init__ na subclasse, o da mae deixa de rodar
# sozinho. O super().__init__(...) pede a mae que monte a parte
# comum; a filha so acrescenta o que e seu. Sem ele, codigo, nome e
# preco nunca seriam criados.
