# [matricula, nome, nota 1, nota 2]
alunos = [[1001, "Felipe", 9.0, 10.0], [1002, "Ana", 5.0, 2.0], [1003, "João", 5.8, 4.9]]

# Qual a média do aluno Felipe?
print((alunos[0][2] + alunos[0][3]) / 2)

# Quanto é a média geral da turma?
geral = 0

for aluno in alunos:
    media = (aluno[2] + aluno[3]) / 2
    geral += media
    print(f"{aluno[1]} ({aluno[0]}) = {media}")

print(f"Média Geral: {geral / len(alunos)}")
