def calcular_media(n1: float, n2: float, n3: float, tipo: str) -> float:
    if tipo == "A":
        media = (n1 + n2 + n3) / 3
    elif tipo == "P":
        media = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    else:
        media = -1

    return media


def main() -> None:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    tipo = input("Digite o tipo de média (A ou P): ").upper()

    media_aritmetica = calcular_media(nota1, nota2, nota3, tipo)
    print(f"Média: {media_aritmetica:.2f}")


if __name__ == "__main__":
    main()
