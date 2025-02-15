import requests

WS_URL_PREFIXO = "http://localhost:8080/palavras"

while True:
    print("-" * 50)
    print("0. Sair do programa")
    print("1. Adicionar ou atualizar palavra")
    print("2. Listar todas as palavras")
    print("3. Buscar uma palavra")
    print("4. Remover uma palavra")
    opcao = int(input("Escolha sua opção: "))

    if opcao == 0:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        palavra = input("Digite a palavra: ")
        significado = input("Digite o significado: ")

        with requests.post(
            WS_URL_PREFIXO, json={"palavra": palavra, "significado": significado}, timeout=10
        ) as resposta:
            if resposta.status_code == 200:
                print(f"A palavra {palavra} foi atualizada com sucesso!")
            elif resposta.status_code == 201:
                print(f"A palavra {palavra} foi adicionada com sucesso!")
            else:
                print("Erro ao adicionar a palavra!")
    elif opcao == 2:
        with requests.get(WS_URL_PREFIXO, timeout=10) as resposta:
            if resposta.status_code == 200:
                dicionario = resposta.json()

                if dicionario:
                    for palavra, significado in dicionario.items():
                        print(f"{palavra} = {significado}")
                else:
                    print("Não há palavras no dicionário!")
            else:
                print("Erro ao realizar a requisição!")
    elif opcao == 3:
        palavra = input("Digite a palavra: ")

        with requests.get(f"{WS_URL_PREFIXO}/{palavra}", timeout=10) as resposta:
            if resposta.status_code == 200:
                significado = resposta.json()["resposta"][palavra]
                print(f"{palavra} = {significado}")
            elif resposta.status_code == 404:
                print(f"A palavra '{palavra}' não foi encontrada!")
            else:
                print("Erro ao realizar a requisição!")
    elif opcao == 4:
        palavra = input("Digite a palavra a ser removida: ")

        with requests.delete(f"{WS_URL_PREFIXO}/{palavra}", timeout=10) as resposta:
            if resposta.status_code == 200:
                significado = resposta.json()["resposta"][palavra]

                print("Palavra encontrada:")
                print(f"{palavra} = {significado}")
                print("A palavra foi removida com sucesso!")
            elif resposta.status_code == 404:
                print(f"A palavra '{palavra}' não foi encontrada!")
            else:
                print("Erro ao realizar a requisição!")
    else:
        print("Opção inválida, tente novamente!")
