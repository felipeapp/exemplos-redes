def ler_int(mensagem: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                break
            print(f"O valor deve estar entre {minimo} e {maximo}!")
        except ValueError:
            print("O valor não é um número inteiro!")

    return valor


def ler_float(mensagem: str, minimo: int, maximo: int) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                break
            print(f"O valor deve estar entre {minimo} e {maximo}!")
        except ValueError:
            print("O valor não é um número real!")

    return valor


if __name__ == "__main__":
    print(ler_int("Digite a idade: ", 0, 120))
    print(ler_int("Digite a nota: ", 0, 100))

    print(ler_float("Digite o preço: ", 0, 1000))
    print(ler_float("Digite a nota: ", 0, 10))
