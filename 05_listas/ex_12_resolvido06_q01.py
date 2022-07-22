dicionario = {}
# dicionario = dict()

while True:
    print(30 * "-")
    print("Escolha uma opção:")
    print("0 - Finalizar")
    print("1 - Adicionar palavra")
    print("2 - Consultar palavra")
    print("3 - Remover palavra")
    print("4 - Listar palavras")
    opcao = int(input(">> "))
    print(30 * "-")

    if opcao == 0:
        print("Finalizando o programa...")
        break
    elif opcao == 1:
        palavra = input("Digite a palavra: ").lower()
        significado = input(f"Digite o significado de '{palavra}': ")

        dicionario[palavra] = significado
        print("A operação foi realizada com sucesso!")
    elif opcao == 2:
        palavra = input("Digite a palavra: ").lower()

        # Retorna o valor da palavra ou o texto informado caso ela não exista
        print(dicionario.get(palavra, f"A palavra {palavra} não foi encontrada!"))

        # if palavra in dicionario:
        #     print(dicionario[palavra])
        # else:
        #     print(f"A palavra '{palavra}' não foi encontrada!")
    elif opcao == 3:
        palavra = input("Digite e palavra: ").lower()

        if palavra in dicionario:
            del dicionario[palavra]
            print(f"A palavra '{palavra}' foi removida com sucesso!")
        else:
            print(f"A palavra '{palavra}' não foi encontrada!")
    elif opcao == 4:
        for palavra, significado in dicionario.items():
            print(f"{palavra}: {significado}")
    else:
        print("Opção inválida, tente novamente!")
