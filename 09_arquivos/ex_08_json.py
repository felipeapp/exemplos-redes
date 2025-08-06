import json

turma = {
    "nome": "Turma Fácil, Fácil e Divertido!",
    "professores": [
        {"nome": "Felipe", "disciplina": "Programação"},
        {"nome": "Chibério", "disciplina": "Sistemas Digitais"},
        {"nome": "Iria", "disciplina": "Introdução às Redes"},
    ],
    "alunos": ["Maria", "Gustavo", "Bruno", "Ana", "João"],
    "media": 8.5,
    "ano_ingresso": 2023,
}

print(turma)
print(40 * "-")
print(json.dumps(turma, indent=4))

with open("turma.json", "w", encoding="utf-8") as arquivo:
    json.dump(turma, arquivo, indent=4)

with open("turma.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(40 * "-")
print(dados)
print(dados["nome"])
print(dados["professores"][0])
