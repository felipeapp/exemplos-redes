import csv

with open("contatos.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")

    for nome, email, telefone in leitor:
        print(nome)
        print(email)
        print(telefone)
        print("###")

print("Fim do arquivo!")
