def letreiro(tipo: str, disciplina: str = "Programação de Computadores") -> None:
    print(50 * "*")

    if tipo == "cabecalho":
        print("Bem Vindo!".center(50))
    elif tipo == "rodape":
        print("Até mais, foi um Prazer!".center(50))

    print("Instituto Federal do Rio Grande do Norte".center(50))
    print("Campus São Gonçalo do Amarante".center(50))
    print(f"Disciplina {disciplina}".center(50))
    print(50 * "*")


letreiro("cabecalho")
nome = input("Digite seu nome: ")
print(f"Bem vindo ao IFRN Campus SGA {nome}!")
letreiro("rodape", "Programação para Redes")
