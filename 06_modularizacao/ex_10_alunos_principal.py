import ex_10_alunos_funcoes as alunos


def main() -> None:
    nota1 = alunos.ler_nota("Digite a primeira nota: ", "Primeira nota inválida!")
    nota2 = alunos.ler_nota("Digite a segunda nota: ", "Segunda nota inválida!")
    nota3 = alunos.ler_nota("Digite a terceira nota: ", "Terceira nota inválida!")
    nota4 = alunos.ler_nota("Digite a quarta nota: ", "Quarta nota inválida!")

    media = alunos.media_aritmetica(nota1, nota2, nota3, nota4)

    print(f"Média: {media:.2f}")
    alunos.mostrar_situacao(media)


if __name__ == "__main__":
    main()
