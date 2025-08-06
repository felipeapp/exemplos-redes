import csv
from dataclasses import dataclass
from datetime import datetime

NOME_ARQUIVO = "vendas.csv"


@dataclass
class Venda:
    codigo: int
    nome: str
    valor: float
    data: datetime


def verificar_arquivo() -> None:
    with open(NOME_ARQUIVO, "a", encoding="utf-8", newline=""):
        pass


def criar_venda(codigo: str, nome: str, valor: str, data: str) -> Venda:
    return Venda(codigo=int(codigo), nome=nome, valor=float(valor), data=datetime.fromisoformat(data))


def salvar(venda: Venda) -> None:
    with open(NOME_ARQUIVO, "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([venda.codigo, venda.nome, venda.valor, venda.data])


def calcular_periodo(mes: int, ano: int) -> float:
    total = 0

    with open(NOME_ARQUIVO, encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")

        for codigo, nome, valor, data in leitor:
            venda = criar_venda(codigo, nome, valor, data)
            if venda.data.month == mes and venda.data.year == ano:
                total += venda.valor

    return total


def buscar_por_codigo(codigo_busca: int) -> Venda | None:
    resultado = None

    with open(NOME_ARQUIVO, encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")

        for codigo, nome, valor, data in leitor:
            if int(codigo) == codigo_busca:
                resultado = criar_venda(codigo, nome, valor, data)
                break

    return resultado


def listar() -> None:
    with open(NOME_ARQUIVO, encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")
        for codigo, nome, valor, data in leitor:
            imprimir(criar_venda(codigo, nome, valor, data))


def imprimir(venda: Venda) -> None:
    print(f"\nCódigo: {venda.codigo}")
    print(f"Nome: {venda.nome}")
    print(f"Valor: R${venda.valor:.2f}")
    print(f"Data: {venda.data.strftime('%H:%M %d/%m/%Y')}")
