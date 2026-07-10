def letreiro() -> None:
    print(50 * "*")
    print("Instituto Federal do Rio Grande do Norte".center(50))
    print("Campus São Gonçalo do Amarante".center(50))
    print("Disciplina Programação de Computadores".center(50))
    print(50 * "*")


letreiro()
nome = input("Digite seu nome: ")
print(f"Bem vindo ao IFRN Campus SGA {nome}!")
letreiro()
