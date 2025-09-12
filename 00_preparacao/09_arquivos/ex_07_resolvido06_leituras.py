from datetime import datetime


def ler_opcao() -> int:
    print(30 * "-")
    print("0 - Sair do programa")
    print("1 - Cadastrar uma venda")
    print("2 - Listar todas as vendas cadastradas")
    print("3 - Mostrar uma venda a partir de seu código")
    print("4 - Calcular o valor total das vendas em um mês do ano")

    try:
        opcao = int(input("Escolha sua opção: "))
    except ValueError:
        opcao = -1

    return opcao


def ler_data() -> datetime:
    while True:
        try:
            valor = datetime.strptime(input("Digite a data da venda (hh:mm dd/mm/aaaa): "), "%H:%M %d/%m/%Y")
            break
        except ValueError:
            print("A data informada não é válida, use o formato hh:mm dd/mm/aaaa!")

    return valor


def ler_codigo() -> int:
    while True:
        try:
            valor = int(input("Digite o código da venda: "))
            if valor > 0:
                break
            print("O valor deve ser maior que zero!")
        except ValueError:
            print("O valor não é um número inteiro!")

    return valor


def ler_mes_ano(mensagem: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            if minimo <= numero <= maximo:
                break
            print(f"O valor deve ser entre {minimo} e {maximo}!")
        except ValueError:
            print("O valor não é um número inteiro!")

    return numero


def ler_valor() -> float:
    while True:
        try:
            valor = float(input("Digite o valor da venda: "))
            if valor > 0:
                break
            print("O valor deve ser maior que zero!")
        except ValueError:
            print("O valor não é um número real!")

    return valor


def ler_nome() -> str:
    while True:
        nome = input("Digite o nome do cliente da venda: ")

        if len(nome) >= 3:
            break

        print("O nome deve ter pelo menos três caracteres!")

    return nome
