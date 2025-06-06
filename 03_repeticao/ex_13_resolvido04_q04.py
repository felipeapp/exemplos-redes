while True:
    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de nascimento (dd/mm/aaaa):")
    celular = input("Digite seu número de celular: ")

    print(30 * "-")
    print("Os dados informados foram:")
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {nascimento}")
    print(f"Número do Celular: {celular}")
    print(30 * "-")

    while True:
        confirmacao = input("Os dados estão corretos (sim/não)? ")
        if confirmacao in ("sim", "não"):
            break

    if confirmacao == "sim":
        print("Obrigado pelas informações!")
        break

    print("Ok, então tente novamente!")
