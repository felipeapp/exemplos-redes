from dataclasses import dataclass
from datetime import datetime


@dataclass
class Venda:
    codigo: int
    nome: str
    valor: float
    data: datetime


def calcular_periodo(vendas: list[Venda], mes: int, ano: int) -> float:
    total = 0

    for v in vendas:
        if v.data.month == mes and v.data.year == ano:
            total += v.valor

    return total


def buscar_por_codigo(vendas: list[Venda], codigo: int) -> Venda | None:
    resultado = None

    for v in vendas:
        if v.codigo == codigo:
            resultado = v
            break

    return resultado


def imprimir(venda: Venda) -> None:
    print(f"\nCódigo: {venda.codigo}")
    print(f"Nome: {venda.nome}")
    print(f"Valor: R${venda.valor:.2f}")
    print(f"Data: {venda.data.strftime('%H:%M %d/%m/%Y')}")
