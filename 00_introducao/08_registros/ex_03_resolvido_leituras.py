from datetime import datetime


def ler_data(mensagem: str) -> datetime:
    while True:
        try:
            valor = datetime.strptime(input(mensagem), "%H:%M %d/%m/%Y")
            break
        except ValueError:
            print("A data informada não é válida, use o formato hh:mm dd/mm/aaaa!")

    return valor


def ler_codigo(mensagem: str, minimo: int) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                break
            print(f"O valor deve ser maior ou igual a {minimo}!")
        except ValueError:
            print("O valor não é um número inteiro!")

    return valor


def ler_valor(mensagem: str, minimo: float) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= minimo:
                break
            print(f"O valor deve ser maior ou igual a {minimo} !")
        except ValueError:
            print("O valor não é um número real!")

    return valor
