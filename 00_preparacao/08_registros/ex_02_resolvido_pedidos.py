"""
Atividade sobre produtos.

Use uma lista de listas para armazenar um conjunto de
produtos com seus preços e quantidades, simulando a ideia
de um carrinho de pedidos. O programa apresentará ao
usuário a opção de encerrar ou adicionar um novo produto.
Se ele escolher adicionar, o programa deve pedir o nome,
o preço e a quantiade do produto, caso ele escolha
encerrar, o programa mostrará a lista de produtos com
seus preços e o valor total do carrinho. O preço e a quantidade
do produto deve ser validado como sempre maior do que zero.
O nome do produto deve sempre ter três caracteres no mínimo.
"""

from dataclasses import dataclass

import ex_02_resolvido_funcoes as funcoes

pedido = []


@dataclass
class Item:
    nome: str
    preco: float
    quantidade: int


def main() -> None:
    while True:
        print(40 * "#")
        print("0 - Encerrar o programa")
        print("1 - Adicionar um novo produto")

        try:
            opcao = int(input("Escolha sua opção: "))
        except ValueError:
            opcao = -1

        print(40 * "#")

        if opcao == 0:
            if pedido:
                valor_pedido = 0

                for item in pedido:
                    valor_item = item.preco * item.quantidade
                    valor_pedido += valor_item
                    print(f"{item.nome}: R$ {item.preco} x {item.quantidade} = R$ {valor_item}")

                print(40 * "-")
                print(f"Total do pedido = R$ {valor_pedido}")
            else:
                print("Nenhum produto adicionado!")

            break
        elif opcao == 1:  # noqa: RET508
            nome = funcoes.ler_nome()
            preco = funcoes.ler_preco()
            quantidade = funcoes.ler_quantidade()

            pedido.append(Item(nome, preco, quantidade))
            print("Produto adicionado!")
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAté mais!")
