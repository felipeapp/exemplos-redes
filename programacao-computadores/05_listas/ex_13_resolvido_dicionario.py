dicionario = {}

while True:
    print(30 * "-")
    print("0. Finalizar programa")
    print("1. Adicionar palavra")
    print("2. Listar palavras")
    print("3. Consultar palavra")
    print("4. Remover palavra")
    opcao = int(input(">> "))

    if opcao == 0:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        palavra = input("Digite a palavra a ser adicionada: ").lower()
        significado = input(f"Digite o significado de '{palavra}': ")

        dicionario[palavra] = significado
        print("Dicionário atualizado com sucesso!")
    elif opcao == 2:
        for palavra, significado in dicionario.items():
            print(f"{palavra}: {significado}")
    elif opcao == 3:
        palavra = input("Digite a palavra a buscar: ").lower()
        significado = dicionario.get(palavra)

        if significado is None:
            print(f"A palavra '{palavra}' não foi encontrada!")
        else:
            print(f"Significado: {significado}")
    elif opcao == 4:
        palavra = input("Digite a palavra a remover: ").lower()

        if palavra in dicionario:
            del dicionario[palavra]
            print(f"A palavra '{palavra}' foi removida com sucesso!")
        else:
            print(f"A palavra '{palavra}' não foi encontrada!")
    else:
        print("Opção inválida, tente novamente!")
