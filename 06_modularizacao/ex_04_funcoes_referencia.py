def dobrar_lista(lista: list[int]) -> None:
    for i, e in enumerate(lista):
        lista[i] = 2 * e


def dobrar_valor(valor_simples: int) -> None:
    valor_simples *= 2


numeros = [5, 6, 8, 9, 10, 4]
numero = 10

dobrar_lista(numeros)  # A lista é passada por referência
dobrar_valor(numero)  # O número é passado por valor/cópia

print(numeros)
print(numero)
