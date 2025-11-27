from modelo.dao.produtodao import (
    adicionar_produto,
    atualizar_produto,
    buscar_por_nome_exato,
    buscar_por_nome_similar,
    listar_produtos,
    remover_produto,
)
from modelo.entidade.produto import Produto


def menu() -> None:  # noqa: C901, PLR0912, PLR0915
    while True:
        print(50 * "-")
        print("0 - Sair do programa")
        print("1 - Adicionar produto")
        print("2 - Buscar produto pelo nome exato")
        print("3 - Buscar produto por similaridade de nome")
        print("4 - Listar produtos")
        print("5 - Atualizar preço e quantidade")
        print("6 - Remover um produto")
        opcao = int(input(">> "))

        if opcao == 0:
            print("Finalizando programa...")
            break

        if opcao == 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            medida = input("Digite a medida do produto: ")

            if adicionar_produto(Produto(nome.upper(), preco, quantidade, medida.upper())):
                print("Produto adicionado com sucesso!")
            else:
                print("Erro ao adicionar o produto!")
        elif opcao == 2:
            nome = input("Digite o nome exato do produto: ")
            produto = buscar_por_nome_exato(nome.upper())

            if produto:
                print(produto)
            else:
                print("O nome informado não foi encontrado!")
        elif opcao == 3:
            nome = input("Digite o nome da busca: ")
            produtos = buscar_por_nome_similar(nome.upper())

            if produtos:
                for p in produtos:
                    print(p)
            else:
                print("O nome informado não foi encontrado!")
        elif opcao == 4:
            produtos = listar_produtos()

            if produtos:
                for p in produtos:
                    print(p)
            else:
                print("Não há produtos cadastrados!")
        elif opcao == 5:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o novo preço do produto: "))
            quantidade = int(input("Digite a nova quantidade do produto: "))

            if atualizar_produto(nome.upper(), preco, quantidade):
                print("Produto atualizado com sucesso!")
            else:
                print("Erro ao atualizar produto!")
        elif opcao == 6:
            nome = input("Digite o nome do produto a ser removido: ")

            if remover_produto(nome.upper()):
                print("Produto foi removido com sucesso!")
            else:
                print("Produto não encontrado!")
        else:
            print("Opção inválida, tente novamente!")
