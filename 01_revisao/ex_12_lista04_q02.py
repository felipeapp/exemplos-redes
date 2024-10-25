nomes = []
medias = []

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

    nomes.append(nome)
    medias.append(media)

print(40 * "-")
print(f"Lista de nomes: {nomes}")
print(f"Lista de médias: {medias}")
print(40 * "-")

for i in range(len(nomes)):
    if medias[i] >= 6:
        situacao = "aprovado"
    elif medias[i] < 2:
        situacao = "reprovado"
    else:
        situacao = "recuperação"

    print(f"O aluno {nomes[i]} está na situação {situacao}.")
