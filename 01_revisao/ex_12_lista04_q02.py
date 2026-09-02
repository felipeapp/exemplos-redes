from dataclasses import dataclass


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

    while True:
        media = float(input("Digite a média do aluno: "))
        if 0 <= media <= 10:
            break
        print("Média inválida! Digite um valor entre 0 e 10.")

    alunos.append(Aluno(nome, media))

print("-" * 40)

for a in alunos:
    if a.media >= 6:
        situacao = "Aprovado"
    elif a.media < 2:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"

    print(f"Nome: {a.nome}")
    print(f"Média: {a.media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 40)
