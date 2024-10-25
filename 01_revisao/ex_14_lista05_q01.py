def calcular_media(n1: float, n2: float, n3: float, tipo: str) -> float:
    if tipo == "A":
        media = (n1 + n2 + n3) / 3
    elif tipo == "P":
        media = (5 * n1 + 3 * n2 + 2 * n3) / 10
    else:
        media = -1

    return media


def ler_nota(mensagem: str) -> float:
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
            break
        print("Nota inválida, tente novamente!")

    return nota


def main() -> None:
    nota1 = ler_nota("Digite a primeira nota: ")
    nota2 = ler_nota("Digite a segunda nota: ")
    nota3 = ler_nota("Digite a terceira nota: ")
    tipo = input("Digite o tipo de média (A ou P): ")

    resultado = calcular_media(nota1, nota2, nota3, tipo)
    print(f"A média é {resultado:.2f}")


if __name__ == "__main__":
    main()
