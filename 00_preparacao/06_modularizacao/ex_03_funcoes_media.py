def ler_nota(mensagem: str, erro: str) -> float:
    while True:
        nota = float(input(mensagem))

        if 0 <= nota <= 10:
            return nota

        print(erro)


def media_aritmetica(v1: float, v2: float, v3: float, v4: float) -> float:
    return (v1 + v2 + v3 + v4) / 4


def mostrar_situacao(m: float) -> None:
    if m >= 6:
        print("O aluno está aprovado!")
    elif m < 2:
        print("O aluno está reprovado!")
    else:
        print("O aluno está em recuperação!")


nota1 = ler_nota("Digite a primeira nota: ", "Primeira nota inválida!")
nota2 = ler_nota("Digite a segunda nota: ", "Segunda nota inválida!")
nota3 = ler_nota("Digite a terceira nota: ", "Terceira nota inválida!")
nota4 = ler_nota("Digite a quarta nota: ", "Quarta nota inválida!")

media = media_aritmetica(nota1, nota2, nota3, nota4)

print(f"Média: {media:.2f}")
mostrar_situacao(media)
