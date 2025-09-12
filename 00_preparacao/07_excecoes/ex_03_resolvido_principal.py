from ex_03_resolvido_funcoes import ler_float, ler_int


def main() -> None:
    ano = ler_int("Digite seu ano de ingresso: ", 2020, 2023)
    nota1 = ler_float("Digite a primeira nota: ", 0, 10)
    nota2 = ler_float("Digite a segunda nota: ", 0, 10)

    print(f"Você ingressou em {ano}")
    print(f"Sua média é {(nota1 + nota2) / 2}")


try:
    main()
except KeyboardInterrupt:
    print("\nExecução cancelada pelo usuário!")
