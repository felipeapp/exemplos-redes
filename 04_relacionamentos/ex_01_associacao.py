"""
Exercicio 01 | Associacao: o pedido conhece o cliente.

Programacao Orientada a Objetos | IFRN

ENUNCIADO
    Crie as classes Cliente (nome, endereco) e Pedido (numero,
    cliente). O pedido deve guardar o OBJETO cliente, e nao copias
    dos seus dados. Mostre que, quando o cliente muda de endereco,
    todos os pedidos dele enxergam a mudanca.

Rode:  python3 ex_01_associacao.py
"""


# --- solucao ---------------------------------------------------------
class Cliente:
    def __init__(self, nome: str, endereco: str) -> None:
        self.nome = nome
        self.endereco = endereco


class Pedido:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self.numero = numero
        self.cliente = cliente        # referencia ao objeto


# --- demonstracao ----------------------------------------------------
ana = Cliente("Ana", "Rua das Flores, 10")
p1 = Pedido(1, ana)
p2 = Pedido(2, ana)

print("antes :", p1.cliente.endereco, "|", p2.cliente.endereco)
ana.endereco = "Av. Brasil, 200"
print("depois:", p1.cliente.endereco, "|", p2.cliente.endereco)
print("mesmo cliente nos dois pedidos?", p1.cliente is p2.cliente)

# --- por que assim ---------------------------------------------------
# Guardar o objeto evita duplicar dados: a Ana existe uma vez so, e
# cada pedido aponta para ela. Uma mudanca em um lugar vale para
# todos. Se o pedido copiasse nome e endereco, seria preciso
# corrigir pedido por pedido.
