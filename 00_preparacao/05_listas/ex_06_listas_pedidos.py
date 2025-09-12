"""
Exemplo de listas de listas.

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

pedidos = []

while True:
    print(40 * "-")
    print("0 - Encerrar o programa")
    print("1 - Adicionar um novo produto")
    opcao = int(input("Escolha sua opção: "))
    print(40 * "-")

    if opcao == 0:
        if pedidos:
            total = 0

            for item in pedidos:
                valor = item[1] * item[2]
                total += valor
                print(f"{item[0]} = {item[1]} x R$ {item[2]} = R$ {valor}")

            print(f"Valor total: R$ {total}")
        else:
            print("Não existem pedidos!")

        break
    elif opcao == 1:
        while True:
            nome = input("Digite o nome do produto: ")
            if len(nome) >= 3:
                break
            print("Nome inválido, precisa ter pelo menos 3 caracteres!")

        while True:
            preco = float(input("Digite o preço unitário: "))
            if preco > 0:
                break
            print("Preço inválido, tente novamente!")

        while True:
            quantidade = int(input("Digite a quantidade de itens: "))
            if quantidade > 0:
                break
            print("Quantidade inválida, tente novamente!")

        pedidos.append([nome, preco, quantidade])
        print("Produto adicionado ao carrinho!")
    else:
        print("Opção inválida, tente novamente!")
