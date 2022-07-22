alunos = []

while True:
    print(50 * "-")

    # Leitura do nome
    nome = input("Digite o nome do aluno: ")
    if nome.lower() == "sair":
        print()
        break

    # Leitura da média
    while True:
        media = float(input("Digite a média do aluno: "))
        if 0 <= media <= 10:
            break
        print("Média inválida, tente novamente!")

    # Adiciona nome e média na lista de alunos
    alunos.append([nome, media])

for nome, media in alunos:
    if media >= 6:
        situacao = "aprovado(a)"
    elif media < 2:
        situacao = "reprovado(a)"
    else:
        situacao = "em recuperação"

    print(f"{nome} tem média {media} e está {situacao}!")
