alunos = []

while True:
    print(40 * "-")
    nome = input("Digite o nome do aluno: ")
    if nome.lower() == "sair":
        break

    while True:
        media = float(input("Digite a média do aluno [0-10]: "))
        if 0 <= media <= 10:
            break
        print("Média inválida, tente novamente!")

    alunos.append([nome, media])

print(40 * "-")
print(f"Lista de alunos: {alunos}")
print(40 * "-")

for a in alunos:
    if a[1] >= 6:
        situacao = "aprovado"
    elif a[1] < 2:
        situacao = "reprovado"
    else:
        situacao = "recuperação"

    print(f"O aluno {a[0]} está na situação {situacao}.")
