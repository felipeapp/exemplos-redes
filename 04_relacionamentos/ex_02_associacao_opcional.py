"""
Exercicio 02 | Associacao opcional: o entregador chega depois.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Acrescente o Entregador (nome, veiculo). Todo pedido nasce sem
    entregador. Escreva atribuir(entregador) e um metodo situacao()
    que diga "aguardando entregador" ou "com <nome>".

Rode:  python3 ex_02_associacao_opcional.py
"""


# --- solucao ---------------------------------------------------------
class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Entregador:
    def __init__(self, nome: str, veiculo: str) -> None:
        self.nome = nome
        self.veiculo = veiculo


class Pedido:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self.numero = numero
        self.cliente = cliente
        self.entregador = None        # ainda ninguem

    def atribuir(self, entregador: Entregador) -> None:
        self.entregador = entregador

    def situacao(self) -> str:
        if self.entregador is None:
            return "aguardando entregador"
        return f"com {self.entregador.nome} ({self.entregador.veiculo})"


# --- demonstracao ----------------------------------------------------
pedido = Pedido(1, Cliente("Ana"))
print(f"pedido {pedido.numero}:", pedido.situacao())

bruno = Entregador("Bruno", "moto")
pedido.atribuir(bruno)
print(f"pedido {pedido.numero}:", pedido.situacao())

# --- por que assim ---------------------------------------------------
# None representa "ainda nao conhece ninguem". Por isso, antes de
# usar o entregador, o metodo confere com 'is None'. No diagrama de
# classes, essa associacao tem multiplicidade 0..1.
