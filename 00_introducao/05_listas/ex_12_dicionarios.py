aluno = {
    "nome": "Felipe Alves",
    "matricula": 1812384,
    "email": "felipe.pinto@ifrn.edu.br",
    "notas": (8.9, 9.5),
    "endereco": {"rua": "Rua da Programação", "numero": 667},
}

print(aluno)
print(aluno["matricula"])
print(aluno["notas"])
print(aluno["notas"][0])
print(aluno["notas"][1])
print(aluno["endereco"])
print(aluno["endereco"]["rua"])
print(aluno["endereco"]["numero"])

aluno["curso"] = "Ciência da Computação"
aluno["endereco"]["numero"] = "665"
aluno["endereco"]["bairro"] = "Feliz"
print(aluno)

del aluno["endereco"]
print(aluno)

for chave, valor in aluno.items():
    print(f"{chave} = {valor}")
