with open("contatos.csv", "r", encoding="utf-8") as arquivo:  # noqa: UP015
    for linha in arquivo:
        nome, email, telefone = linha.strip().split(";")

        print(nome)
        print(email)
        print(telefone)
        print("#")
