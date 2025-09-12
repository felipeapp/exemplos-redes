# Lembrando que venda é uma lista:
# [codigo, nome, valor, dia, mes, ano]
def imprimir_venda(venda: list) -> None:
    print(f"\nCódigo: {venda[0]}")
    print(f"Cliente: {venda[1]}")
    print(f"Valor: R$ {venda[2]:.2f}")
    print(f"Data: {venda[3]}/{venda[4]}/{venda[5]}")


def buscar_por_codigo(vendas: list[list], codigo: int) -> list | None:
    for v in vendas:
        if v[0] == codigo:
            return v

    return None


def calcular_rendimento(vendas: list[list], mes: int, ano: int) -> float:
    rendimento = 0

    for v in vendas:
        if v[4] == mes and v[5] == ano:
            rendimento += v[2]

    return rendimento


if __name__ == "__main__":
    print("Teste das funções!")
    imprimir_venda([1, "Felipe", 100, 12, 12, 2024])
