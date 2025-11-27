from modelo.dao.produtodao import criar_tabela_produto
from visao.terminal import menu


def main() -> None:
    criar_tabela_produto()
    print("Bem-vindo ao sistema de gerenciamento de produtos!")
    menu()


if __name__ == "__main__":
    main()
