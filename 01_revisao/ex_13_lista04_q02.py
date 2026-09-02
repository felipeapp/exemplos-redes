from dataclasses import dataclass


def calcular_situacao(media: float) -> str:
    if media >= 6:
        situacao = "Aprovado"
    elif media < 2:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"

    return situacao


def ler_media() -> float:
    while True:
        media = float(input("Digite a média do aluno: "))

        if 0 <= media <= 10:
            break

        print("Média inválida! Digite um valor entre 0 e 10.")

    return media


@dataclass
class Aluno:
    nome: str
    media: float


alunos = []

while True:
    print("-" * 40)
    nome = input("Digite o nome ou sair para encerrar: ")

    if nome.lower() == "sair":
        break

    media = ler_media()
    alunos.append(Aluno(nome, media))

print("-" * 40)

for a in alunos:
    print(f"Nome: {a.nome}")
    print(f"Média: {a.media:.2f}")
    print(f"Situação: {calcular_situacao(a.media)}")
    print("-" * 40)
