"""
Exercicio 15 | Visibilidade na heranca: _protegido e __privado.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Mostre que um atributo com um underscore pode ser usado pela
    subclasse, e que um atributo com dois underscores nao chega a
    ela com o mesmo nome.

Rode:  python3 ex_15_visibilidade_heranca.py
"""


def reais(centavos: int) -> str:
    """Formata um valor em centavos como R$ 12,50."""
    return f"R$ {centavos // 100},{centavos % 100:02d}"


# --- solucao ---------------------------------------------------------
class Produto:
    def __init__(self, codigo: int, nome: str, preco: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self._preco = preco           # protegido: a familia pode usar
        self.__custo = preco // 2     # privado: so Produto

    @property
    def preco(self) -> int:
        return self._preco


class Bebida(Produto):
    def __init__(self, codigo: int, nome: str, preco: int, volume_ml: int) -> None:
        super().__init__(codigo, nome, preco)
        self.volume_ml = volume_ml

    def preco_por_litro(self) -> int:
        return self._preco * 1000 // self.volume_ml      # funciona


# --- demonstracao ----------------------------------------------------
suco = Bebida(1, "Suco de caju", 800, 500)
print("preco por litro:", reais(suco.preco_por_litro()))
print("de fora, pela property:", reais(suco.preco))

# O privado foi renomeado com o nome da classe ONDE foi criado:
print("existe _Produto__custo?", hasattr(suco, "_Produto__custo"))
print("existe _Bebida__custo? ", hasattr(suco, "_Bebida__custo"))
# Por isso, dentro de Bebida, self.__custo procuraria _Bebida__custo
# -- que nao existe -- e o programa pararia com AttributeError.

# --- por que assim ---------------------------------------------------
# Um underscore quer dizer "interno, mas a familia pode usar": e o
# padrao para dados que as subclasses precisam. Dois underscores
# ativam o name mangling com o nome da classe, e por isso atrapalham
# a heranca. Regra pratica: um underscore; dois so com motivo claro.
