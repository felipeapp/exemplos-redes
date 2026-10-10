"""
Exercicio 12 | Heranca: o comum sobe para a superclasse.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie Produto com codigo, nome, preco e __str__. Depois crie
    Bebida e Prato herdando de Produto, sem escrever nada dentro
    delas, e mostre que ja funcionam.

Rode:  python3 ex_12_heranca_basica.py
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


class Bebida(Produto):     # Bebida herda de Produto
    pass


class Prato(Produto):      # Prato herda de Produto
    pass


# --- demonstracao ----------------------------------------------------
suco = Bebida(1, "Suco de caju", 800)
feijoada = Prato(2, "Feijoada", 4500)

print(suco)
print(feijoada)
print("tipo do suco:", type(suco).__name__)

# --- por que assim ---------------------------------------------------
# O nome entre parenteses diz de quem a classe herda. Construtor e
# __str__ vieram prontos de Produto: o codigo comum foi escrito uma
# vez so. Se a regra de exibicao mudar, muda em Produto e vale para
# as duas.
