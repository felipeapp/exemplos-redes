def ler_nota(mensagem, erro):
    while True:
        nota = float(input(mensagem))

        if 0 <= nota <= 10:
            return nota

        print(erro)


def media_aritmetica(v1, v2, v3, v4):
    return (v1 + v2 + v3 + v4) / 4


def mostrar_situacao(m):
    if m >= 6:
        print("O aluno está aprovado!")
    elif m < 2:
        print("O aluno está reprovado!")
    else:
        print("O aluno está em recuperação!")


def main():
    nota = ler_nota("Digite uma nota: ", "Nota inválida!")
    print(f"Nota digitada: {nota}")
    print(f"Média: {media_aritmetica(9, 10, 10, 7)}")
    mostrar_situacao(8)


if __name__ == "__main__":
    main()
