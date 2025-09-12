def ler_quantidade() -> int:
    while True:
        try:
            valor = int(input("Digite a quantidade do prduto: "))

            if valor > 0:
                return valor

            print("A quantidade deve ser maior do que zero!")
        except ValueError:
            print("O valor digitado não é um número inteiro!")


def ler_preco() -> float:
    while True:
        try:
            valor = float(input("Digite o preco do produto: "))

            if valor > 0:
                return valor

            print("O preço deve ser maior do que zero!")
        except ValueError:
            print("O valor digitado não é um número real!")


def ler_nome() -> str:
    while True:
        valor = input("Digite o nome do produto: ")

        if len(valor) >= 3:
            return valor

        print("O nome deve ter pelo menos três caracteres!")
