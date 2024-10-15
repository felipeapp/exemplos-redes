import csv

nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
telefone = input("Digite o telefone: ")

with open("contatos.csv", "a", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow([nome, email, telefone])

print("Dados salvos!")
