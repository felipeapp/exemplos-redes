# [matricula, nome, nota 1, nota 2]
alunos = [
    [1001, "Felipe", 9.5, 10.0],
    [1002, "Ana", 1.5, 2.0],
    [1003, "João", 5.5, 5.0],
]

# Qual a média do aluno Felipe?
print((alunos[0][2] + alunos[0][3]) / 2)

print(30 * "-")

# Acessando diretamente as sublistas
for aluno in alunos:
    media = (aluno[2] + aluno[3]) / 2

    if media > 6:
        situacao = "aprovado"
    elif media < 2:
        situacao = "reprovado"
    else:
        situacao = "em recuperação"

    print(f"{aluno[1]} ({aluno[0]}) teve média {media} e está {situacao}")

print(30 * "-")

# Extraindo os elementos de cada sublista para variáveis
for matricula, nome, nota1, nota2 in alunos:
    media = (nota1 + nota2) / 2

    if media > 6:
        situacao = "aprovado"
    elif media < 2:
        situacao = "reprovado"
    else:
        situacao = "em recuperação"

    print(f"{nome} ({matricula}) teve média {media} e está {situacao}")
