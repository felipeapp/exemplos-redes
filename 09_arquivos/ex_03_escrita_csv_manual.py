nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
telefone = input("Digite o telefone: ")

with open("contatos.csv", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome};{email};{telefone}\n")
