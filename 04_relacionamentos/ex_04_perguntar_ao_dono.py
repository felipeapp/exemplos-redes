"""
Exercicio 04 | Comunicacao: perguntar a quem tem o dado.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie uma etiqueta de entrega para o pedido, no formato "#1 - Ana
    - Rua das Flores, 10". Em vez de o pedido montar tudo mexendo
    nos atributos do cliente, faca o cliente responder a parte dele.

Rode:  python3 ex_04_perguntar_ao_dono.py
"""


# --- solucao ---------------------------------------------------------
class Cliente:
    def __init__(self, nome: str, endereco: str) -> None:
        self.nome = nome
        self.endereco = endereco

    def identificacao(self) -> str:
        return f"{self.nome} - {self.endereco}"


class Pedido:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self.numero = numero
        self.cliente = cliente

    def etiqueta(self) -> str:
        return f"#{self.numero} - {self.cliente.identificacao()}"


# --- demonstracao ----------------------------------------------------
ana = Cliente("Ana", "Rua das Flores, 10")
print(Pedido(1, ana).etiqueta())
print(Pedido(2, ana).etiqueta())

# --- por que assim ---------------------------------------------------
# Cada objeto cuida do que e seu. Se o formato da identificacao
# mudar -- incluir o telefone, por exemplo --, so a classe Cliente
# muda. O pedido nao precisa conhecer os detalhes internos do
# cliente: so pedir a ele.
